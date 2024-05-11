FROM python:latest

# Set working directory
WORKDIR /app

# Copy requirements.txt to the container at /app
# COPY requirements.txt .

# Install dependencies
# RUN pip install -r requirements.txt
COPY . .
RUN pip install datasets pandas pymongo sentence_transformers
# RUN pip install -U transformers
# RUN pip install accelerate
# RUN pip uninstall torch -y
# RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
RUN pip install python-dotenv
RUN pip install Flask
RUN pip install google
# RUN pip install langchain_google_genai
# RUN pip install langchain

# Copy the rest of the application code

# Expose port 5000
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app/app.py"]
