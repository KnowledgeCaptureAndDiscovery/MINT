---
permalink: "/products/data/"
layout: page
title:  "Data Services"
---

### MINT Data Catalog

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

#### Relevant Pointers
- Code: [https://github.com/mintproject/MINT-DataCatalog-Public](https://github.com/mintproject/MINT-DataCatalog-Public)
- Portal: [https://data-catalog.mint.isi.edu](https://data-catalog.mint.isi.edu)


    
### Transformation Services
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
- Wrapper Web UI for the CCUT API service: [https://github.com/basels/ccut-wrapper](https://github.com/basels/ccut-wrapper)
