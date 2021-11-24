# Spam Detection with SKLearn, FastAPI on Azure Container Instance

## Dataset

The UCI [SMS Spam Collection](https://data.world/uci/sms-spam-collection) is a public
set of SMS labeled messages that have been collected for mobile phone spam research.

## Setup

Create environment:

    conda create --name spam
    conda activate spam
    conda install --yes --file requirements.txt

Train spam classifier model:

    python train.py

For local testing, start server and open SwaggerUI

    uvicorn app:app --reload
    open http://localhost:8000/docs

Test local endpoint:

    curl http://localhost:8000/predict?message=I want your Money

## Build Docker Image

Build docker image and run docker container:

    docker build -t spam .
    docker run -d --rm --name spam -p 80:80 spam

## Deploy as Azure Container Instance

Use Azure Container Instances (ACI) to run serverless Docker containers in Azure.

Create Azure Container Registry (ACR):

    az login
    az group create -n <group> -l <location>
    az acr create -g <group> -n <reg> --sku Basic --admin-enabled true
    az acr list -g <group> -o table

Upload docker image to ACR

    docker tag spam <reg>.azurecr.io/spam:v1
    az acr login -n <reg>
    docker push <reg>.azurecr.io/spam:v1

Create container (find username and password here: Portal > Container Registry > Access Keys)

    az container create -g <group> -n <container> --image <reg>.azurecr.io/spam:v1 --dns-name-label <label> --ports 80
    az container show -g <group> -n <container> --query "{FQDN:ipAddress.fqdn,ProvisioningState:provisioningState}"
    az container logs -g <group> -n <container>

Open SwaggerUI
    
    open http://<label>.<location>.azurecontainer.io

Delete resource group
    
    az group delete -n <group>
