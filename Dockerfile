# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Collect staticfiles
RUN python manage.py collectstatic --noinput

# Migrate database
RUN python manage.py migrate

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application"]
