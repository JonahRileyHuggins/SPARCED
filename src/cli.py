#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun. 17/11/2024 00:18AM - JRH

Description: This script is the main method for constructing an AMICI model
using SPARCED input files. The first step is to build the model. Note that
building the model may take several minutes. There are 3 main utilities described here:
1. Model Compilation
2. Experiment Simulation
3. Benchmarking

The script is executed by running the following command in the terminal:
    $ SPARCED compile
    $ SPARCED simulate
    $ SPARCED benchmark
    $ SPARCED -h
"""

#-----------------------Package Import & Defined Arguements--------------------# 
from utils.arguments import parse_args

def compile_model(args):
    """Handle the compile subcommand. This script is the method for constructing an \
    AMICI model using SPARCED input files."""
    print(f"Compiling model: {args.name}")
    print(f"Input data: {args.input_data}")
    print(f"Output parameters file: {args.output_parameters}")
    from compilation.launcher import launch_model_creation
    launch_model_creation() # Process parsed arguments and launch model creation

def simulate_model(args):
    """ Handle the simulate subcommand.
    Run a simulation. Here, you can run an experiment, i.e. one or several cell simulations \
    within the given initial conditions. Executes the simulation of an AMICI model,\
    compiled either using the SPARCED input files or SBML file.
    """
    print(f"Simulating model: {args.name}")
    print(f"Population size: {args.population_size}")
    print(f"Simulation time: {args.time} hours")
    print(f"Results directory: {args.results}")

    from simulation.launchers import launch_experiment_simulation
    launch_experiment_simulation() # Process parsed arguments and launch simulation

def benchmark_model(args):
    """Handle the benchmark subcommand. Script to automate model-data comparisons, \
    'benchmarks'. 
"""
    print(f"Benchmarking results directory: {args.results}")
    from validation.simulation.run_benchmark import RunBenchmark
    rb = RunBenchmark()
    rb.run()
    rb.observable_calculation()
    rb.run_visualizer()
    rb.return_sedml()



def main():
    """Main entry point."""
    args = parse_args()

    if args.command == "compile":
        compile_model(args)
    elif args.command == "simulate":
        simulate_model(args)
    elif args.command == "validate":
        benchmark_model(args)
    else:
        print("No valid command provided. Use --help for guidance.")

if __name__ == "__main__":
    main()
