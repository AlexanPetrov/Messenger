# Define how to build & run container image (application in container)

# Official Python image from Docker Hub
FROM python:3.11-slim

# Working directory inside the container
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the app's source code to the container
COPY . .

# Expose port 8000 to access the FastAPI app
EXPOSE 8000

# Command to run the FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
