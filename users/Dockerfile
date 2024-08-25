# Use the official Python image with a specific version
FROM python:3.12-slim-bullseye

# Environment variable to ensure Python output is sent directly to the terminal (useful for logging)
ENV PYTHONUNBUFFERED=1

# Update the package list and install dependencies
RUN apt-get update && apt-get -y install gcc libpq-dev

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/
