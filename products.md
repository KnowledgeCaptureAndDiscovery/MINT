---
layout: page
title: MINT Services and Software
---

*Last updated: 2020-04-28*

This document provides links to public MINT products (APIs, software, data and services) and a summary of the documentation and specifications available.

Each product is evolving, the [release page]({{ '/releases.html' | absolute_url }}) contains announcements about new versions.


## MINT User Interface

MINT assists an analyst to easily use sophisticated simulation models and data in order to explore the role of weather and climate in water on food availability in select regions of the world. 

### Relevant Pointers

 * The MINT Portal can be accessed in the following URL:  [https://mint.isi.edu/](https://mint.isi.edu/)
 * Documentation page: [https://mintproject.readthedocs.io/en/latest/](https://mintproject.readthedocs.io/en/latest/)
 * The MINT training document introduces visually the main components of the MINT user interface and is available [here](https://drive.google.com/file/d/12nx2MkZuZUzKj2pP0ZRz8u3j7_vVfND2/view). 
 * A video with a walkthrough of the MINT user interface is available [here](https://youtu.be/g3wVmqIC6Kc)


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
- [Demo](https://youtu.be/9ER74oVgkv0) of registering a dataset using API
- [Demo](https://youtu.be/DIKU-4k5mKs) of fetching for a dataset using API
- [Python notebook](https://github.com/mintproject/MINT-DataCatalog-Public/blob/master/demo/api_demo.ipynb) of registering a dataset using API
- [Python notebook](https://github.com/mintproject/MINT-DataCatalog-Public/blob/master/demo/CHIRPS_browse.ipynb) of searching for a dataset using API

Upcoming and planned new features include:

- Generate a pipeline to transform a dataset into a target format
- Get all data transformations that use or generate a data format

### Relevant Pointers
- Code: [https://github.com/mintproject/MINT-DataCatalog-Public](https://github.com/mintproject/MINT-DataCatalog-Public)
- Portal: [https://data-catalog.mint.isi.edu](https://data-catalog.mint.isi.edu)

## Model Services

The MINT Model Catalog provides detailed information about software models and metadata available in MINT. See an overview on the following [link](https://mintproject.readthedocs.io/en/latest/modelcatalog/).

The models in the Model Catalog are executable through the [Desktop Application for Model Execution (DAME)](https://model-catalog-python-api-client.readthedocs.io/en/latest/example/). 

New model descriptions can be added to the model catalog through the the [model insertion checker wizard](https://mic-cli.readthedocs.io/en/latest/).

### Relevant Pointers:

- Model catalog API for adding/modifying/deleting model metadata: [[REST API](https://api.models.mint.isi.edu/latest)] [[Code](https://github.com/mintproject/model-catalog-api)] [[Documentation](https://model-catalog-python-api-client.readthedocs.io/en/latest/endpoints/)] [[Releases](https://github.com/mintproject/model-catalog-api/releases)]
- GUI for exploring the contents of the model catalog: [[Application (GUI)](https://models.mint.isi.edu/home)] [[Video of the main features](https://www.youtube.com/watch?v=C9rxGT2k9is)]
- [Requires log in] GUI for configuring and editing models: [[Application](https://mint.isi.edu/ethiopia/models/configure)] [[Code](https://github.com/mintproject/mint-ui-lit)] [[Releases](https://github.com/mintproject/mint-ui-lit/releases)]
- Model services API client and examples: [[Code](https://github.com/mintproject/model-catalog-python-api-client/)] [[Documentation](https://model-catalog-python-api-client.readthedocs.io/en/latest/)] [[Releases](https://github.com/mintproject/model-catalog-python-api-client/releases)]
- Desktop appliation for model execution (dame) [[Code](https://github.com/mintproject/dame_cli/)] [Documentation](https://dame-cli.readthedocs.io/en/latest/)] [[Releases](https://github.com/mintproject/dame_cli/releases)]
- Model insertion checker (mic) [[Code](https://github.com/mintproject/mic)] [[Documentation](https://mic-cli.readthedocs.io/en/latest/)] [[Releases](https://github.com/mintproject/mic/releases)]

The API relies on the Software Description Ontology for Models  [https://w3id.org/okn/o/sdm](https://w3id.org/okn/o/sdm)

The MINT [Model Catalog API](https://api.models.mint.isi.edu/latest/ui/) supports:

- Get a list of all resources (Model, ModelVersion, Parameters, Inputs, Variables and other classes). For example: get all the models in MINT.
- Get the detailed information of a resource. For example: get the description of the model [Topoflow](https://dev.mint.isi.edu/south_sudan/models/explore/TOPOFLOW/topoflow_3.5/topoflow_cfg_simple/topoflow_cfg_simple_Guder)
- Create, updates and deletes resources on the Model Catalog. For example, create a new model, delete or update an existing model.
    
## Transformation Services
The [MINT Data Transformation System](https://data-trans.mint.isi.edu/)  provides a list of supported transformations that can be used to transform datasets into different formats, which may be required by different models.

The main idea of the transformation system is that we use smaller components (we refer to them as *adapters*) which we ’concatenate’ to form a transformation flow (a *pipeline*). This modular design allows us to reuse existing modules and wrap ready-scripts to create a language-and-format-independent module and pipeline.

The current supported transformations contains:
- Spatial Transformations: cropping, regirdding, resampling, etc.
- Model-specific Transformations: PIHM, Cycles, Econ, etc.
- General Transformations: joining, filtering, merging, etc.

### Common Data Representation

To make the transformation adapters work with datasets in different formats and layouts (e.g., CSV, NetCDF, Spreadsheet), we developed a library named D-REPR that reads the datasets into a common data representation. We choose to represent the data in RDF. Given a D-REPR model of a dataset, the D-REPR library can either virtually map the data to RDF or material the data. The library and its documentation is available [here](https://github.com/usc-isi-i2/d-repr)

### Relevant Pointers

- Code: [https://github.com/mintproject/MINT-Transformation](https://github.com/mintproject/MINT-Transformation)
- Portal: [https://data-trans.mint.isi.edu/](https://data-trans.mint.isi.edu/)
- Demo: [https://www.youtube.com/watch?v=tENwysxt3xI](https://www.youtube.com/watch?v=tENwysxt3xI)

### Identifying and Transforming Units of Measurement in Scientific Data

The library, called CCUT, uses grammar tools to automatically parse the different components in a unit found in textual data and map them to elements of a standard ontology called QUDT to form a structured semantic output. The output depicts the different relationships, attributes and semantics of units and allows users to have a better understanding of their data. The system also enables data transformations such as unit conversions.

### Relevant Pointers

- Code: [https://github.com/basels/ccut](https://github.com/basels/ccut)
- Python Package: [https://pypi.org/project/ccut/](https://pypi.org/project/ccut/)

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

The Scientific Variables Ontology Framework is a methodology for uniformly representing scientific variables. The required elements are an upper ontology consisting of a set of domain-independent categories and a set of design patterns for modular creation of complex variable representations. The customizable lower ontology can be populated with any collection of variables as necessitated by an application.

#### Relevant Pointers
- General SVO Website: [http://www.geoscienceontology.org/](http://www.geoscienceontology.org/)
- SVO Documentation: [http://www.geoscienceontology.org/svo/](http://www.geoscienceontology.org/svo/)
- Publicly available SVO code: [https://github.com/mariutzica/ScientificVariablesOntology](https://github.com/mariutzica/ScientificVariablesOntology)


## Remote Sensing
Access to observation data for calibration and validation is essential for building robust models. Earth Observation data from remote sensing satellites has the potential of providing this observation data especially in regions where ground observations are very scarce or completely absent. For example, the link below demonstrates how we are using satellite imagery to monitor river width changes in Ethiopia. 
[http://umnlcc.cs.umn.edu/river-width-demo/](http://umnlcc.cs.umn.edu/river-width-demo/)




