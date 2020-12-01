---
layout: page
title: MINT Project Releases
---

*Last updated: 2020-11-30*
## November, 2020
* Release the first version of an evaluation [dataset](https://drive.google.com/drive/u/1/folders/1ot6d4do1oLGXzAIIppx5j9ECDxzHkB-4) for Semantic Modeling that contains 500 Wikipedia Tables manually mapped to Wikidata.

## October, 2020
* Release of [B-Clean API](https://github.com/mintproject/byod-cleaning-api/tree/v0.4) v0.4 to support automatic data cleaning
  * Improve performance of deep learning model
  * Support user curation in active learning fashion
  * Provide datasets for system evaluation
* Release of the [Model Catalog 1.6.0](https://github.com/mintproject/ModelCatalog/releases/tag/v1.6.0)
  * Upgraded contents to [Software Description Ontology v1.8.0](https://w3id.org/okn/o/sd/1.8.0)  and [Software Description Ontology for Models v1.7.0](https://w3id.org/okn/o/sdm/1.7.0)
  * Fixed errors and data cleaning
  * Added new properties and model categories
  * Improved documentation and export/import process

## September, 2020
 * Release of [Data Transformation service v1.2]({{ '/products/data/' | absolute_url }}#transformation-services)
   * Now support CHIRPS dataset download with temporal and spatial cropping ([example](https://github.com/mintproject/MINT-Transformation/tree/master/examples/chirps)).
 * Release a [draft dataset](https://drive.google.com/drive/folders/1ot6d4do1oLGXzAIIppx5j9ECDxzHkB-4?usp=sharing) of ~1M semantic models of Wikipedia tables to Wikidata and an [UI](https://github.com/binh-vu/semantic-modeling-ui) to create and curate semantic models
 * Release of [MIC]({{ '/products/model/' | absolute_url }}#model-insertion-checker-mic) 1.3.4
    * [Changelog](https://github.com/mintproject/mic/releases/tag/1.3.4)
    * Bug fixes and tests (error in automated parameter detection, errors in hyphens in the main configuration, etc.)
  * Release of the [Software Description Ontology v1.8.0](https://w3id.org/okn/o/sd/1.8.0)
    * [Changelog](https://knowledgecaptureanddiscovery.github.io/SoftwareDescriptionOntology/release/1.8.0/index-en.html#changes)
    * Support for additional properties for describing results of a transformation.
  * Release of the [Software Description Ontology for Models v1.7.0](https://w3id.org/okn/o/sdm/1.7.0)
    * [Changelog](https://mintproject.github.io/Mint-ModelCatalog-Ontology/release/1.7.0/index-en.html#changes)
    * Suppot for model categories and description of coupled models.

## August, 2020
* Release of [B-Clean API](https://github.com/mintproject/byod-cleaning-api/tree/v0.3) v0.3 to support automatic data cleaning
  * Add deep learning model for few-shot data cleaning
* Applications of the TopoFlow hydrologic model:
  * Comparisons of TopoFlow model output to remote sensing time series.
  * Comparisons of TopoFlow model output to daily discharge data at gauges.
  * Improvements to the TopoFlow model calibration module.
  * New model runs with 6-hourly CHIRPS rainfall data.
  * Improvements to TopoFlow Jupyter notebooks.
  * Testing of MIC with the TopoFlow model.
  * New script to auto-generate TopoFlow visualizations.
* Release of [MIC]({{ '/products/model/' | absolute_url }}#model-insertion-checker-mic) 1.3.3
  * [Changelog](https://github.com/mintproject/mic/releases/tag/1.3.3)
  * Bug fixes (errors in Windows executions, errors with double quotes in parameters)


## July, 2020

* Release of [MIC]({{ '/products/model/' | absolute_url }}#model-insertion-checker-mic) 1.3.1
  * [Changelog](https://github.com/mintproject/mic/releases/tag/1.3.1)
  * Better capture of dependencies (starting from own image, committing image after user edits)
  * Auto-detection of parameters and inputs when encapsulating component.
  * Support for uploading data transformations.
  * Usability bugs and testing
  * Improved documentation
* Release of [DAME]({{ '/products/model/' | absolute_url }}#desktop-appliation-for-model-execution-dame) 5.3.1
  * [Changelog](https://github.com/mintproject/dame_cli/releases/tag/5.3.1)
  * Improve errors in singularity image detection and minor bugs
  * Users can execute data transformations from DAME.
* Release of [Model Catalog API]({{ '/products/model/' | absolute_url }}#model-catalog-api) 1.5.0
  * [Changelog](https://github.com/mintproject/ModelCatalog/releases/tag/v1.5.0)
  * Model description fixes, improved model export functionality.
* Release of [CCUT-Wrapper](https://github.com/basels/ccut-wrapper) 1.0.0
  * We are releasing a beta version of the wrapper UI for [CCUT 1.0.0](https://pypi.org/project/ccut/). This is an interactive web application that suggests semantic types for units of measurement, supports their transformations, and allows working with spreadsheet files.
* Release of [B-Clean API](https://github.com/mintproject/byod-cleaning-api) v0.2 to support automatic data cleaning
  * Increase training data: include ~1M web tables with ~7M attributes and ~200M cell values.
  * Support outlier detection based on n-gram uncommonness instead of whole string uncommonness 
* Release of [Semantic Modeling API](https://github.com/mintproject/semantic-modeling-api) v0.2
  * The new model leverages available data on Wikidata and WebTables to improve performance on domains with little training data
* Release of new Jupyter Notebook for the TopoFlow model, and updates to existing notebooks and underlying code:
    * Troubleshooting large discrepancies between the GLDAS and GPM rainfall datasets (TopoFlow input data)
    * Calibration with new daily discharge data for the Baro River at Masha.
    * New: [TopoFlow_Calibration_Baro_at_Masha](https://github.com/peckhams/topoflow36/blob/master/notebooks/TopoFlow_Calibration_Baro_at_Masha.ipynb)
    * Update: [TopoFlow Calibration Remote Sensing](https://github.com/peckhams/topoflow36/blob/master/notebooks/TopoFlow_Calibration_Remote_Sensing.ipynb)
    * Update: [TopoFlow Water Scarcity](https://github.com/peckhams/topoflow36/blob/master/notebooks/TopoFlow_Water_Scarcity_Demo.ipynb)

## June, 2020
* Release of [B-Clean API](https://github.com/mintproject/byod-cleaning-api) v0.1 to support automatic data cleaning
  * Added Web API for [outlier detection](https://bclean.mint.isi.edu/detect).
  * Added [Jupyter notebook](https://github.com/mintproject/byod-cleaning-api/blob/master/ocde_demo.ipynb) to interact with service.
* Release of [Semantic Modeling API](https://github.com/mintproject/semantic-modeling-api) v0.1 to support automatic data modeling
  * Added Web API for [source modeling](http://mira.isi.edu:8000).
  * Added [Jupyter notebook](https://github.com/mintproject/semantic-modeling-api/blob/master/demo.ipynb) to interact with service.
* Release of [DAME]({{ '/products/model/' | absolute_url }}#desktop-appliation-for-model-execution-dame) 5.2.0
  *  [Changelog](https://github.com/mintproject/dame_cli/releases/tag/5.1.1)
  *  Added changes so users can specify their own parameter values instead of defaults.
* Release of [MIC]({{ '/products/model/' | absolute_url }}#model-insertion-checker-mic) 1.0.0
  * [Changelog](https://github.com/mintproject/mic/releases/tag/1.0.0)
  * Now users can start from their model folder (no requirements for data organization)
  * Automatic detection the framework/language used by the model component (python, conda, java, general)
  * Automated extraction of dependencies according to the framework/language (pip is supported)
  * Creation a Linux environment using Docker
  * MIC can now trace commands and automatically detect configuration files, inputs and outputs

* Release of [riverwidthEO version 1.2](https://github.com/mintproject/riverwidthEO)
  * updated the classification model by adding ~3,000 labeled and 90,000 unlabeled images.
  
* Release of [River Segment Surface Area Dataset version 1.2](https://mint.isi.edu/ethiopia/datasets/browse/da6b6d47-7672-4e6e-a455-7bbc7e7ceb99) for Ethiopia
  * updated the results for all of Ethopia using the updated model. 

* Release of two new Jupyter Notebooks for the TopoFlow model, and updates to several existing notebooks:
    * New: [TopoFlow Calibration Remote Sensing](https://github.com/peckhams/topoflow36/blob/master/notebooks/TopoFlow_Calibration_Remote_Sensing.ipynb)
    * New: [TopoFlow Water Scarcity](https://github.com/peckhams/topoflow36/blob/master/notebooks/TopoFlow_Water_Scarcity_Demo.ipynb)
    * Update: [TopoFlow Rainfall Inputs](https://github.com/peckhams/topoflow36/blob/master/notebooks/TopoFlow_Rainfall_Inputs.ipynb)
    * Update: [TopoFlow Flood Modeling](https://github.com/peckhams/topoflow36/blob/master/notebooks/TopoFlow_Flood_Modeling.ipynb)
    * Update: [TopoFlow Calibration Gauge Data](https://github.com/peckhams/topoflow36/blob/master/notebooks/TopoFlow_Calibration_Gauge_Data.ipynb) 
    * Update: [TopoFlow Getting Started](https://github.com/peckhams/topoflow36/blob/master/notebooks/TopoFlow_Getting_Started.ipynb) 
    * Update: [TopoFlow Prepare_Input_Data](https://github.com/peckhams/topoflow36/blob/master/notebooks/TopoFlow_Prepare_Input_Data.ipynb)
    * Update: [TopoFlow Visualization](https://github.com/peckhams/topoflow36/blob/master/notebooks/TopoFlow_Visualization.ipynb)
 
## May, 2020
* Release of [DSI](https://github.com/mintproject/droughtIndices) v1.1.0
  * [Changelog](https://github.com/mintproject/droughtIndices/releases/tag/1.1.0)
  * Configuration of the model using a JSON file
  * Add support to ECMWF
  * Add support to run globally
  * Improve compatibility with xarray (performance improvement)

* Release of [DAME]({{ '/products/model/' | absolute_url }}#desktop-appliation-for-model-execution-dame) 5.1.1
  * [Changelog](https://github.com/mintproject/dame_cli/releases/tag/5.1.1)
  * Run models using local data
  * Configure with custom ModelCatalog or user
  * Support Docker on Windows, Linux and macOS (Beta)
  * Validation of URLs
  * List and show model configurations and setups
  * Integration of data transformations for TopoFlow Data (Weather)

* New release of [MIC]({{ '/products/model/' | absolute_url }}#model-insertion-checker-mic) 0.4.1 - ALPHA
  * End-to-end encapsulation of model components.
  * Provides templates for creating components.
  * Enables testing through Docker images (locally)
  * Create a snapshot of a model component, saving code in GitHub and Docker image in DockerHub.
  * After testing, pushes changes to model catalog.
  
* Release of [Data Transformation service v1.1]({{ '/products/data/' | absolute_url }}#transformation-services)
  * Support data streaming 
  * Add new pipeline/adapters to support [GLDAS2Cycles transformation](https://github.com/mintproject/MINT-Transformation/wiki/Transformation-Adapters#3--gldas2cyclesfunc)
  * Add new pipeline/adapters to support [variable aggregation in GLDAS data by both time and woreda](https://github.com/mintproject/MINT-Transformation/tree/master/examples/aggregation)
  * Design a procedure to quickly [import external transformation libraries](https://github.com/mintproject/MINT-Transformation/wiki/Importing-External-Transformations) (e.g. Topoflow transformation notebooks)

* Release of [riverwidthEO version 1.1](https://github.com/mintproject/riverwidthEO)
  * updated the methodology to detect cloudy pixels.
  * updated the methodology to use clustering and classification together to handle hazy images (that are missed by cloud filters)
  * updated the classification model by adding more training images.
  
* Release of [River Segment Surface Area Dataset version 1.1](https://mint.isi.edu/ethiopia/datasets/browse/da6b6d47-7672-4e6e-a455-7bbc7e7ceb99) for Ethiopia
  * updated the results for 5 basins in Ethopia using the updated model. 

* Release of three new Jupyter Notebooks for the TopoFlow model, and three updates to existing notebooks:
    * New: [TopoFlow Rainfall Inputs](https://github.com/peckhams/topoflow36/blob/master/notebooks/TopoFlow_Rainfall_Inputs.ipynb)
    * New: [TopoFlow Flood Modeling](https://github.com/peckhams/topoflow36/blob/master/notebooks/TopoFlow_Flood_Modeling.ipynb)
    * New: [TopoFlow Calibration Gauge Data](https://github.com/peckhams/topoflow36/blob/master/notebooks/TopoFlow_Calibration_Gauge_Data.ipynb) 
    * Update: [TopoFlow Getting Started Notebook](https://github.com/peckhams/topoflow36/blob/master/notebooks/TopoFlow_Getting_Started.ipynb) 
    * Update: [TopoFlow Prepare Input Data](https://github.com/peckhams/topoflow36/blob/master/notebooks/TopoFlow_Prepare_Input_Data.ipynb)
    * Update: [TopoFlow Visualization](https://github.com/peckhams/topoflow36/blob/master/notebooks/TopoFlow_Visualization.ipynb)
    
* Release of notebook and Python tools for performing scientific variable exploration and grounding to Scientific Variables Ontology (SVO) variables and entries in the World Modelers Indicators (WMI) list:
    * New: [Scientific Variable Exploration and Grounding](https://github.com/mariutzica/Scientific-Variable-Exploration-Tools/blob/master/Variable%20Report.ipynb)
    
## April, 2020
* Release of [DAME]({{ '/products/model/' | absolute_url }}#desktop-appliation-for-model-execution-dame) 4.1.3
  * [Changelog](https://github.com/mintproject/dame_cli/releases/tag/4.1.3)
  * Additional testing and bug fixes (Testing in OSX and Unix). DAME will ask for missing parameters and inputs, using defaults when provided.
  * Improvements to messages and logging in the UI. Now the singularity commands, inputs and Docker images are displayed, in case users want to execute models with their own means.
  * Improved documentation and examples
* Initial release of [MIC]({{ '/products/model/' | absolute_url }}#model-insertion-checker-mic) 0.2.0 - ALPHA
  * [Code](https://github.com/mintproject/mic/releases/tag/0.2.0)
  * Users can define and insert an initial subset of metadata about new models.
  * First BETA [release of mic documentation](https://mic-cli.readthedocs.io/en/latest/)
* Release of [Data Transformation service v1.0]({{ '/products/data/' | absolute_url }}#transformation-services)
  * Users can run the transformation pipeline through CLI, web service or Docker.
    * [Instructions](https://github.com/mintproject/MINT-Transformation) 
  * Release predefined pipelines in form of configuration files for:
    * Model-specific transformations: [Topoflow](https://github.com/mintproject/MINT-Transformation/wiki/Transformation-Adapters)
* Release of [MINT-Data-Sync](https://github.com/mintproject/MINT-Data-Sync) system
  * Monitor when new GLDAS data files become available, upload them to MINT Data Server, and register them in MINT Data Catalog
* Release of [River Segment Surface Area Dataset version 1.0](https://mint.isi.edu/ethiopia/datasets/browse/da6b6d47-7672-4e6e-a455-7bbc7e7ceb99) for Ethiopia
  * Processed 8710 river segments (covering all of Ethiopia) using machine learning algorithms and satellite imagery to create surface area timeseries.
  * Uses Sentinel-2 imagery available from December 2015 until March 2020. 
  * A csv with surface area timeseries for each river segment is available for download from the MINT Data Catalog. 
* Release of [riverwidthEO version 1.0](https://github.com/mintproject/riverwidthEO)
  * A python package that processes river segments using machine learning algorithms and satellite imagery (Sentinel-2) to create surface area timeseries (delivered as a csv file).
  * Uses descarteslabs API to download data for any given segment.
  * Provides user with options to provide points on a river as input or just provide a region or country to select predefined points on the river. These predefined points are available for rivers (>100 meters in width) across the globe. 
* Release of a [Jupyter Notebook for the TopoFlow model](/notebooks.html##jupyter-notebooks-for-use-with-the-topoflow-model) with an overview and introduction to new users
    * [TopoFlow Getting Started Notebook](https://github.com/peckhams/topoflow36/blob/master/notebooks/TopoFlow_Getting_Started.ipynb) 

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

