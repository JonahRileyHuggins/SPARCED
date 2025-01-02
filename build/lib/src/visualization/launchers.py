#!/bin/bash python3
# -*- coding: utf-8 -*-
"""
script name: launchers.py
Created on Fri Dec. 3rd 23:32:00 2024
Author: Jonah R. Huggins

Description: House the main functions for launching the visualization functionality 
of the SPARCED model. This functionality will have 2 primary flags for operation:
    1. `--yaml_path`: The path to the yaml file containing the visualization PEtab file
    2. `--from_script`: A flag to indicate that the visualization is being run from a custom script
    rather than from a PEtab visualization file. 

Output: The output of this script will be the visualization of the PEtab file in the yaml file.
"""

# Import necessary libraries
import os
import sys
import json
from datetime import datetime
import pandas as pd

from src.utils.arguments import parse_args
from src.utils.petab_file_loader import PEtabFileLoader as pfl
from src.visualization.visualizer import Visualizer

args = parse_args()

def launch_visualizer() -> None:
    """
    Recieves arguements from the CLI `sparced visualize` command and runs the
    appropriate visualization script / file.

    """
    if args.from_script:
        run_custom_script(args.input_data, args.from_script, args.output, args.name)
    else:
        run_visualizer(args.input_data, args.yaml, args.output, args.name)


def run_visualizer(input_data: os.PathLike | str, yaml_path: os.PathLike | str,
                   output_path: os.PathLike | str, file_name: str = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
                   ) -> None:
    """
    Takes a dataset and a PEtab-compliant yaml file and generates a visualization plot.

    Parameters:
    - input_data (str): path to the data file
    - yaml_path (str): path to the yaml file
    - output_path (str): path to the output file
    - file_name (str): name of the output file

    Returns:
    - None
    """
    petab_files = pfl(yaml_path)

    results_dictionary = load_data(input_data)

    if petab_files.visualization_df is not None:

        print("Generating visualization plot...")

        fig = Visualizer(
            petab_files=petab_files,
            results_dict=results_dictionary,
        ).dynamic_plot()

        name = file_name if file_name is not None else datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        fig.savefig(os.path.join(output_path, f"{name}.png"))


def run_custom_script(input_data: os.PathLike | str = None, from_script: os.PathLike | str = None, 
                      output_path: os.PathLike | str = None, file_name: str = None, 
                      catchall: str = None) -> None:
    """
    Run the visualization script from a custom script with optional arguments.
    
    Parameters:
    - input_data (str, optional): Path to the input data file.
    - from_script (str, optional): Path to the custom script to execute. (Required)
    - output_path (str, optional): Path to the output directory.
    - file_name (str, optional): Name for the output file.
    - catchall (str, optional): Additional custom arguments as a JSON string.
    """
    print("Running visualization script from a custom script.")
    
    # Ensure from_script is provided
    if not from_script:
        print("Error: A path to the custom script must be provided using the --from_script flag.")
        sys.exit(1)
    
    # Initialize execution context
    exec_context = {}

    # Load data if provided
    if input_data:
        try:
            results_dictionary = load_data(input_data)
            exec_context["results_dictionary"] = results_dictionary
        except Exception as e:
            print(f"Error loading data: {e}")
            sys.exit(1)
    else:
        print("Warning: No input data provided.")

    # Add optional arguments to the execution context
    if output_path:
        exec_context["output_path"] = output_path
    if file_name:
        exec_context["file_name"] = file_name
    else:
        exec_context["file_name"] = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    
    # Parse catchall arguments
    if catchall:
        try:
            additional_args = json.loads(catchall)
            exec_context.update(additional_args)
        except json.JSONDecodeError:
            print("Error: Catchall arguments must be a valid JSON string.")
            sys.exit(1)
    
    # Run the custom script
    try:
        with open(from_script, encoding="utf-8") as script:
            exec(script.read(), exec_context)
    except Exception as e:
        print(f"Error executing script: {e}")
        sys.exit(1)
    
    print("Visualization script complete.")


def load_data(input_data: os.PathLike | str) -> dict:
    """
    Load the data from the input data file. This function is to add a clean space
    for error handling of the data.
    """
    try:
        results_dictionary = pd.read_pickle(input_data)

    except FileNotFoundError:
        print(f"Error: The file {input_data} does not exist. Please check the path and try again.")
        sys.exit(1)

    return results_dictionary
