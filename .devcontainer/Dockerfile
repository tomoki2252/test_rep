# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the working directory in the container
WORKDIR /workspace

# Create a non-root user and switch to it
RUN useradd -ms /bin/bash vscode
USER vscode

# Copy the requirements file into the container
COPY --chown=vscode:vscode requirements.txt .

# The postCreateCommand in devcontainer.json will run `pip install`.
# This helps to avoid rebuilding the container image for dependency changes.
