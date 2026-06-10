FROM python:3.14-slim

# Install PostgreSQL client (optional, for debugging) and clean apt cache
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first (for better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Run pytest as default command
CMD ["python", "main.py"]