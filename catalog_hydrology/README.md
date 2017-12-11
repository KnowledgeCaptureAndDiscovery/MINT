## Scrapper for extracting hydrology information

We are going to use two sources:


1. **Africa Groundwater Atlas** 
  The successful and sustainable development of groundwater resources in Africa is critical for future safe water supplies, economic  growth and food security in the continent. Doing this successfully relies on good hydrogeological understanding - but much of the data and information that already exists about groundwater in Africa is not available to the people who could make use of it. Information freely accessible and it can be accessed online by following the link: [earthwise](http://earthwise.bgs.ac.uk/index.php/Hydrogeology_by_country) 

* **"earthewise_scrapper.py"** extracts automatically the details ( authors, citation, reference, description, etc.) of this website for all the listed countries - bellow you will find the instructions for executing it. 

2. **AQUASTAT** 
  It is the FAO’s global water information system, providing data for countries in Africa, Asia, Latin America, and the Caribbean countries. Accesible online by the following link:[aquastat](http://www.fao.org/nr/water/aquastat/main/index.stm) 

### Africa Groundwater Atlas Scrapper

```
   python earthwise_scrapper.py

```
**Nota: Tested with version Python 2.7.13**

*Output example of the scrapper:* 
  * Extracting automaticaly: http://earthwise.bgs.ac.uk/index.php/Hydrogeology_of_Algeria ###### 
    * **Resource**: http://earthwise.bgs.ac.uk/index.php/Hydrogeology_of_Algeria 
    * **Description**: Hydrogeology of Algeria - Earthwise 
    * **Location**: Algeria 
    * **Aut.** Dr Nabil Chabour - **Inst**:Université Constantine, Algeria
    * **Aut.** Brighid Ó Dochartaigh - **Inst**:British Geological Survey, UK
    * **Aut.** Dr Naima Mebrouk - **Inst**:Université d'Oran, Algeria
    * **Aut.** Professor Moulay Idriss Hassani - **Inst**:Université de Oran, Algeria
    * **Aut.** Dr Kirsty Upton - **Inst**:British Geological Survey, UK
    * **Citation**: Bibliographic reference: Chabour, N, Mebrouk, N, Hassani, I H, Upton, K, and Ó Dochartaigh, B É. 2016. Africa Groundwater Atlas: Hydrogeology of Algeria. British Geological Survey.  
    * **Terms of use**: http://earthwise.bgs.ac.uk/index.php/Africa_Groundwater_Atlas_Terms_of_Use 
    * **Rdf link**: ['http://earthwise.bgs.ac.uk/index.php?title=Special:ExportRDF/Hydrogeology_of_Algeria&xmlmime=rdf'] 

** Note: The script detec all the countries listed in http://earthwise.bgs.ac.uk/index.php/Hydrogeology_by_country, and it extract the previous information automatically. 
