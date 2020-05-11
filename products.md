---
layout: page
title: MINT Services and Software
date: 2020-04-28T10:20:00Z
---

This document provides links to public MINT products (APIs, software, data and services) and a summary of the documentation and specifications available.



## MINT User Interface

[MINT User Interface]({{ '/products/mint' | absolute_url }}) assists an analyst to easily use sophisticated simulation models and data in order to explore the role of weather and climate in water on food availability in select regions of the world. 

To do that, the [MINT User Interface]({{ '/products/mint' | absolute_url }}) interacts with the [Model](#model-services), [Data](#data-services) and [Execution](#execution-services) Services


## Model Services

The MINT Model Services provides detailed information about software models and metadata available in MINT. 
We provide multiple services to interact with the MINT Model Catalog.

- [Model Catalog API]({{ '/products/model/' | absolute_url }}#model-catalog-api) for adding/modifying/deleting model metadata. 
- [Model Catalog Explorer]({{ '/products/model/' | absolute_url }}#model-catalog-explorer) is graphical user interface (GUI) for exploring the contents of the model catalog. Also, a registered user can add, edit, and remove their Model Configuration Setups.
- [Model Insertion CLI (MIC)]({{ '/products/model/' | absolute_url }}#model-insertion-checker-mic) is a command-line interface for adding models on a Model Catalog Service using the [Model Catalog API](#model-catalog-api)
- [Desktop Application for Model Execution (DAME)]({{ '/products/model/' | absolute_url }}#desktop-appliation-for-model-execution-dame) obtains the details about the models using MINT Model Catalog API and run it in your computer.
- [Clients]({{ '/products/model/' | absolute_url }}#model-service-api-clients) are provided to interact with [Model Catalog API]({{ '/products/model/' | absolute_url }}#model-catalog-api) easily.



[Model Services - Overview ]({{ '/products/model' | absolute_url }}) shows the interaction of these services.

## Data Services

The MINT Data Catalog is a system that provides a curated collection of datasets. Each dataset is a logical grouping of data about specific variables contained in one or more resources.

- The [MINT Data Catalog]({{ '/products/data' | absolute_url }}#mint-data-catalog) provides access to a curated collection of a datasets in the MINT Data Catalog.
- The [MINT Data Transformation System]({{ '/products/data' | absolute_url }}#transformation-services)  provides a list of supported transformations that can be used to transform datasets into different formats, which may be required by different models.


## Execution Services

The MINT Execution Services allow the [MINT-UI]({{ '/products/' | absolute_url }}#mint-user-interface) to run models on servers. And store, and gather the results.

- The [MINT Emulator API]({{ '/products/execution' | absolute_url }}#emulator-apis) access to a curated collection of a datasets in the MINT Data Catalog.
- The [MINT  Ensemble Manager API]({{ '/products/execution' | absolute_url }}#ensemble-manager-api)  provides a list of supported transformations that can be used to transform datasets into different formats, which may be required by different models.

## Other services

- [The Scientific Variables Ontology Framework]({{ '/products/other' | absolute_url }}) is a methodology for uniformly representing scientific variables.
- [Remote Sensing access](({{ '/products/other' | absolute_url }})) to observation data for calibration and validation is essential for building robust models.

## Release Page

Each product is evolving, the [release page]({{ '/releases.html' | absolute_url }}) contains announcements about new versions.




