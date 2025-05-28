# Use a lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy bot code
COPY . .

COPY docs/campus_presentation_may_2025.pdf /docs/campus.pdf
COPY docs/pedago_presentation_may_2025.pdf /docs/pedago.pdf

# Run the bot
CMD ["python", "bot.py"]

