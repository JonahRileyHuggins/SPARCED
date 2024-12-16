#!/bin/bash

#--apt-package dependencies install script --#
# For Linux/Ubuntu 22.04-24.02 Desktop distros only #

# Add environment variables to .bashrc if not already present
grep -qxF 'export BLAS_LIBS=-lopenblas' ~/.bashrc || echo 'export BLAS_LIBS=-lopenblas' >> ~/.bashrc
grep -qxF 'export LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH' ~/.bashrc || echo 'export LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH' >> ~/.bashrc
source ~/.bashrc

# Function to check for root access
check_root() {
    if [ "$EUID" -ne 0 ]; then
        echo "Root access is required to install apt packages. Proceeding without installation..."
        return 1
    fi
    return 0
}

# Update and upgrade the system only if root access is available
if command -v apt >/dev/null 2>&1; then
    echo "Checking for root access to install apt packages..."
    if check_root; then
        echo "Updating system and installing necessary dependencies..."
        sudo apt-get update && sudo apt-get upgrade -y

        # Install necessary dependencies
        sudo apt install -y openmpi-bin openmpi-common libopenmpi-dev \
                gcc libopenblas-dev g++ cmake make python3-pip pipx \
                libgfortran5 libatomic1 swig libhdf5-dev libsbml-dev
    fi
else
    echo "apt command not found. Please ensure you are using a compatible Linux distribution."
fi

# Ensure pipx path
pipx ensurepath

# Install the Python package with pipx
if pipx install dist/SPARCED-2.0-py3-none-any.whl --verbose --force; then
    echo "SPARCED was successfully installed!"
else
    echo "SPARCED installation failed. Please check your system's compatibility and dependencies."
fi
