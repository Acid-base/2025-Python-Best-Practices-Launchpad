# Use the official Python 3.10 image as the base image
FROM python:3.10-slim-bullseye

# Set environment variables for non-interactive installations
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Linuxbrew (or Homebrew) for consistent package management
RUN /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" && \
    echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> ~/.bashrc && \
    eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"

# Install Python dependencies using Linuxbrew or pip
RUN brew install python

# Set up working directory
WORKDIR /workspace

# Copy the project files into the container
COPY . /workspace/

# Install `uv` (your dependency manager) using pip
RUN pip install uv

# Install project dependencies from the lock file
RUN uv sync

# Install pre-commit hooks
RUN pip install pre-commit && pre-commit install

RUN pip install mypy
RUN pip install ruff
# Expose port 8000 (you can customize this based on your needs)
EXPOSE 8000

# Set the default command to open a bash shell
CMD ["bash"]
