---
permalink: "/products/model/"
layout: page
title:  "Model Services"
---

The [MINT Model Catalog](#model-catalog-api) provides detailed information about software models and metadata available in MINT. 
A good overview about the concepts is available [here](https://mintproject.readthedocs.io/en/latest/modelcatalog/).

## Overview

We provide multiple services to add, modify, and browse model metadata:
1. Create and edit your models 
    - [Model Insertion Checker (MIC) - BETA](#model-insertion-checker-mic) [CLI]: Application to help users encapsulate model code and capture their model metadata using the [MINT Model Catalog API](#model-catalog-api)
    - [Model Catalog Explorer](#model-catalog-explorer): GUI designed to help users modify the contents of the MINT Model Catalog using the [MINT Model Catalog API](#model-catalog-api)
2. Browse available models:
    - [Model Catalog Explorer](#model-catalog-explorer): GUI that helps users browse and explore the contents of the MINT Model Catalog using the [MINT Model Catalog API](#model-catalog-api)
3. Execute models:
    - [MINT-UI](#model-catalog-explorer): Application designed to guide users when setting up  and executing a MINT model. It uses the [MINT Model Catalog API](#model-catalog-api) and can be run in any server. 
    - [Desktop Application for Model Execution (DAME)](https://model-catalog-python-api-client.readthedocs.io/en/latest/example/): Application designed to execute any model in the MINT model catalog in your local machine or server. DAME obtains the execution details of models using [MINT Model Catalog API](#model-catalog-api).

## Services

### Model Catalog API 

Model Catalog API for adding/modifying/deleting model metadata. We provide several clients (available [here](#model-service-api-clients)) to improve the experience for developers when accessing the contents of our APIs.

[[RESTAPI](https://api.models.mint.isi.edu/latest)] [[Documentation](https://model-catalog-python-api-client.readthedocs.io/en/latest/endpoints/)] [[Code](https://github.com/mintproject/model-catalog-api)] [[Releases](https://github.com/mintproject/model-catalog-api/releases)]

### Model Catalog Explorer

GUI for browsing the contents of the model catalog

[[Website](https://models.mint.isi.edu/home)] [[Demo](https://www.youtube.com/watch?v=C9rxGT2k9is)]

Registered users can add, edit, and remove metadata of their models, as well as creating new model setups, for example, adapting an existing model to a new region.

### Model Insertion Checker (MIC)

The Model Insertion Checker (MIC) is a command-line interface for encapsulating models in a Model Catalog Service using the [Model Catalog API](#model-catalog-api).

[[Documentation](https://mic-cli.readthedocs.io/en/latest/)] [[Code](https://github.com/mintproject/mic)] [[Releases](https://github.com/mintproject/mic/releases)]

### Desktop application for model execution (DAME)

The Desktop Application for Model Execution (DAME) is a command line interface designed to execute model components in any local host or server.

Given a model identifier (e.g., TopoFlow for the Awash region: topoflow36_2.1.0_Awash), DAME downloads the model container, its execution environment, and fetches the datasets needed (e.g., soil data, elevation data, etc) so users can run the model with different input scenarios.

[[Documentation](https://dame-cli.readthedocs.io/en/latest/)] [[Code](https://github.com/mintproject/dame_cli/)] [[Releases](https://github.com/mintproject/dame_cli/releases)]

### Tools

#### Model Service API clients

We provide two clients (Python and Javascript) to help developers access the model service APIs.

Both clients support the following operations:

- Get a list of all exiting resources of a class. For example: get all the models in MINT, get a list with all variables, all regions, etc.
- Get the details of a resource. For example: get the description of the model [CYCLES](https://models.mint.isi.edu/models/explore/CYCLES)
- Create, update, and delete model resources and metadata in the Model Catalog. 

##### Python

[[Documentation](https://model-catalog-python-api-client.readthedocs.io/en/latest/)] [[Code](https://github.com/mintproject/model-catalog-python-api-client/)] [[Releases](https://github.com/mintproject/model-catalog-python-api-client/releases)]



##### JavaScript

 [[Documentation](https://github.com/mintproject/model-catalog-fetch-api-client/blob/master/README.md)]  [[Code](https://github.com/mintproject/model-catalog-fetch-api-client)][[Releases](https://github.com/mintproject/model-catalog-fetch-api-client/releases)]


### Ontologies
We have developed two main ontologies to help structure the metadata and contents of the model catalog:

#### Software Description Ontology (SD)
Ontology used to capture the overall metadata of scientific software, including its versions, functionality, inputs, outputs, etc. SD builds on existing efforts, such as [Schema.org](https://schema.org/) and [OntoSoft](https://ontosoft.org/). [[Documentation](https://w3id.org/okn/o/sd)] [[Download](https://github.com/KnowledgeCaptureAndDiscovery/SoftwareDescriptionOntology)]


#### Software Description Ontology for Models (SDM)
Extension of the Software Description Ontology to capture metadata specific to models (e.g., the region where they are valid, their spatial grid, their temporal restrictions, etc.). [[Documentation](https://w3id.org/okn/o/sdm/)] [[Download](https://github.com/mintproject/Mint-ModelCatalog-Ontology)]