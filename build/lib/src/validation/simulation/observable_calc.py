#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
script name: Observable_calc.py
Created on Fri April 24 18:00:00 2024
Author: Jonah R. Huggins

Description: This script is designed to calculate observable values from 
             simulation results.

Output: dictionary containing the observables of interest

"""
# -----------------------Package Import & Defined Arguements-------------------#
import re
import numpy as np
from typing import List
import pandas as pd
#-------------------------Initialization & Variables---------------------------#
class ObservableCalculator:
    """This class is designed to calculate observable values from simulation results."""

    def __init__(self, parent):
        """This class is designed to calculate observable values from \
            simulation results.
            
        input:
            yaml_file: str - path to the YAML file
            results_dict: dict - dictionary containing the simulation results
            observable_df: str - path to the observable dataframe
            model: libSBML model - the model used for the simulation
        """
        self.yaml_file = parent.yaml_file
        self.results_dict = parent.results_dictionary
        self.observable_df = parent.observable_df
        self.measurement_df = parent.measurement_df

    def run(self):
        """isolate only the observables of interest from the simulation data. \
        Primary function is to cut down on data saved.

        Returns: modified results dictionary containing only the observables of 
        interest
        """
        observableIds = self.observable_df["observableId"].unique()

        # Stores the calculated observable values for each observable and condition
        observable_dict = {}

        for entry in self.results_dict:

            observable_dict[entry] = {
                "conditionId": self.results_dict[entry]["conditionId"],
                "cell": self.results_dict[entry]["cell"]
            }

            for observableId in observableIds:

                # calculate the observable values from the simulation results
                observable_array = self.observable_caluculator(
                    observableId, entry
                )

                # add any potential experimental data to the observable_dict
                experimental_data = self.extract_experimental_data(
                    observableId, self.results_dict[entry]["conditionId"]
                )

                # add the observable to the observable_arrays dictionary
                observable_dict[entry][f"simulation {observableId}"] = observable_array

                observable_dict[entry][f"experiment {observableId}"] = experimental_data

            # reduce timepoints in the simulation to only experimental match
            observable_dict[entry]["time"] = self.timepoint_reduction(
                self.results_dict[entry]["time"]
                )

        return observable_dict


    def observable_caluculator(
        self, observable: str, entry: str
    ) -> np.array:
        """Calculate the observable values from the simulation results.

        Parameters:
        - observable (str): The observable of interest. Should be a column in \
            the observable dataframe.
        - entry (str): String of the identifier for a particular simulation \
            result for a single condition.

        Returns:
        - observable_array(np.array): Array containing the observable values.
        """
        try:
            assert (
                observable in self.observable_df["observableId"].values,
                f"{observable} is not in the observable dataframe",
            )

            # replace species name strings in the observable_formula with the
            # corresponding species index in the results_dict
            observable_formula = self.observable_df["observableFormula"][
                self.observable_df["observableId"] == observable
            ]

            observable_formula = observable_formula.iloc[0]

            # Search the observable formula for species names
            species = get_valid_species(observable_formula)

            for species_i in species:

                observable_formula = self.swap_species_for_array(
                    entry, species_i, observable_formula
                )

            observable_answer = eval(observable_formula)

            time = self.results_dict[entry]["time"]

            observable_answer = self.data_reduction(observable_answer, time)

            return observable_answer

        except AssertionError as e:
            print(e)
            pass


    def timepoint_reduction(self, time: np.array) -> np.array:
        """Reduce the number of timepoints in the simulation results. to match
            the number of timepoints in the experimental data.

        Parameters:
        - toutS (np.array): The timepoints from the simulation results.

        Returns:
        - toutS (np.array): The reduced timepoints.
        """
        # Ensure experimental values in the measurement
        # before reducing the timepoints, if none are found, return the original
        if self.measurement_df["measurement"].isna().all():
            return time

        unique_timepoints = self.measurement_df["time"].unique()

        reduced_toutS = []

        for t in unique_timepoints:
            closest_idx = np.argmin(np.abs(time - t))
            reduced_toutS.append(time[closest_idx])

        # Convert to np.array and remove duplicates if any
        return np.unique(np.array(reduced_toutS))


    def data_reduction(self, observable_answer: np.array, time: np.array) -> np.array:
        """Reduce the data to only the timepoints in the experimental data.

        Parameters:
        - observable_answer (np.array): The observable values from the simulation.
        - time (np.array): Array of timepoints recorded during the simulation.

        Returns:
        - observable_answer (np.array): The reduced observable values.
        """
        # Ensure first that there is no experimental values in the measurement
        # before reducing the timepoints, if none are found, return the original
        if self.measurement_df["measurement"].isna().all():
            return observable_answer

        # Find the minimum number of timepoints in the measurement data
        min_timepoint_idx = self.timepoint_reduction(time)

        # Now find the indices of the filtered_toutS in toutS (if needed)
        timepoint_indices = np.where(np.isin(time, min_timepoint_idx))

        # Reduce the observable_answer to only the timepoints in the experimental data
        observable_answer = observable_answer[timepoint_indices]

        return observable_answer


    def swap_species_for_array(self, dict_entry: str, species_i: str, 
                            observable_formula: str) -> str:
        """
        Takes a species identifier and returns the corresponding array from the results_dict.

        Parameters:
        - dict_entry (str): The identifier for a particular simulation result for a single condition.
        - species_i (str): The species identifier.
        - observable_formula (str): The formula containing species and mathematical expressions.

        Returns:
        - observable_formula (str): The observable formula with the species replaced by the array.

        Raises:
        - KeyError: If the species identifier is not found in the results dictionary.
        - ValueError: If the replacement value cannot be converted to a NumPy array.
        """
        try:
            # Validate inputs
            if not isinstance(dict_entry, str):
                raise TypeError("The dict_entry must be a string.")
            if not isinstance(species_i, str):
                raise TypeError("The species_i must be a string.")
            if not isinstance(observable_formula, str):
                raise TypeError("The observable_formula must be a string.")

            # Retrieve the replacement value from the results dictionary
            replacement_value = self.results_dict.get(dict_entry, {}).get(species_i)

            if replacement_value is None:
                raise KeyError(f"Species '{species_i}' not found in results_dict for entry '{dict_entry}'.")

            # Convert to NumPy array
            if isinstance(replacement_value, pd.Series):
                replacement_value = replacement_value.to_numpy()
            elif not isinstance(replacement_value, np.ndarray):
                raise ValueError(f"Replacement value for species '{species_i}' is not a valid array or Series.")

            # Prepare replacement string
            replacement_value_str = f"np.array({replacement_value.tolist()})"

            # Replace only exact matches of the species name in the formula
            observable_formula = re.sub(fr"\b{re.escape(species_i)}\b",
                                        replacement_value_str,
                                        observable_formula)

            return observable_formula

        except Exception as e:
            print(f"Error in swap_species_for_array: {e}")
            raise


    def extract_experimental_data(self, observableId: str, conditionId: str):
        """
        Extract experimental data for a given observable and condition from the measurement dataframe.

        Parameters:
        - observableId (str): The observable identifier.
        - conditionId (str): The condition identifier.

        Returns:
        - np.array: The experimental data for the given observable and condition.
        """
        try:
            # Filter the measurement dataframe for the given observable and condition
            filtered_df = self.measurement_df[
                (self.measurement_df["observableId"] == observableId) &
                (self.measurement_df["simulationConditionId"] == conditionId)
            ].dropna(subset=["measurement"]).sort_values("time")

                # Extract the experimental data
            if filtered_df.empty:
                print(f"No experimental data found for observableId '{observableId}'"\
                      f" and conditionId '{conditionId}'.")
                return np.array([])

            # Extract the experimental data
            experimental_data = filtered_df["measurement"].to_numpy()

            return experimental_data

        except Exception as e:
            print(f"Error in extract_experimental_data: {e}")
            return np.array([])


def get_valid_species(observable_formula: str) -> List[str]:
    """
    Extract valid species identifiers from an observable formula based on PEtab naming conventions.

    Parameters:
    - observable_formula (str): The formula containing species and mathematical expressions.

    Returns:
    - List[str]: A list of valid species identifiers.

    Raises:
    - ValueError: If no valid species are found in the observable formula.
    """
    try:
        if not isinstance(observable_formula, str):
            raise TypeError("Input observable_formula must be a string.")

        # Regex for PEtab-compliant species identifiers
        petab_species_regex = r"[a-zA-Z_][a-zA-Z_\d]*"

        # Split the formula by mathematical operators and filter valid species
        components = re.split(r"[+\-*/() ]", observable_formula)
        valid_species = [c for c in components if re.match(petab_species_regex, c)]

        if not valid_species:
            raise ValueError("No valid species found in the observable formula.")

        return valid_species

    except Exception as e:
        print(f"Error in get_valid_species: {e}")
        return []


