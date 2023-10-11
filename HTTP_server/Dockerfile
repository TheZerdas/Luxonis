# Use an official Python runtime as a parent image
FROM python:3.8.10

# Set the working directory inside the container
WORKDIR /app

# Copy the Flask application files to the container
COPY . /app

# Install any additional dependencies needed for your Flask application
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port on which your Flask application will listen (e.g., 8080)
EXPOSE 8080

# Define the command to run your Flask application
CMD ["python", "app.py"]