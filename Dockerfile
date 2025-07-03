# Use official Python image
FROM python:3.12-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 5000

# Default environment variables
ENV FLASK_APP=app.main
ENV PYTHONUNBUFFERED=1

# Command to run migrations and start the app
CMD ["sh", "-c", "flask db upgrade && python -m app.main"]
