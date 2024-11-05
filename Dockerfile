# Use the official Python 3.9 image
FROM python:3.9.19-slim

# Set the environment variable
ENV PYTHONUNBUFFERED True

# Set the working directory
WORKDIR /server

RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y gcc default-libmysqlclient-dev pkg-config vim && \
    rm -rf /var/lib/apt/lists/*  # Clean up apt cache


# Copy the requirements file to the working directory
COPY requirements.txt /server/

# Install any needed packages
RUN pip install --no-cache-dir -r requirements.txt 

# Copy the rest of the application code to the working directory
COPY . /server/

# Expose the port that the FastAPI server will run on
EXPOSE 8000

# Command to run the FastAPI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
