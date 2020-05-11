---
permalink: "/products/execution/"
layout: page
title:  "Execution Management Services"
---


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