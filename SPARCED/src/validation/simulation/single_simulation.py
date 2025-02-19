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
import sys
import math
import libsbml
import importlib
import numpy as np
import pandas as pd

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
        """
        This class is designed to simulate the experimental replicate model.
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

    def run(self, condition: pd.Series) -> pd.DataFrame:
        """
        This function A). runs a decision based on if gene regulation
        and omics data are present in the model, and B). runs the simulation
        for each condition in the conditions dataframe.

        Parameters:
            self (Simulation): The Simulation class
            condition (pd.Series): The condition to simulate

        Returns:
            results (pd.DataFrame): dataframe of simulation results
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

        flagD = self.determine_hybrid_flag(condition)

        # Look for heterogenize parameters in the condition
        self.model = self.heterogenize(condition)

        # Look for preequilibration parameters in the condition
        self.model = self.preequilibrate(condition, flagD)

        # # Set the perturbations for the simulation
        self.model, self.f_omics = self.set_perturbations(condition)

        # Set the timepoints for the simulation
        simulation_timeframe = self.measurement_df["time"][
            self.measurement_df["simulationConditionId"].isin(condition)
        ].max()

        self.model.setTimepoints(np.linspace(0, 30))


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

    def preequilibrate(self, condition: pd.Series, flagD: bool) -> pd.DataFrame:
        """
        This function assigns a set of conditions that replicate
        prior experimental conditions before the primary stimulus of
        interest.

        Parameters:
        - condition (pd.Series): the condition to simulate
        - flagD (bool): the flag for if the simulation is deterministic or stochastic

        Returns:
        - preequilibrated_model (pd.DataFrame) the preequilibrated model
            OR 
        - model (pd.DataFrame): the model, sans preequilibration condition
        """
        # Isolate the preequilibration condition if included in the measurement
        # table
        if "preequilibrationConditionId" not in self.measurement_df.columns:
            return self.model
        
        preequilibrate_condition_id = (
            self.measurement_df.loc[
                self.measurement_df["simulationConditionId"]
                == condition["conditionId"],
                "preequilibrationConditionId",
            ]
            .dropna()
            .unique()
        )

        # account for no preequilibration condition being found
        if len(preequilibrate_condition_id) == 0:
            return self.model

        parent_condition = condition

        condition = self.conditions_df.loc[
            self.conditions_df["conditionId"] == preequilibrate_condition_id[0]
        ]

        # set perturbations for the simulation
        self.model, self.f_omics = self.set_perturbations(condition)

        # Find the time frame for the preequilibration simulation
        simulation_timeframe = self.measurement_df["time"][
            self.measurement_df["simulationConditionId"] == preequilibrate_condition_id[0]
        ].max()

        print_statement = (f"Running parent condition {parent_condition['conditionId']}",
                           f"preequilibration {preequilibrate_condition_id[0]}",
                           f"for {simulation_timeframe} seconds.")
        print(*print_statement)

        species_initializations = np.array(self.model.getInitialStates())

        self.model.setTimepoints(np.linspace(0, 30))

        # Run the simulation
        xoutS_all, _, _ = RunSPARCED(
            flagD=flagD,
            th=(simulation_timeframe / 3600),
            spdata=species_initializations,
            genedata=[],
            sbml_file=self.sbml_file,
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
                self.model = utils.set_species_value(
                    self.model, perturbant, condition[perturbant]
                )
                break
            except:
                pass

            try:
                self.model = utils.set_parameter_value(
                    self.model, perturbant, condition[perturbant]
                )
                break
            except:
                pass

            try:
                self.model = utils.set_compartmental_volume(
                    self.model, perturbant, condition[perturbant]
                )
                break
            except:
                pass

            try:
                self.f_omics = utils.set_transcription_values(
                    omics_data=self.f_omics,
                    gene=perturbant,
                    value=condition[perturbant],
                )
                break
            except:
                pass
                
        return self.model, self.f_omics
        
    def heterogenize(self, condition: pd.Series) -> libsbml.Model:
        """
        Runs the 'runSPARCED' function to simulate asynchrony among replicates.

        Parameters:
        - condition (pd.Series): the condition to simulate

        Returns:
        - model (libsbml.Model): the updated SBML model with stochastic heterogenization
        - model (libsbml.Model): the original SBML model if no heterogenization is required
        """

        heterogenize = condition.get("heterogenize_time", None)

        if heterogenize is None or isinstance(heterogenize, str) or (isinstance(heterogenize, float) and math.isnan(heterogenize)):
            return self.model  # Return original model if no heterogenization is required

        simulation_time = int(heterogenize) / 3600
        self.model.setTimepoints(np.linspace(0, 30))

        # TODO: Improve mechanism for setting signaling ligands to 0
        growth_factors = ["E", "H", "HGF", "P", "F", "I", "INS"]

        for species in growth_factors:
            self.model = utils.set_species_value(self.model, species, 0)  # Set growth factors to 0

        xoutS_all, _, _ = RunSPARCED(
            flagD=0,  # Use stochastic solver for heterogenization
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

        utils.add_amici_path(self.sbml_file)

        sparced = utils.swig_interface_path(self.sbml_file)
        sys.path.append(sparced)
        SPARCED = importlib.import_module(sparced.split("/")[-1].split(".")[0])
        model = SPARCED.getModel()
        solver = model.getSolver()
        solver.setMaxSteps = 1e10

        return model

    @staticmethod
    def determine_hybrid_flag(condition: pd.Series) -> int:
        """
        Determines if hybrid is an included flag within the individual perturbation, 
        and if so, sets the model solver accordingly. 

        Parameters:
        - condition (pd.Series): key-value pair structure of perturbation identifiers
                                     (assigned following PEtab conditions table standard)
                                    matched to associated values. 

        Returns:
        - flagD (int): Deterministic decision flag for if the SPARCED model will solve 
                       the system deterministically, or use the integrated hybrid simulation 
                       setting, enabling stochastic trajectories.
        """

        if "hybrid" in condition.keys():
            if condition["hybrid"]:  # If hybrid is True
                flagD = 0
            
            else:
                flagD = 1

        else:
            flagD = 1

        return flagD