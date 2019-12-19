---
layout: page
title: Public APIs
---

### Model Catalog

The Model Catalog API provides detailed information about software models and metadata available in the MINT Model Catalog.


[Model Catalog API](https://api.models.mint.isi.edu/v1.3.0/ui/) performs the following tasks:

- Get a list of all the resources (Model, ModelVersion, Parameters, Inputs, Variables and more).
  - For example: get all the `models` on MINT.
- Get the detailed information of a resource.
  - For example: get the description of the `model` [Topoflow](https://dev.mint.isi.edu/south_sudan/models/explore/TOPOFLOW/topoflow_3.5/topoflow_cfg_simple/topoflow_cfg_simple_Guder)
- Create, updates and deletes resources on the Model Catalog.
    - For example: Create a new `model`, delete or update an existing `model`.

#### Clients:

We provides the following clients:

- [Python client](https://github.com/mintproject/model-catalog-python-api-client)
- [NodeJS client](https://github.com/mintproject/model-catalog-fetch-api-client)

#### Links

- Code: [https://github.com/mintproject/model-catalog-api](https://github.com/mintproject/model-catalog-api)
- API specification: [https://api.models.mint.isi.edu/v1.3.0/ui/](https://api.models.mint.isi.edu/v1.3.0/ui/)


### DataCatalog

Provides a curated collection of a dataset from DataCatalog

[Data Catalog API](https://data-catalog.mint.isi.edu/documentation) performs the following tasks:

- Create a dataset.
- Create the resources and the standard variables.
- List all the variables for a dataset.
- List all resources for a dataset.
- Detailed information about the dataset, standard variable, and resource.
- Full-text search of a dataset.
- Search datasets by name, id, or standard variables.

#### Links
- Code: [https://github.com/mintproject/MINT-DataCatalog-Public](https://github.com/mintproject/MINT-DataCatalog-Public)
- API specification: [https://data-catalog.mint.isi.edu/documentation](https://data-catalog.mint.isi.edu/documentation)


### Ingestion API

[Ingestion API]( https://ingestion.mint.isi.edu/v1.1.0/ui) performs the following tasks:

- Post-process the output and save the execution trace into the MINT-Database.
- Provide a summary of a MINT execution(s) to the user.

We plan to split the Ingestion API in the future into the following two sets of APIs
- MINT Emulator Manager API
- MINT Emulator Data Services APIs

#### Links
- Code: [https://github.com/mintproject/ingestion-api](https://github.com/mintproject/ingestion-api)
- API specification: [https://ingestion.mint.isi.edu/v1.1.0/ui]( https://ingestion.mint.isi.edu/v1.1.0/ui)

### Ensemble Manager

The Ensemble Manager executes a model ensemble for all possible parameters and data combinations in a MINT modeling thread. It performs the following tasks:

- Run Model Ensembles ( Locally or via WINGS/Pegasus )
- Monitor Model Ensembles

#### Links

- Code: [https://github.com/mintproject/mint-ensemble-manager](https://github.com/mintproject/mint-ensemble-manager)
- API specification [https://ensemble.mint.isi.edu/v1/api-docs](https://ensemble.mint.isi.edu/v1/api-docs)

### Wings API

[WINGS API](https://api.wings.mint.isi.edu/v1.0.0/ui/) submits executions using [Wings Workflows](https://github.com/KnowledgeCaptureAndDiscovery/wings) and [Pegasus](https://pegasus.isi.edu/)

#### Links
- Code: [https://github.com/KnowledgeCaptureAndDiscovery/wings-api](https://github.com/KnowledgeCaptureAndDiscovery/wings-api)
- API specification [https://api.wings.mint.isi.edu/v1.0.0/ui/](https://api.wings.mint.isi.edu/v1.0.0/ui/)
