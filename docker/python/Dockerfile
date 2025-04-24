FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Set Python path
ENV PYTHONPATH=/app

# Expose the port the app runs on
EXPOSE 8001

# Command to run the application
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"] 