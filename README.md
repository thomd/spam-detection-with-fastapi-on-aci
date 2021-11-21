# Spam Detection with SciKit-Learn, FastAPI on Docker

## Setup

Create environment:

    conda env create --file environment.yaml
    conda activate spam

Train spam classifier model:

    pyhon train.py

For local testing, start server with

    uvicorn app:app --reload

and open Swagger-UI:

    open http://localhost:8000/docs

Test:

    curl http://localhost:8000/predict?message=I want your Money

## Docker

Build docker image and run docker container:

    docker build -t spam-detection .
    docker run -d --rm --name spam -p 80:80 spam-detection
