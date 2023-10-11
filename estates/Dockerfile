# Use an official Python runtime as a parent image
FROM python:3.8.10

# Set the working directory inside the container
WORKDIR /app

# Copy the Scrapy project files to the container
COPY . /app

# Install any additional dependencies needed for your Scrapy project
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Define the command to run your Scrapy spider
CMD ["scrapy", "crawl", "estates"]