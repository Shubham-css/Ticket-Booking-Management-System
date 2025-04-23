# Use official Python image
FROM python:3.13-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Expose port and run the server
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
