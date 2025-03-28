# Must be built from the root directory of the repo
# BUILD: docker build -t sparced -f container/Dockerfile .
# TEST LOCAL (optional): docker run -p 8888:8888 --name test1 -i -t sparced
# TAG: docker tag sparced birtwistlelab/sparced:latest
# PUSH: docker push birtwistlelab/sparced:latest

FROM ubuntu:22.04

# Copy SPARCED files (ensure build context matches path)
RUN mkdir -p /SPARCED
COPY . /SPARCED/

# Set working directory
WORKDIR /SPARCED

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive \
    SHELL=/bin/bash \
    BLAS_LIBS=-lopenblas \
    PATH=/root/.local/bin:$PATH \
    LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH \
    PIPX_HOME=/usr/local/pipx \
    PIPX_BIN_DIR=/usr/local/bin \
    OMPI_ALLOW_RUN_AS_ROOT=1 \
    OMPI_ALLOW_RUN_AS_ROOT_CONFIRM=1 


# Remove .git directory from SPARCED
RUN rm -rf ./SPARCED/.git

# Update and install basic dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        git \
        python3-pip \
        python3-venv \
        python3-dev \
        rsync \
        openmpi-bin \
        openmpi-common \
        libopenmpi-dev \
        libopenblas-dev \
        gcc \
        g++ \
        cmake \
        make \
        pipx \
        libgfortran5 \
        libatomic1 \
        swig \
        libhdf5-dev \
        libsbml-dev \
        && apt-get clean && rm -rf /var/lib/apt/lists/*

# Create persistent paths for pipx
RUN mkdir -p $PIPX_HOME $PIPX_BIN_DIR

# Install Python dependencies using pipx
RUN pipx ensurepath
RUN pipx install dist/sparced-2.0-py3-none-any.whl --verbose --force

# Set default shell
SHELL ["/bin/bash", "-c"]

# Test the installation
RUN sparced --help

