# Use a lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy bot code
COPY . .

COPY docs/pedago_presentation_may_2025.pdf /docs/test.pdf
COPY docs/pedago_presentation_may_2025.pdf /docs/test1.pdf

# Run the bot
CMD ["python", "bot.py"]

