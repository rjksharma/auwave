# Use the Python base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files to the container
COPY . .

# Copy the .sh file
COPY build_files.sh .

# Grant execute permissions to the .sh file
RUN chmod +x build_files.sh

# Expose the Gunicorn port
EXPOSE 8000

# Start Gunicorn with the .sh file
CMD ["./build_files.sh"]
