FROM python:3.9-slim
RUN pip install --no-cache-dir scikit-learn fastapi uvicorn
WORKDIR /app
ADD . /app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
