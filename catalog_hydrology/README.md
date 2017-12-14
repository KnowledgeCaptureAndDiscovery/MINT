## Scrapper for extracting hydrology information

We are going to use two sources:


1. **Africa Groundwater Atlas** 
  The successful and sustainable development of groundwater resources in Africa is critical for future safe water supplies, economic  growth and food security in the continent. Doing this successfully relies on good hydrogeological understanding - but much of the data and information that already exists about groundwater in Africa is not available to the people who could make use of it. Information freely accessible and it can be accessed online by following the link: [earthwise](http://earthwise.bgs.ac.uk/index.php/Hydrogeology_by_country) 

* **"earthewise_scrapper.py"** extracts automatically the details ( authors, citation, reference, description, etc.) of this wiki for all the listed countries - bellow you will find the instructions for executing it. 

2. **AQUASTAT** 
  It is the FAO’s global water information system, providing data for countries in Africa, Asia, Latin America, and the Caribbean countries. Accesible online by the following link:[aquastat](http://www.fao.org/nr/water/aquastat/main/index.stm) 

### Africa Groundwater Atlas Scrapper

```
   python earthwise_scrapper.py > rdf_output.ttl

```

The script detects all the countries listed in http://earthwise.bgs.ac.uk/index.php/Hydrogeology_by_country, and extracts the  **rdfs** (using turtle format) automatically for each of them. The **rdf_output.txt** file contains the rdf results.


```
   python querytest.py 

```

Small script for testing queries to the *rdf_output.ttl* file - it uses rdflib library.

**Note: Both scripts are tested with version Python 2.7.13**
