FROM python:3.9.10

# Set the working directory to /app inside the container
WORKDIR /app

# Copy the requirements.txt file into the container's working directory (/app)
COPY requirements.txt .

# Install the dependencies listed in requirements.txt
RUN pip install --default-timeout=6000 -r requirements.txt

# Copy all files from the current directory into the container's working directory (/app)
COPY . /app

# Expose port 80 to allow external access to the container
EXPOSE 80

# Command to run when the container starts, using uvicorn to serve the FastAPI app
CMD ["uvicorn", "api:api_app", "--host", "0.0.0.0", "--port", "80", "--reload"]
