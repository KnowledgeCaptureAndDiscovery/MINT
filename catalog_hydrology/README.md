## Scrapper for extracting hydrology information

We are going to use two sources:


1. Africa Groundwater Atlas: 
  The successful and sustainable development of groundwater resources in Africa is critical for future safe water supplies, economic  growth and food security in the continent. Doing this successfully relies on good hydrogeological understanding - but much of the data and information that already exists about groundwater in Africa is not available to the people who could make use of it. Information freely accessible: you can access it online now by following the link below. 
Link: http://earthwise.bgs.ac.uk/index.php/Hydrogeology_by_country

We have created a script (earthewise_scrapper) that extracts automatically the details ( authors, citation, reference, description, etc.) of this website for all the listed countries. 

2. AQUASTAT: 
  It is the FAO’s global water information system, providing data for countries in Africa, Asia, Latin America, and the Caribbean Link: http://www.fao.org/nr/water/aquastat/main/index.stm


### Africa Groundwater Atlas scrapper

```
   python earthwise_scrapper.py

```
