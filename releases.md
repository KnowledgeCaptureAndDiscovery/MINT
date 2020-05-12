---
layout: page
title: MINT Release updates
---

*Last updated: 2020-05-05*

## May, 2020
* Release of [DAME]({{ '/products/model/' | absolute_url }}#desktop-appliation-for-model-execution-dame) 5.0.0
  * [Changelog](https://github.com/mintproject/dame_cli/releases/tag/5.0.0)
  * Run models using local data
  * Configure with custom ModelCatalog or user
  * Support Docker on Windows, Linux and macOS (Beta)
  * Validation of URLs
  * List and show model configurations and setups


## April, 2020
* Release of [DAME]({{ '/products/model/' | absolute_url }}#desktop-appliation-for-model-execution-dame) 4.1.3
  * [Changelog](https://github.com/mintproject/dame_cli/releases/tag/4.1.3)
  * Additional testing and bug fixes (Testing in OSX and Unix). DAME will ask for missing parameters and inputs, using defaults when provided.
  * Improvements to messages and logging in the UI. Now the singularity commands, inputs and Docker images are displayed, in case users want to execute models with their own means.
  * Improved documentation and examples
* Initial release of [MIC]({{ '/products/model/' | absolute_url }}#model-insertion-checker-mic) 0.2.0
  * [Code](https://github.com/mintproject/mic/releases/tag/0.2.0)
  * Users can define and insert new models and model configurations.
  * Users can define input/outputs/parameters of model configurations.
  * First [release of mic documentation](https://mic-cli.readthedocs.io/en/latest/)
* Release of [Data Transformation services]({{ '/products/data/' | absolute_url }}#transformation-services) system
  * Users can run the transformation pipeline through CLI, web service or Docker.
    * [Instructions](https://github.com/mintproject/MINT-Transformation)
  * Release predefined pipelines in form of configuration files for
    * Model-specific transformations: [Topoflow](https://github.com/mintproject/MINT-Transformation/blob/master/examples/topoflow4/topoflow_climate.yml)
    * Spatial transformations: [Cropping](https://github.com/mintproject/MINT-Transformation/blob/master/examples/cropping_weather_dataset.yml)
* Release of [MINT-Data-Sync](https://github.com/mintproject/MINT-Data-Sync) system
  * Monitor when new GLDAS data files become available, upload them to MINT Data Server, and register them in MINT Data Catalog
* Release of [riverwidthEO version 1.0](https://github.com/mintproject/riverwidthEO)
  * Process river segments using machine learning algorithms and satellite imagery (Sentinel-2) to create surface area timeseries.
  * Uses descarteslabs API to download data for any given segment.
  * Provides user with options to provide points on a river as input or just provide a region or country to select predefined points on the river. These predefined points are available for rivers (>100 meters in width) across the globe. 
* Initial release of [River Segment Surface Area Dataset version 1.0](https://mint.isi.edu/ethiopia/datasets/browse/da6b6d47-7672-4e6e-a455-7bbc7e7ceb99) for Ethiopia
  * process ~10,000 river segments (covering all of Ethiopia) using machine learning algorithms and satellite imagery to create surface area timeseries.
  * uses Sentinel-2 imagery from available from Dec-2015 till Mar-2020. 
  * a csv for each river segment will be available for download from the data catalog. 
* Release of a [Jupyter Notebook for the TopoFlow model](/notebooks.html##jupyter-notebooks-for-use-with-the-topoflow-model) with an overview and introduction to new users
    * [TopoFlow Getting Started Notebook](https://github.com/peckhams/topoflow36/blob/master/TopoFlow_Getting_Started.ipynb) 

## March, 2020

* Release of [MINT-UI 4.3.4]({{ '/products/mint/' | absolute_url }})
    * [Changelog](https://github.com/mintproject/mint-ui-lit/releases/tag/4.3.4)
    * Users can run their ModelConfigurations
* Release of [DAME]({{ '/products/model/' | absolute_url }}#desktop-appliation-for-model-execution-dame) 3.3.0
    * [Changelog](https://github.com/mintproject/dame_cli/releases/tag/3.3.0)
    * Execute models from MINT on Desktop/Server
* Release of [Model Catalog API]({{ '/products/model/' | absolute_url }}#model-catalog-api) 1.4.0
    * [Changelog](https://github.com/mintproject/ModelCatalog/releases/tag/v1.4.0)
    * Users can insert their ModelConfigurations
    
## February, 2020

* Release of [MINT-UI 4.3.0]({{ '/products/mint/' | absolute_url }}) (Feb 26)
    * [Changelog](https://github.com/mintproject/mint-ui-lit/releases/tag/4.3.0)
* Release of [MINT-UI 4.2.1]({{ '/products/mint/' | absolute_url }})) (Feb 19)
    * [Changelog](https://github.com/mintproject/mint-ui-lit/releases/tag/4.2.1)
* Release of [MINT-UI 4.2.0]({{ '/products/mint/' | absolute_url }})) (Feb 14)
    * [Changelog](https://github.com/mintproject/mint-ui-lit/releases/tag/4.2.0)
* Release of [MINT-UI 4.1.0]({{ '/products/mint/' | absolute_url }})(https://mint.isi.edu/)
    * Fixing bugs and usability improvements [Release Release 4.1.0 · mintproject/mint-ui-lit](https://github.com/mintproject/mint-ui-lit/releases/tag/4.1.0)

## January, 2020
* Release of [MINT-UI 4.0.0]({{ '/products/mint/' | absolute_url }})
    * Bug fixes and usability improvements [Release Release 4.0.0-0 · mintproject/mint-ui-lit](https://github.com/mintproject/mint-ui-lit/releases/tag/4.0.0-0)

## December, 2019

#### MINT Data Catalog

*   Releases of MINT Data Catalog UI
    *   It is now possible to browse MINT Data Catalog from a [browser](https://data-catalog.mint.isi.edu/)
    *   You can view API documentation [here](https://data-catalog.mint.isi.edu/documentation)
*   MINT Data Catalog [Github repository](https://github.com/mintproject/MINT-DataCatalog-Public). Specifically,
    *   Interactive [Jupyter notebook](https://mybinder.org/v2/gh/mintproject/MINT-DataCatalog-Public/master?filepath=%2Fdemo%2Fapi_demo.ipynb) that showcases Data Catalog API
    *   More information on [Resources](https://github.com/mintproject/MINT-DataCatalog-Public/blob/master/docs/resources.md)
    *   More information on [Variables](https://github.com/mintproject/MINT-DataCatalog-Public/blob/master/docs/variables.md)
    *   [Issue tracker and feature requests](https://github.com/mintproject/MINT-DataCatalog-Public/issues)
    *   [Linking](https://github.com/mintproject/MINT-DataCatalog-Public/issues/new/choose) variable names to Standard Variable Ontology (SVO)

#### MINT Model Catalog:

* Release [1.3.0](https://api.models.mint.isi.edu/v1.3.0/ui/):
    *   Update to use [the Software Description Ontology v1.4.0](https://w3id.org/okn/o/sd/1.4.0)    
    *   Add custom SPARQL queries

### Ensemble Manager API

* Release [1.0.0](https://ensemble.mint.isi.edu/v1/api-docs):
    * Execute models using singularity
    * Include parallelism option in config to do multiple model runs
    * Adding DELETE request to executions
    * Local delete for cache of execution

#### Ingestion API:

* Release [1.1.0](https://ingestion.mint.isi.edu/v1.1.0/ui):
    * Take model execution data and ingest into a database to enable interactive dashboards
    * Gather model ensemble execution results
    
## November, 2019

#### MINT NetCDF Convention

*   Release of MINT NetCDF convention
    *   We propose a self-describing data format for structured gridded datasets for MINT data catalog and visualization based on the NetCDF and the CF convention. Check [here](https://github.com/mintproject/MINT-NetCDF-Convention) for the lastest document. Please open new issues on [GitHub](https://github.com/mintproject/MINT-NetCDF-Convention/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc) or on [Google doc](https://docs.google.com/spreadsheets/d/1eT_Z51R4VwVen-qx7XGtNjoHuc2sMlYmmxbi5acumx0/edit#gid=0) for comments.
*   Release of MINT-GeoViz
    *   We are releasing the v1 of MINT-GeoViz, an interactive visualization library for large geospatial datasets that follow MINT NetCDF convention. Check out this [GitHub repo](https://github.com/mintproject/MINT-GeoViz/tree/master?) for more details.
    *   Check out our full [demo](https://drive.google.com/drive/folders/1t9E5HsUOre0CgAevkdRAxgaRQghJ_i2v?usp=sharing) and [notebook examples](https://github.com/mintproject/MINT-GeoViz/tree/master/examples/notebooks) on how to use the library

## October, 2019

#### Data Catalog


*   Release of D-REPR: a library for reading heterogeneous datasets into common representations. Check its [GitHub](https://github.com/usc-isi-i2/d-repr) for more information.


## May, 2019

#### Model Catalog


*   New content: The MINT model catalog has been expanded to include a semantic representation of units, scientific variables and links to Wikidata. Check the [release on GitHub](https://github.com/mintproject/ModelCatalog/releases) for more information.
*   New APIs for adding content: We have expanded our APIs with a new client based on Open API that allows anyone to insert models in the model catalog. The API is accessible in the following link: [https://api.models.mint.isi.edu/v0.0.2/ui/#/](https://api.models.mint.isi.edu/v0.0.2/ui/#/)
*   New APIs for accessing content: 3 new methods have been added to our [GRLC API](https://query.mint.isi.edu/api/mintproject/MINT-ModelCatalogQueries#/). The first one, to obtain additional information of a Scientific Variable given its label (getStandardVariableMetadata). The other two (getInputCompatibleConfig) and (getOutputCompatibleConfig) retrieve those models or software compatible with a target model. This facilitates understanding which software has variables that may interoperate with other software.
*   A new client for accessing content: With our new Python client, now it is possible to access the content in the model catalog without having to issue SPARQL queries or API queries. [Check it out here](https://github.com/mintproject/MINT-ModelCatalogAPI-client).
*   New examples: Check out our [notebook](https://github.com/mintproject/MINT-ModelCatalogAPI-client/blob/master/notebook-example-how-to-use.ipynb) for examples on how to use the client.
*   The [Model Explorer](https://dev.models.mint.isi.edu) has been updated to show the contents of models in a more user-friendly manner. Check [here](https://dev.models.mint.isi.edu) the latest version. Please [open new issues on GitHub](https://github.com/mintproject/MINT-ModelCatalogExplorer/issues/new) if you find bugs.

