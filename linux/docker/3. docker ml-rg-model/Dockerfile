FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
COPY linear_regression.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "linear_regression.py"]
