#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
script name: sparced_simulation.py
Created on Thurs. 04/23/2024 9:00:00
Author: Jonah R. Huggins

Description: This file conducts user defined, condition-specific simulations \
using SPARCED and returns the results as nested NumPy arrays.

Output:
- xoutS_all (np.ndarray): The species concentrations at each timepoint
- tout_all (np.ndarray): The timepoints at which the species concentrations \
    were recorded
- xoutG_all (np.ndarray): The gene expression values at each timepoint

"""

# -----------------------Package Import & Defined Arguements-------------------#
import os
import sys
import math
import libsbml
import importlib
import numpy as np
import pandas as pd
import mpi4py

from src.validation.simulation.utils import Utils as utils
from src.utils.combine_results import combine_results
from src.simulation.RunSPARCED import RunSPARCED, RunAMICI

class Simulator:
    def __init__(
        self,
        yaml_file: str,
        conditions_df: pd.DataFrame,
        measurement_df: pd.DataFrame,
        parameters_df: pd.DataFrame,
        sbml_file: str,
        f_omics: pd.DataFrame,
        f_genereg: pd.DataFrame
    ):
        """This class is designed to simulate the experimental replicate model.
        input:
            yaml_file: str - path to the YAML file
            model: str - path to the SBML model
            conditions_df: pd.DataFrame - the conditions dataframe
            measurement_df: pd.DataFrame - the measurement dataframe
            parameters_df: pd.DataFrame - the parameters dataframe
            sbml_file: str - path to the SBML file
        """

        self.yaml_file = yaml_file
        self.conditions_df = conditions_df
        self.measurement_df = measurement_df
        self.parameters_df = parameters_df
        self.sbml_file = sbml_file
        self.f_omics = f_omics
        self.f_genereg = f_genereg

        # Load the SPARCED model
        self.model = self.load_sparced_model()

    def run(self, condition: pd.Series) -> tuple:
        """
        This function A). runs a decision based on if gene regulation
        and omics data are present in the model, and B). runs the simulation
        for each condition in the conditions dataframe.

        Parameters:
            self (Simulation): The Simulation class
            condition (pd.Series): The condition to simulate

        Returns:
            results (tuple): A tuple of the simulation results
        """
        if self.f_genereg is not None and self.f_omics is not None:
            results = self.run_sparced_simulation(condition)

        else:
            results = self.run_amici_simulation(condition)

        return results


    def run_sparced_simulation(self, condition: pd.Series) -> np.ndarray:
        """This function runs the simulation for a single condition.
        Parameters:
            self: Simulation - the Simulation class
            condition: pd.Series - the condition to simulate

        Returns:
            result: pd.DataFrame - the simulation results
        """
        # Look for heterogenize parameters in the condition
        if "heterogenize" in condition and not math.isnan(condition["heterogenize"]):
            self.model = self.heterogenize(condition)

        if "preequilibrationConditionId" in condition and not math.isnan(
            condition["preequilibrationConditionId"]
        ):
            self.model.preequilibrate(condition)

        # # Set the perturbations for the simulation
        self.model, self.f_omics = self.set_perturbations(condition)

        # Set the timepoints for the simulation
        simulation_timeframe = self.measurement_df["time"][
            self.measurement_df["simulationConditionId"].isin(condition)
        ].max()

        self.model.setTimepoints(np.linspace(0, 30))

        # Find gene sampling method, flagD
        perturbations = list(self.conditions_df.columns[2:])
        if "flagD" in perturbations:
            flagD = condition["flagD"]
        else:
            flagD = 1

        # Run the simulation
        xoutS_all, xoutG_all, tout_all = RunSPARCED(
            flagD=flagD,
            th=(simulation_timeframe / 3600),
            spdata=[],
            genedata=[],
            sbml_file=self.sbml_file,
            model=self.model,
            f_genereg=self.f_genereg,
            f_omics=self.f_omics,
        )

        results = combine_results(self.model, xoutS_all, xoutG_all, tout_all)

        return results
    

    def run_amici_simulation(self, condition: pd.Series) -> tuple:
        """This function runs the AMICI simulation for a single condition.
        Parameters:
            self: Simulation - the Simulation class
            condition: pd.Series - the condition to simulate

        Returns:
            result: tuple - the simulation results

        """
                # Set the timepoints for the simulation
        simulation_timeframe = self.measurement_df["time"][
            self.measurement_df["simulationConditionId"].isin(condition)
        ].max()

        # Set the perturbations for the simulation
        self.model, _ = self.set_perturbations(condition)

        xoutS_all, tout_all = RunAMICI(simulation_timeframe, self.model)

        results = combine_results(self.model, xoutS_all, None, tout_all)

        return results


    def preequilibrate(self, condition: pd.Series) -> pd.DataFrame:
        """This function assigns a set of conditions that replicate
        prior experimental conditions before the primary stimulus of
        interest.

        input:
            condition: pd.Series - the condition to simulate

        output:
            preequilibrated_model: pd.DataFrame - the preequilibrated model
        """

        # Isolate the preequilibration condition if included in the measurement
        # table
        preequilibrate_condition = (
            self.measurement_df.loc[
                self.measurement_df["simulationConditionId"]
                == condition["conditionId"],
                "preequilibrationConditionId",
            ]
            .dropna()
            .unique()
        )

        # account for no preequilibration condition being found
        if len(preequilibrate_condition) == 0:
            return self.model

        # set perturbations for the simulation
        self.model, self.f_omics = self.set_perturbations(condition)

        # Find gene sampling method, flagD
        flagD = self.conditions_df.loc[
            self.conditions_df["conditionId"] == preequilibrate_condition[0], "flagD"
        ].values[0]

        # Find the time frame for the preequilibration simulation
        simulation_timeframe = self.measurement_df["time"][
            self.measurement_df["preequilibrationConditionId"].isin(condition)
        ].max()

        species_initializations = np.array(self.model.getInitialStates())

        self.model.setTimepoints(np.linspace(0, 30))

        # Run the simulation
        xoutS_all, _, _ = RunSPARCED(
            flagD,
            simulation_timeframe,
            species_initializations,
            [],
            self.sbml_file,
            model=self.model,
            f_genereg=self.f_genereg,
            f_omics=self.f_omics,
        )

        # Return the final values
        self.model.setInitialStates(xoutS_all[-1])

        return self.model

    def set_perturbations(self, condition: pd.Series) -> libsbml.Model:
        """This function sets the perturbations for the simulation.
        input:
            condition: pd.Series - the condition to simulate
        output:
            model: libsbml.Model - the updated SBML model
        """

        perturbations = list(self.conditions_df.columns[2:])

        for perturbant in perturbations:
            try:
                self.model = utils._set_species_value(
                    self.model, perturbant, condition[perturbant]
                )
                break
            except:
                pass

            try:
                self.model = utils._set_parameter_value(
                    self.model, perturbant, condition[perturbant]
                )
                break
            except:
                pass

            try:
                self.model = utils._set_compartmental_volume(
                    self.model, perturbant, condition[perturbant]
                )
                break
            except:
                pass

            try:
                # Change the OmicsData values and save the prior values
                self.f_omics = utils._set_transcription_values(
                    omics_data=self.f_omics,
                    gene=perturbant,
                    value=condition[perturbant],
                )
                break
            except:
                pass
                
        return self.model, self.f_omics

    def heterogenize(self, condition: pd.Series) -> libsbml.Model:
        """This function runs the 'runSPARCED function and returns the final
        values, thus creating the simulated appearance of asynchrony among
        replicates.
        input:
            condition: pd.Series - the condition to simulate
        output:
            heterogenized_initial_values: pd.DataFrame - the heterogenized
            initial values
        """

        heterogenize = condition["heterogenize"]

        simulation_time = int(heterogenize) / 3600

        self.model.setTimepoints(np.linspace(0, 30))

        # TODO: Find a better mechanism for setting signaling ligands to 0
        growth_factors = ["E", "H", "HGF", "P", "F", "I", "INS"]

        for species in growth_factors:
            self.model = utils._set_species_value(self.model, species, 0)

        xoutS_all, _, _ = RunSPARCED(
            flagD=0,
            th=simulation_time,
            spdata=[],
            genedata=[],
            sbml_file=self.sbml_file,
            model=self.model,
            f_genereg=self.f_genereg,
            f_omics=self.f_omics,
        )

        self.model.setInitialStates(xoutS_all[-1])

        return self.model


    def load_sparced_model(self):
        """
        This function loads the SPARCED model.

        Parameters:
            None

        Returns:
        - model (libsbml.Model): The SBML model
        """
        # Create an instance of the AMICI model.
        sys.path.append(self.sbml_file)

        # try:
        utils._add_amici_path(self.sbml_file)

        sparced = utils._swig_interface_path(self.sbml_file)
        sys.path.append(sparced)
        SPARCED = importlib.import_module(sparced.split("/")[-1].split(".")[0])
        model = SPARCED.getModel()
        solver = model.getSolver()
        solver.setMaxSteps = 1e10

        return model
