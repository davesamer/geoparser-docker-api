FROM python:3.11-slim

WORKDIR /app

# Copy and install pip requirements
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_trf


# Copy the script and data into the container
COPY ./app /app/

# Command to run the FastAPI application using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]