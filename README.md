# ONS Engineer  - Banking App Infrastructure

This repository is part of the microservice training for the ONS Software
Engineering Session.

## Contents

This repository contains the Kubernetes configuration for shared infrastructure
used by the microservices. This includes:

- The [RabbitMQ](https://www.rabbitmq.com/) message broker
- The Ingress API routes

## Deploying

### 1. Update the hosts in the [ingress.yml](./kubernetes/ingress.yml)

For the app, use `GITHUSER-banking-app.apps.onse-training.co.uk`.

For the RabbitMQ dashboard use `GITHUSER-banking-rabbit.apps.onse-training.co.uk`.

### 2. Deploy

`kubectl -n NAMESPACE apply -f kubernetes/`

Note: There is an included [Jenkinsfile](./Jenkinsfile) which allows this step
to be done via a pipeline.