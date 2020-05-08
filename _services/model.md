---
permalink: "/products/model/"
layout: page
title:  "Model Services"
---

The [MINT Model Catalog](#model-catalog-api) provides detailed information about software models and metadata available in MINT. See an overview on the following [link](https://mintproject.readthedocs.io/en/latest/modelcatalog/).

You can:
- Insert new models to the MINT Model Catalog through the [Model Insertion Checker (MIC)] 
    - [Model Insertion Checker (MIC)](#model-insertion-checker-mic) inserts the information using [MINT Model Catalog](#model-catalog-api)
- Browse avaialable models:
    - Using our GUI [Model Catalog Explorer](#model-catalog-explorer)
- Execute models:
    - Using our GUI [Model Catalog Explorer](#model-catalog-explorer)
    - Using [Desktop Application for Model Execution (DAME)](https://model-catalog-python-api-client.readthedocs.io/en/latest/example/).  

### Model Catalog API 

Model catalog API for adding/modifying/deleting model metadata. We provide the following clients to improve the experience to developers available [here](#model-service-api-clients)

[[RESTAPI](https://api.models.mint.isi.edu/latest)] [[Documentation](https://model-catalog-python-api-client.readthedocs.io/en/latest/endpoints/)] [[Code](https://github.com/mintproject/model-catalog-api)] [[Releases](https://github.com/mintproject/model-catalog-api/releases)]

### Model Catalog Explorer

GUI for exploring the contents of the model catalog

[[Website](https://models.mint.isi.edu/home)] [[Demo](https://www.youtube.com/watch?v=C9rxGT2k9is)]

In addition, a register user can add, edit and remove their models.

### Model Insertion Checker (MIC)

Model Insertion CLI (MIC) is a command-line interface for adding models on a Model Catalog Service using the previous service [Model Catalog API](#model-catalog-api).

[[How to use it?](https://mic-cli.readthedocs.io/en/latest/)] [[Code](https://github.com/mintproject/mic)] [[Documentation](https://mic-cli.readthedocs.io/en/latest/)] [[Releases](https://github.com/mintproject/mic/releases)]


### Tools

#### Model Service API clients

We provide the following clients to improve the experience to the developers.

These clients support all the operations.

- Get a list of all resources. For example: get all the models in MINT.
- Get the details of a resource. For example: get the description of the model [CYCLES](https://models.mint.isi.edu/models/explore/CYCLES)
- Create, updates and deletes resources on the Model Catalog. For example, create a new model, delete or update an existing model.

##### Python

[[How to use it?](https://model-catalog-python-api-client.readthedocs.io/en/latest/)] [[Code](https://github.com/mintproject/model-catalog-python-api-client/)] [[Releases](https://github.com/mintproject/model-catalog-python-api-client/releases)]



##### JavaScript

[[Code](https://github.com/mintproject/model-catalog-fetch-api-client)] [[Documentation](https://github.com/mintproject/model-catalog-fetch-api-client/blob/master/README.md)] [[Releases](https://github.com/mintproject/model-catalog-fetch-api-client/releases)]