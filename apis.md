---
layout: page
title: Public APIs for MINT
---

*Last update: Dec 19, 2019*

This document provides links to public MINT APIs and a summary of the documentation and specifications available.
 
Each API is evolving, the [release page](http://mint-project.info/releases.html) contains announcements about new versions.

Each API is documented as follows:
- An open API specification
- Ontologies and documentation about classes (when available)
- API documentation (in progress)

### Emulator APIs

We are creating two separate APIs for MINT Emulators
- **MINT Emulator Manager API:** to support search and discovery of emulators that are available in MINT
- **MINT Emulator Data Services APIs:** to support retrieval and processing of data in MINT emulators

We are building these two APIs based on an existing MINT [Ingestion API](https://ingestion.mint.isi.edu/v1.1.0/ui) that performs the following tasks:

- Gather model ensemble execution results.
- Store model ensemble results into a database.

#### Links
- Code: [https://github.com/mintproject/ingestion-api](https://github.com/mintproject/ingestion-api)
- API specification: [https://ingestion.mint.isi.edu/v1.1.0/ui]( https://ingestion.mint.isi.edu/v1.1.0/ui)


### Ensemble Manager API

The Ensemble Manager executes a model ensemble for all possible parameters and data combinations in a MINT modeling thread. It performs the following tasks:

- Submit model ensembles for execution (Options: Local execution or Scalable execution)
- Get Model Ensemble execution status


#### Links

- Code: [https://github.com/mintproject/mint-ensemble-manager](https://github.com/mintproject/mint-ensemble-manager)
- API specification [https://ensemble.mint.isi.edu/latest/api-docs](https://ensemble.mint.isi.edu/latest/api-docs)



### MINT Model Catalog

The MINT Model Catalog API provides detailed information about software models and metadata available in the MINT Model Catalog.

The API relies on the Software Description Ontology for Models  [https://w3id.org/okn/o/sdm](https://w3id.org/okn/o/sdm)

The MINT [Model Catalog API](https://api.models.mint.isi.edu/latest/ui/) supports:

- Get a list of all the resources (Model, ModelVersion, Parameters, Inputs, Variables and other classes).
  - For example: get all the `models` on MINT.
- Get the detailed information of a resource.
  - For example: get the description of the `model` [Topoflow](https://dev.mint.isi.edu/south_sudan/models/explore/TOPOFLOW/topoflow_3.5/topoflow_cfg_simple/topoflow_cfg_simple_Guder)
- Create, updates and deletes resources on the Model Catalog.
    - For example: Create a new `model`, delete or update an existing `model`.

Upcoming and planned new features include:
- Test model based on unit tests
- Get models based on region
- Get models based on variables and processes (eg standard variable names)


#### Clients:

We provides the following clients:

- [Python client](https://github.com/mintproject/model-catalog-python-api-client)
- [NodeJS client](https://github.com/mintproject/model-catalog-fetch-api-client)

#### Links

- Code: [https://github.com/mintproject/model-catalog-api](https://github.com/mintproject/model-catalog-api)
- API specification: [https://api.models.mint.isi.edu/latest/ui/](https://api.models.mint.isi.edu/latest/ui/)


### MINT Data Catalog

Provides access to a curated collection of a datasets in the MINT Data Catalog.

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



#### Links
- Code: [https://github.com/mintproject/MINT-DataCatalog-Public](https://github.com/mintproject/MINT-DataCatalog-Public)

