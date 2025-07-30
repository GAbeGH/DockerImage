# Dockerfile for a Python application
# Use a lightweight Python image as the base
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy your project files into the container
COPY pyproject.toml ./

# (Optional) Install dependencies
# RUN pip install -r requirements.txt
RUN pip install .

# puts source code in image
# guides python to source code
COPY src/ ./src/ 
ENV PYTHONPATH=/app/src

# ENTRYPOINT  runs container without extra commands
# default command that docker will run when the container starts
# in this case it runs python interpeter with main.py
ENTRYPOINT [ "python", "src/main.py" ]
