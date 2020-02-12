---
layout: page
title: MINT Release updates
---

*Last updated: 2019-12-19*

## February, 2020

* Release MINT-UI 4.1.0
    * Fixing bugs and usability improvements [Release Release 4.1.0 · mintproject/mint-ui-lit](https://github.com/mintproject/mint-ui-lit/releases/tag/4.1.0)

## January, 2020
* Release MINT-UI 4.0.0
    * Fixing bugs and usability improvements [Release Release 4.0.0-0 · mintproject/mint-ui-lit](https://github.com/mintproject/mint-ui-lit/releases/tag/4.0.0-0)

## December, 2019

#### MINT Data Catalog

*   Release of MINT Data Catalog UI
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


#### Ingestion API:

* Release [1.1.0](https://ingestion.mint.isi.edu/v1.1.0/ui):
    * Gather model ensemble execution results

### Ensemble Manager API

* Release [1.0.0](https://ensemble.mint.isi.edu/v1/api-docs):
    * Execute models using singularity
    * Include parallelism option in config
    * Adding DELETE request to executionsLocal to delete cache of execution

## November, 2019

#### MINT NetCDF


*   Release of MINT NetCDF convention
    *   We propose a self-describing data format for structured gridded datasets for MINT data catalog and visualization based on the NetCDF and the CF convention. Check [here](https://github.com/mintproject/MINT-NetCDF-Convention) for the lastest document. Please open new issues on [GitHub](https://github.com/mintproject/MINT-NetCDF-Convention/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc) or on [Google doc](https://docs.google.com/spreadsheets/d/1eT_Z51R4VwVen-qx7XGtNjoHuc2sMlYmmxbi5acumx0/edit#gid=0) for comments.
*   Release of MINT-GeoViz
    *   We are releasing the v1 of MINT-GeoViz, an interactive visualization library for large geospatial datasets that follow MINT NetCDF convention. Check out this [GitHub repo](https://github.com/mintproject/MINT-GeoViz/tree/master?) for more details.
    *   Check out our full [demo](https://drive.google.com/drive/folders/1t9E5HsUOre0CgAevkdRAxgaRQghJ_i2v?usp=sharing) and [notebook examples](https://github.com/mintproject/MINT-GeoViz/tree/master/examples/notebooks) on how to use the library

## October, 2019

#### Data Catalog


*   Release D-REPR: a library for reading heterogeneous datasets into common representations. Check its [GitHub](https://github.com/usc-isi-i2/d-repr) for more information.


## May, 2019

#### Model Catalog


*   New content: The MINT model catalog has been expanded to include a semantic representation of units, scientific variables and links to Wikidata. Check the [release on GitHub](https://github.com/mintproject/ModelCatalog/releases) for more information.
*   New APIs for adding content: We have expanded our APIs with a new client based on Open API that allows anyone to insert models in the model catalog. The API is accessible in the following link: [https://api.models.mint.isi.edu/v0.0.2/ui/#/](https://api.models.mint.isi.edu/v0.0.2/ui/#/)
*   New APIs for accessing content: 3 new methods have been added to our [GRLC API](https://query.mint.isi.edu/api/mintproject/MINT-ModelCatalogQueries#/). The first one, to obtain additional information of a Scientific Variable given its label (getStandardVariableMetadata). The other two (getInputCompatibleConfig) and (getOutputCompatibleConfig) retrieve those models or software compatible with a target model. This facilitates understanding which software has variables that may interoperate with other software.
*   A new client for accessing content: With our new Python client, now it is possible to access the content in the model catalog without having to issue SPARQL queries or API queries. [Check it out here](https://github.com/mintproject/MINT-ModelCatalogAPI-client).
*   New examples: Check out our [notebook](https://github.com/mintproject/MINT-ModelCatalogAPI-client/blob/master/notebook-example-how-to-use.ipynb) for examples on how to use the client.
*   The [Model Explorer](https://dev.models.mint.isi.edu) has been updated to show the contents of models in a more user-friendly manner. Check [here](https://dev.models.mint.isi.edu) the latest version. Please [open new issues on GitHub](https://github.com/mintproject/MINT-ModelCatalogExplorer/issues/new) if you find bugs.

