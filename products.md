---
layout: page
title: MINT Services and Software
---

*Last updated: 2020-03-24*

This document provides links to public MINT products (APIs, software, data and services) and a summary of the documentation and specifications available.

Each product is evolving, the [release page]({{ '/releases.html' | absolute_url }}) contains announcements about new versions.


## MINT User Interface

MINT assists an analyst to easily use sophisticated simulation models and data in order to explore the role of weather and climate in water on food availability in select regions of the world. 

### Relevant Pointers

 * The MINT Portal can be accessed in the following URL:  [https://mint.isi.edu/](https://mint.isi.edu/)
 * Documentation page: [https://mintproject.readthedocs.io/en/latest/](https://mintproject.readthedocs.io/en/latest/)
 * The MINT Training Document that introduces visually the main components of the MINT user interface is available [here](https://drive.google.com/file/d/12nx2MkZuZUzKj2pP0ZRz8u3j7_vVfND2/view). 
 * A video with a walkthrough of the MINT user interface is available [here](https://drive.google.com/file/d/1FENjOdCkbES_Cc8s74tKUrJSEvQXs1zv/view)


## Data Services

The MINT Data Catalog (see [overview](https://mintproject.readthedocs.io/en/latest/datacatalog/)) provides access to a curated collection of a datasets in the MINT Data Catalog.

The MINT Data Catalog API documentation: [https://data-catalog.mint.isi.edu/documentation](https://data-catalog.mint.isi.edu/documentation)

The MINT [Data Catalog API](https://data-catalog.mint.isi.edu/documentation) performs the following tasks:

- Create an entry for a dataset.
- Create entries for the data files and the standard variable names in the data.
- Get all the variables for a dataset.
- Get all resources for a dataset.
- Get all datasets for an area (given a bounding box).
- Metadata about the dataset, standard variable names, and files.
- Full-text search of a dataset.
- Search datasets by name, id, or standard variable names.

Upcoming and planned new features include:

- Generate a pipeline to transform a dataset into a target format
- Get all data transformations that use or generate a data format

### Relevant Pointers
- Code: [https://github.com/mintproject/MINT-DataCatalog-Public](https://github.com/mintproject/MINT-DataCatalog-Public)
- Portal: [https://data-catalog.mint.isi.edu](https://data-catalog.mint.isi.edu)

## Model Services

The MINT Model Catalog provides detailed information about software models and metadata available in MINT. See an overview on the following [link](https://mintproject.readthedocs.io/en/latest/modelcatalog/).

The models in the Model Catalog are executable through the [Desktop Application for Model Execution (DAME)](https://model-catalog-python-api-client.readthedocs.io/en/latest/example/). 

### Relevant Pointers:

- Code: [https://github.com/mintproject/model-catalog-api](https://github.com/mintproject/model-catalog-api)
- GUI for exploring the contents of the model catalog: [https://models.mint.isi.edu/home](https://models.mint.isi.edu/home). [(See a video of the main features)](https://www.youtube.com/watch?v=C9rxGT2k9is)
- REST API for adding/modifying/deleting model metadata: [https://api.models.mint.isi.edu/latest](https://api.models.mint.isi.edu/latest)
- [Requires log in] GUI for configuring and editing models: [https://mint.isi.edu/ethiopia/models/configure](https://mint.isi.edu/ethiopia/models/configure)
- Model services API client and examples: [https://model-catalog-python-api-client.readthedocs.io/en/latest/](https://model-catalog-python-api-client.readthedocs.io/en/latest/)
- Model catalog API documentation: [https://model-catalog-python-api-client.readthedocs.io/en/latest/endpoints/](https://model-catalog-python-api-client.readthedocs.io/en/latest/endpoints/)

The API relies on the Software Description Ontology for Models  [https://w3id.org/okn/o/sdm](https://w3id.org/okn/o/sdm)

The MINT [Model Catalog API](https://api.models.mint.isi.edu/latest/ui/) supports:

- Get a list of all the resources (Model, ModelVersion, Parameters, Inputs, Variables and other classes).
  - For example: get all the models on MINT.
- Get the detailed information of a resource.
  - For example: get the description of the model [Topoflow](https://dev.mint.isi.edu/south_sudan/models/explore/TOPOFLOW/topoflow_3.5/topoflow_cfg_simple/topoflow_cfg_simple_Guder)
- Create, updates and deletes resources on the Model Catalog.
    - For example: Create a new model, delete or update an existing model.
   

## Execution Management Services


### Emulator APIs
We are creating two separate APIs for MINT Emulators
- **MINT Emulator Manager API:** to support search and discovery of emulators that are available in MINT
- **MINT Emulator Data Services APIs:** to support retrieval and processing of data in MINT emulators

We are building these two APIs based on an existing MINT [Ingestion API](https://ingestion.mint.isi.edu/v1.1.0/ui) that performs the following tasks:

- Gather model ensemble execution results.
- Store model ensemble results into a database.

#### Relevant Pointers
- Code: [https://github.com/mintproject/ingestion-api](https://github.com/mintproject/ingestion-api)
- API specification: [https://ingestion.mint.isi.edu/v1.1.0/ui]( https://ingestion.mint.isi.edu/v1.1.0/ui)

### Ensemble Manager API

The Ensemble Manager executes a model ensemble for all possible parameters and data combinations in a MINT modeling thread. It performs the following tasks:

- Submit model ensembles for execution (Options: Local execution or Scalable execution)
- Get Model Ensemble execution status

#### Relevant Pointers

- Code: [https://github.com/mintproject/mint-ensemble-manager](https://github.com/mintproject/mint-ensemble-manager)
- API specification [https://ensemble.mint.isi.edu/latest/api-docs](https://ensemble.mint.isi.edu/latest/api-docs)

## Scientific Variables
[Section to be completed]

#### Relevant Pointers
- SVO Ontology: [http://www.geoscienceontology.org/svo/](http://www.geoscienceontology.org/svo/)


## Remote Sensing
[Section to be completed]




