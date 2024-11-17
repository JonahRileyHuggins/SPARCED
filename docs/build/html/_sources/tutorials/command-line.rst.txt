===============================================================================
Using the SPARCED Command Line Interface (CLI)
===============================================================================

The SPARCED package provides a convenient CLI tool to manage common tasks like 
compiling models, running simulations, benchmarking, and visualizing results.

This guide explains how to use the `sparced` CLI tool to streamline your workflows.

Getting Started
===============================================================================

Before using the CLI, ensure the following:

1. **SPARCED Installed as a CLI Tool**:
   The `sparced` CLI tool is installed and available in your environment. If not, 
   install it using pipx:
   ::
      pipx install <path_to_sparced_package>

2. **Verify Installation**:
   Run the following command to verify:
   ::
      sparced --help

   If installed correctly, this will display the help menu for the CLI.

Common Commands
===============================================================================

The `sparced` CLI supports several commands for different operations:

General Usage
-------------------------------------------------------------------------------
Use the following syntax:
::
   sparced <command> [options]

Example:
::
   sparced simulate --name SPARCED_standard --condition data/simulation/standard_GeneReg.txt

Available Commands
-------------------------------------------------------------------------------

1. **Compile Models**:
   Compile an Antimony or SBML model:
   ::
      sparced compile --input <model_file> --output <output_directory>

   - `--input`: Path to the Antimony or SBML model file.
   - `--output`: Directory to save the compiled model.

   Example:
   ::
      sparced compile --input models/SPARCED_standard.sbml --output compiled_models/

2. **Run Simulations**:
   Execute simulations using a specified model and condition file:
   ::
      sparced simulate --model <model_name> --condition <condition_file>

   - `--model`: Name of the model (e.g., `SPARCED_standard`).
   - `--condition`: Path to the condition file.

   Example:
   ::
      sparced simulate --name SPARCED_standard --condition data/simulation/standard_GeneReg.txt

3. **Generate Benchmarks**:
   Create a new benchmark YAML file:
   ::
      sparced generate-benchmark --name <benchmark_name> --output <output_file>

   - `--name`: Name of the benchmark.
   - `--output`: Path to save the benchmark file.

   Example:
   ::
      sparced generate-benchmark --name TRAIL-response --output benchmarks/TRAIL-response.yml

4. **Validate Benchmarks**:
   Compare a model's output to a benchmark:
   ::
      sparced validate --benchmark <benchmark_file>

   - `--benchmark`: Path to the benchmark YAML file.

   Example:
   ::
      sparced validate --benchmark benchmarks/TRAIL-response.yml

5. **Visualize Results**:
   Generate visualizations from simulation results:
   ::
      sparced visualize --input <results_directory> --output <output_file>

   - `--input`: Directory containing simulation results.
   - `--output`: File path for saving the visualization.

   Example:
   ::
      sparced visualize --input results/New-Simulation/Control --output figures/Control_Visualization.png

Advanced Options
===============================================================================

To view all options for a specific command, use the `--help` flag:
::
   sparced <command> --help

For example:
::
   sparced run --help

This will display detailed information about the `run` command and its options.

Examples
===============================================================================

Here are a few example workflows:

1. **Compile and Run a Model**:
   ::
      sparced compile --input models/SPARCED_standard.ant --output compiled_models/
      sparced simulate --model SPARCED_standard --condition data/simulation/standard_GeneReg.txt

2. **Generate and Validate a Benchmark**:
   ::
      sparced generate-benchmark --name TRAIL-response --output benchmarks/TRAIL-response.yml
      sparced validate --benchmark benchmarks/TRAIL-response.yml

3. **Visualize Results**:
   ::
      sparced visualize --input results/New-Simulation/Control --output figures/Control_Plot.png

Troubleshooting
===============================================================================

If you encounter issues while using the CLI tool, check the following:

1. **Environment**:
   Ensure the CLI tool is installed in your environment and accessible via the `sparced` command.

2. **Dependencies**:
   Verify all dependencies are installed:
   ::
      pip install -r requirements.txt

3. **Log Files**:
   Some commands may produce log files for debugging. Check the output directory for logs.

For additional help, use:
::
   sparced --help
