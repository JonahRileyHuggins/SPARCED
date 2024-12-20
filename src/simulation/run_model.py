#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import importlib
import numpy as np
import pandas as pd

from simulation.modules.RunSPARCED import RunSPARCED, RunAMICI
from simulation.utils.initial_conditions import *
from simulation.utils.output import save_simulation_output


def run_experiment(model_name: str, simulation_name: str,
                   output_sim: str | os.PathLike, model_path: str | os.PathLike,
                   sbml_model: str | os.PathLike,
                   input_files: dict[str, str | os.PathLike],
                   is_deterministic: bool, popsize: int, duration: float,
                   exchange: int, verbose: bool, is_SPARCED: bool,
                   perturbations: np.ndarray=None,
                   incubation_conditions: np.ndarray=None,
                   incubation_duration: float=None) -> None:
    """Run an experiment

    Run an experiment consisting of one or several cells within the same
    initial conditions.

    Arguments:
        model_name: The name of the model.
        simulation_name: The desired name for the simulation results.
        output_sim: The path where to store the results.
        model_path: The path to the AMICI model folder.
        sbml_model: The path to the SBML model.
        input_files: A dictionnary containing simualation input files paths.
        is_deterministic: Run on deterministic mode.
        popsize: The cell population size in the experiment.
        duration: The duration of the experiment.
        exchange: The timeframe between module information exchange.
        verbose: Verbose.
        is_SPARCED: Use SPARCED hard-coded values/behaviors.
        perturbations: An array containing changes to make to initial conditions.

    Return:
        Nothing.
    """
    # Load model
    sys.path.insert(0, os.path.abspath(model_path)) # TODO: fix the import on the next line to avoid messing up with paths
    model_module = importlib.import_module(model_name)
    model = model_module.getModel()
    if verbose:
        print("{model_name}: Successfully loaded {module}\n"
               .format(model_name=model_name, module=model_module)) 
    # Set time points
    if incubation_duration == None:
        incubation_duration = 0.0
    model.setTimepoints(np.linspace(0, exchange, 2))
    # Compute initial conditions
    if incubation_duration > 0.0:
        species_initial_conditions, species_names = load_species_initial_conditions(sbml_model, incubation_conditions)
    else:
        species_initial_conditions = load_species_initial_conditions(sbml_model, perturbations)[0]
    # Run experiment
    cell_number = 0
    while cell_number < int(popsize):
        if incubation_duration > 0.0:
            xoutS_incub = run_single_simulation(model, simulation_name + "_incub",
                          output_sim, cell_number, sbml_model, is_deterministic,
                          exchange, incubation_duration,
                          species_initial_conditions, verbose,
                          input_files["genereg"], input_files["omics"])
            for specie in range(len(species_initial_conditions)):
                species_initial_conditions[specie] = xoutS_incub[-1:,specie]
            apply_perturbations(species_initial_conditions, species_names,
                                perturbations)
        run_single_simulation(model, simulation_name, output_sim, cell_number, sbml_model,
                              is_deterministic, exchange, duration,
                              species_initial_conditions, verbose,
                              input_files["genereg"], input_files["omics"])
        cell_number += 1

def run_single_simulation(model, simulation_name: str, output_sim: str, simulation_number: int,
                          sbml_model: str, is_deterministic: bool,
                          exchange: int, duration: float,
                          species_initial_conditions: np.ndarray,
                          verbose: bool, f_genereg: str, f_omics: str) -> None:
    """
    Run a single simulation of SPARCED
    """
    # Set initial conditions
    model.setInitialStates(species_initial_conditions)
    if verbose:
        print("{name} n°{number}: Now ready to run\n"
              .format(name=simulation_name, number=simulation_number))
        
    
    # convert f_genereg and f_omics to pandas dataframes
    if f_genereg is not None and f_omics is not None:
        f_genereg = pd.read_csv(f_genereg, header=0, index_col=0, sep="\t")
        f_omics = pd.read_csv(f_omics, header=0, index_col=0, sep="\t")

        # Run the simulation
        xoutS_all, xoutG_all, tout_all = RunSPARCED(is_deterministic, float(duration),
                                                    species_initial_conditions, [],
                                                    sbml_model, model, f_genereg, f_omics)

    else:
        # Run the simulation
        xoutS_all, tout_all = RunAMICI(float(duration), model)

        xoutG_all = None 
    if verbose:
        print("{name} n°{number}: Simulation is over. Now saving results, \
                please do not exit.\n".format(name=simulation_name,
                                              number=simulation_number))
    # Save output
    save_simulation_output(model, simulation_name, simulation_number, output_sim,
                           xoutS_all, xoutG_all, tout_all)
    if verbose:
        print("{name} n°{number}: Simulation saved.\n"
              .format(name=simulation_name, number=simulation_number))
    return(xoutS_all)

