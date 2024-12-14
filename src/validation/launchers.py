# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Created on Thurs. 05/16/2024 10:45:00 - JRH

Script to automate model-benchmark comparison to prior validated results of
the SPARCED model.

Provide a path to the model directory and the script will run all benchmarks, 
outputing visual results to a 'results' directory within the model directory 
for anlysis. 

Users are anticipated to compare simulation results to prior validated results.
"""

# -----------------------Package Import & Defined Arguements-------------------#
import os
from utils.arguments import parse_args
from typing import List
from validation.simulation.run_benchmark import RunBenchmark
import mpi4py.MPI as MPI

# Parse the arguements
args = parse_args()

# Load the MPI communicator
communicator = MPI.COMM_WORLD
rank = communicator.Get_rank()

# -----------------------Function to Run All Benchmarks-------------------------#
def launch_validation() -> None:
    """
    determine the benchmarks to run and run them
    Input:
        - args.input_data: the path to the directory containing the benchmarks
        - args.cores: the number of cores to use for the simulation
        - args.benchmark: the name of the benchmark to run
        - args.run_all: a flag to run all benchmarks

    Output:
        simulation results for all benchmarks to a 'results' directory
        within the model directory
    """
    if args.run_all is not None:
        assert args.run_all is not None, "Error: No benchmark provided, \
            either provide a benchmark or use the --run_all flag to run all benchmarks."
        run_all_benchmarks()
    else:
        assert args.benchmark is not None, "Error: No benchmark provided, \
            either provide a benchmark or use the --run_all flag to run all benchmarks."
        run_single_benchmark(args.benchmark)


def run_all_benchmarks() -> None:
    """
    Run all benchmarks in the provided directory.

    Args:
        None

    Returns:
        None
    """
    benchmarks = _get_list_of_benchmarks(args.run_all)

    for yaml_path in benchmarks:

        assert os.path.exists(yaml_path), f"Error: Benchmark {yaml_path} does not exist. check the benchmark\
                                             directory and try again."

        # Run the benchmark
        run_single_benchmark(yaml_path)


def run_single_benchmark(benchmark: str) -> None:
    """
    Run a single benchmark.

    Args:
        benchmark (str): The path to the benchmark YAML file.

    Returns:
        None
    """
    assert os.path.exists(benchmark), f"Error: Benchmark {benchmark} does not exist. check the benchmark\
                                       directory and try again."

    # Run the benchmark
    if rank == 0:
        print(f"Running benchmark {os.path.basename(benchmark)}")
    rb = RunBenchmark(benchmark)
    rb.run()
    rb.observable_calculation()
    rb.run_visualizer()
    rb.return_sedml()


def _get_list_of_benchmarks(directory: str) -> List[str]:
    """
    Recursively searches for YAML files in the provided directory and its subdirectories.

    Args:
        directory (str): The root directory to search.

    Returns:
        List[str]: A list of paths to the YAML files found.
    """
    yaml_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.yaml', '.yml')):
                yaml_files.append(os.path.join(root, file))

    return yaml_files



# -----------------------Run All Benchmarks------------------------------------#
if __name__ == "__main__":
    run_all_benchmarks()