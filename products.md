---
layout: page
title: MINT Services and Software
date: 2020-04-28T10:20:00Z
---

This document provides links to public MINT components (UIs, APIs, services, and data and software releases) and a summary of their documentation and specifications.

Each of the components is evolving.  The [release page]({{ '/releases.html' | absolute_url }}) contains announcements about new versions.



## MINT User Interface

The MINT user interface (UI) assists a user to easily integrate sophisticated simulation models and data to explore the effects of weather and climate in water on food availability in a given region.  Using the MINT UI requires a user login.  The implementation of the MINT UI is based on  the services described below. 

See an overview and more details in the [MINT UI main page]({{ '/products/mint' | absolute_url }}).


## Model Services

The MINT Model Services provides detailed information about software models and metadata available in MINT. 
We provide multiple services to interact with the MINT Model Catalog.

- [Model Catalog API]({{ '/products/model/' | absolute_url }}#model-catalog-api) for adding/modifying/deleting model metadata. 
- [Model Catalog Explorer]({{ '/products/model/' | absolute_url }}#model-catalog-explorer) is graphical user interface (GUI) for exploring the contents of the model catalog. Also, a registered user can add, edit, and remove their Model Configuration Setups.
- [Model Insertion CLI (MIC)]({{ '/products/model/' | absolute_url }}#model-insertion-checker-mic) is a command-line interface for adding models on a Model Catalog Service using the [Model Catalog API](#model-catalog-api)
- [Desktop Application for Model Execution (DAME)]({{ '/products/model/' | absolute_url }}#desktop-appliation-for-model-execution-dame) obtains the details about the models using MINT Model Catalog API and run it in your computer.
- [Clients]({{ '/products/model/' | absolute_url }}#model-service-api-clients) are provided to interact with [Model Catalog API]({{ '/products/model/' | absolute_url }}#model-catalog-api) easily.

See an overview and more details in the [MINT Model Services main page]{{ '/products/model' | absolute_url }}.

## Data Services

The MINT Data Services provides access to a curated collection of datasets. Each dataset is a logical grouping of data about specific variables contained in one or more resources or files.

- The [MINT Data Catalog]({{ '/products/data' | absolute_url }}#mint-data-catalog) provides access to a curated collection of a datasets in the MINT Data Catalog.
- The [MINT Data Transformation System]({{ '/products/data' | absolute_url }}#transformation-services)  provides a list of supported transformations that can be used to transform datasets into different formats, which may be required by different models.

See an overview and more details in the [MINT Data Services main page]{{ '/products/data' | absolute_url }}.

## Execution Services

The MINT Execution Services support the execution of single models and model ensembles from the [MINT-UI]{{ '/products/' | absolute_url }}.

- The [MINT Emulator API]({{ '/products/execution' | absolute_url }}#emulator-apis) provides access to model executions a curated collection of a datasets in the MINT Data Catalog.
- The [MINT  Ensemble Manager API]({{ '/products/execution' | absolute_url }}#ensemble-manager-api)  provides a list of supported transformations that can be used to transform datasets into different formats, which may be required by different models.

## Other services

- [The Scientific Variables Ontology Framework]{{ '/products/other' | absolute_url }} is a methodology for uniformly representing scientific variables.

- [Unique datasets extracted from remote sensing data]{{ '/products/other' | absolute_url }} for calibration and validation of models.
