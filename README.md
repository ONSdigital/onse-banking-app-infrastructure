# ONS Engineer  - Banking App Infrastructure

This repository is part of the microservice training for the ONS Software
Engineering Session.

## Contents

This repository contains the Kubernetes configuration for shared infrastructure
used by the microservices. This includes:

- The [RabbitMQ](https://www.rabbitmq.com/) message broker
- The Ingress API routes

## Deploying

### 1. Set DockerHub Credentials

Create Docker config file:

`python create_docker_config.py`

Create a Kubernetes secret:

`kubectl -n NAMESPACE create secret generic regcred --from-file=dockerconfigjson=docker-config.json`

NOTE: If you want to delete your Kubernetes secret, then run:

`kubectl -n NAMESPACE delete secret regcred`

### 2. Update the hosts in the [ingress.yml](./kubernetes/ingress.yml)

For the app, use `GITHUSER-banking-app.apps.onse-training.co.uk`.

For the RabbitMQ dashboard use `GITHUSER-banking-rabbit.apps.onse-training.co.uk`.

### 3. Deploy

`kubectl -n NAMESPACE apply -f kubernetes/`

Note: There is an included [Jenkinsfile](./Jenkinsfile) which allows this step
to be done via a pipeline.