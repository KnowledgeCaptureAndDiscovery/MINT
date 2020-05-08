---
layout: page
title: MINT Services and Software
date: 2020-04-28T10:20:00Z
---

This document provides links to public MINT products (APIs, software, data and services) and a summary of the documentation and specifications available.



## MINT User Interface

MINT assists an analyst to easily use sophisticated simulation models and data in order to explore the role of weather and climate in water on food availability in select regions of the world. 

To do that, the service interacts with the [Model](#model-services), [Data](#data-services) and [Execution](#execution-services) Services

More information: [MINT User Interface]({{ '/services/mintui.html' | absolute_url }})


## Model Services

The [MINT Model Catalog](#model-catalog-api) provides detailed information about software models and metadata available in MINT. 
We provide multiple services to interact with the MINT Model Catalog.

- [Model Catalog API]({{ '/products/model/' | absolute_url }}#model-catalog-api) for adding/modifying/deleting model metadata. 
- [Model Catalog Explorer]({{ '/products/model/' | absolute_url }}#model-catalog-explorer) is graphical user interface (GUI) for exploring the contents of the model catalog. Also, a registered user can add, edit, and remove their Model Configuration Setups.
- [Model Insertion CLI (MIC)]({{ '/products/model/' | absolute_url }}#model-insertion-checker-mic) is a command-line interface for adding models on a Model Catalog Service using the [Model Catalog API](#model-catalog-api)
- Desktop Application for Model Execution (DAME) obtains the details about the models using MINT Model Catalog API and run it in your computer.
- [Clients]({{ '/products/model/' | absolute_url }}#model-service-api-clients) are provided to interact with [Model Catalog API]({{ '/products/model/' | absolute_url }}#model-catalog-api) easily.


More information: [Model Services]({{ '/services/model.html' | absolute_url }})

## Data Services

The [MINT Data Catalog]({{ '/services/data.html' | absolute_url }}) access to a curated collection of a datasets in the MINT Data Catalog.

More information: [Data Services]({{ '/services/dats.html' | absolute_url }})

## Execution Services

The [Execution Services]({{ '/services/execuion.html' | absolute_url }}) provides 

More information: [Data Services]({{ '/services/dats.html' | absolute_url }})

## Release Page

Each product is evolving, the [release page]({{ '/releases.html' | absolute_url }}) contains announcements about new versions.




