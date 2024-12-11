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

                # add the observable to the observable_arrays dictionary
                observable_dict[entry][f"simulation {observableId}"] = observable_array

            # reduce timepoints in the simulation to only experimental match
            observable_dict[entry]["time"] = self._timepoint_reduction(
                self.results_dict[entry]["time"]
                )

            # add the observable values to the results_dict if the
            # observable is associated with the conditionId in the measurement_df
            grouped_identifiers = self.measurement_df.groupby(
                ["simulationConditionId", "observableId"]
            )

            for (cond_id, obs_id), group in grouped_identifiers:
                if cond_id == self.results_dict[entry]["conditionId"]:
                    observable_dict[entry][f"experiment {obs_id}"] = (
                        self._add_experimental_data(cond_id, obs_id)
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
            species = re.findall(
                r"\b[A-Za-z](?:[A-Za-z0-9_]*[A-Za-z0-9])?\b", observable_formula
            )

            for species_i in species:

                # Construct the regex pattern to match the species name exactly
                pattern = r"{}".format(re.escape(species_i))
                replacement_value = self.results_dict[entry].get(species_i)
                replacement_value = replacement_value.to_numpy()
                replacement_value_str = f"np.array({replacement_value.tolist()})"

                # Replace only the exact matches of the species name in the formula
                observable_formula = re.sub(pattern,
                                            replacement_value_str,
                                            observable_formula
                                            )

            observable_answer = eval(observable_formula)

            time = self.results_dict[entry]["time"]

            observable_answer = self.data_reduction(observable_answer, time)

            return observable_answer

        except AssertionError as e:
            print(e)
            pass


    def _add_experimental_data(self, conditionId: str, observableId: str) -> np.array:
        """
        Returns a dictionary of experimental data for each observable and condition,
        matching simulation results dictionary format.

        Parameters:
        - entry str: String of the identifier for a particular simulation \
                     result for a single condition.

        Returns:
        - entry (tuple): Modified results_dict entry containing the simulation \
                         results and experimental data.
        """

        if "preequilibrationConditionId" in self.measurement_df.columns:

            # Account for the preequilibration condition
            preequilibration_condition = self.measurement_df.loc[
                self.measurement_df["simulationConditionId"]
                == self.measurement_df["preequilibrationConditionId"]
            ]

            if not preequilibration_condition.empty:
                non_preequilibration_df = self.measurement_df.drop(
                    preequilibration_condition.index
                )

            else:
                non_preequilibration_df = self.measurement_df

        else:
            non_preequilibration_df = self.measurement_df

        # look for experimental data in the measurements file by exculding all
        #  NaN values in measurement_df['measurement']
        if self.measurement_df["measurement"].isna().all():
            print("No experimental data to compare to")
            return self.results_dict

        # match the experimental data to the simulation results
        measurements = self.measurement_df["measurement"][
            (self.measurement_df["simulationConditionId"] == conditionId)
            & (self.measurement_df["observableId"] == observableId)
        ]

        return np.array(measurements)


    def _timepoint_reduction(self, time: np.array) -> np.array:
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
        min_timepoint_idx = self._timepoint_reduction(time)

        # Now find the indices of the filtered_toutS in toutS (if needed)
        timepoint_indices = np.where(np.isin(time, min_timepoint_idx))

        # Reduce the observable_answer to only the timepoints in the experimental data
        observable_answer = observable_answer[timepoint_indices]

        return observable_answer
