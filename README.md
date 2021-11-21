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

Deploy as Azure Container Instance

    az group create -n <group> -l <location>
    az acr create -g <group> -n <registry> --sku Basic --admin-enabled true
    az acr list -g <group> -o table

    docker tag spam-detection <registry>.azurecr.io/spam-detection:v1
    az acr login -n <registry>
    docker push <registry>.azurecr.io/spam-detection:v1
    az container create -g <group> -n <container> --image <registry>.azurecr.io/spam-detection:v1 --dns-name-label <label> --ports 80
    az container show -g <group> -n <container> --query "{FQDN:ipAddress.fqdn,ProvisioningState:provisioningState}"
    az container logs -g <group> -n <container>

    open http://<label>.<location>.azurecontainer.io
