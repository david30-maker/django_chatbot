FROM python:3.10.12-slim-bullseye

# Set the working directory in the container
WORKDIR /app

# Set environment variables to ensure output is sent straight to the terminal without buffering
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Copy the requirements file into the container
COPY ./requirements.txt /app/

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Command to run the application using Gunicorn
ENTRYPOINT ["gunicorn", "core.wsgi", "-b", "0.0.0.0:8000"]
