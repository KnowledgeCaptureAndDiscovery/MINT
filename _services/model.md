---
permalink: "/products/model/"
layout: page
title:  "Model Services"
---

The [MINT Model Catalog](#model-catalog-api) provides detailed information about software models and metadata available in MINT. 
A good overview about the concepts is available [here](https://mintproject.readthedocs.io/en/latest/modelcatalog/).

## Overview

We provide multiple services to add, modify, and browse models:
1. Create and edit your models 
    - [Model Insertion Checker (MIC)](#model-insertion-checker-mic) [CLI] encapsulates your code and add the your model using [MINT Model Catalog API](#model-catalog-api)
    - [Model Catalog Explorer](#model-catalog-explorer) (GUI) modifies the contents of the MINT Model Catalog using [MINT Model Catalog API](#model-catalog-api)
2. Browse avaialable models:
    - [Model Catalog Explorer](#model-catalog-explorer) (GUI) shows the contents of the MINT Model Catalog using [MINT Model Catalog API](#model-catalog-api)
3. Execute models:
    - [MINT-UI](#model-catalog-explorer) obtains the details about the models using [MINT Model Catalog API](#model-catalog-api) and run it in your servers. 
    - [Desktop Application for Model Execution (DAME)](https://model-catalog-python-api-client.readthedocs.io/en/latest/example/) obtains the details about the models using [MINT Model Catalog API](#model-catalog-api) and run it in your computer.

## Services

### Model Catalog API 

Model Catalog API for adding/modifying/deleting model metadata. We provide the following clients to improve the experience to developers available [here](#model-service-api-clients)

[[RESTAPI](https://api.models.mint.isi.edu/latest)] [[Documentation](https://model-catalog-python-api-client.readthedocs.io/en/latest/endpoints/)] [[Code](https://github.com/mintproject/model-catalog-api)] [[Releases](https://github.com/mintproject/model-catalog-api/releases)]

### Model Catalog Explorer

GUI for exploring the contents of the model catalog

[[Website](https://models.mint.isi.edu/home)] [[Demo](https://www.youtube.com/watch?v=C9rxGT2k9is)]

Also, a registered user can add, edit, and remove their models.

### Model Insertion Checker (MIC)

Model Insertion CLI (MIC) is a command-line interface for adding models on a Model Catalog Service using the previous service [Model Catalog API](#model-catalog-api).

[[How to use it?](https://mic-cli.readthedocs.io/en/latest/)] [[Code](https://github.com/mintproject/mic)] [[Documentation](https://mic-cli.readthedocs.io/en/latest/)] [[Releases](https://github.com/mintproject/mic/releases)]

### Desktop appliation for model execution (DAME)

The Desktop Application for Model Execution (DAME) is an application for executing environmental models in any local environment or server through a command line interface.

Given a model identifier (e.g., TopoFlow for the Awash region: topoflow36_2.1.0_Awash), DAME downloads the model container and its execution environment, and fetches the datasets needed (e.g., soil data, elevation data, etc). Then users can run the model with different input scenario

[[How to use it?](https://dame-cli.readthedocs.io/en/latest/)] [[Code](https://github.com/mintproject/dame_cli/)] [[Releases](https://github.com/mintproject/dame_cli/releases)]

### Tools

#### Model Service API clients

We provide the following clients to improve the experience of the developers.

These clients support all the operations.

- Get a list of all resources. For example: get all the models in MINT.
- Get the details of a resource. For example: get the description of the model [CYCLES](https://models.mint.isi.edu/models/explore/CYCLES)
- Create, updates, and deletes resources on the Model Catalog. For example, create a new model, delete or update an existing model.

##### Python

[[How to use it?](https://model-catalog-python-api-client.readthedocs.io/en/latest/)] [[Code](https://github.com/mintproject/model-catalog-python-api-client/)] [[Releases](https://github.com/mintproject/model-catalog-python-api-client/releases)]



##### JavaScript

[[Code](https://github.com/mintproject/model-catalog-fetch-api-client)] [[Documentation](https://github.com/mintproject/model-catalog-fetch-api-client/blob/master/README.md)] [[Releases](https://github.com/mintproject/model-catalog-fetch-api-client/releases)]