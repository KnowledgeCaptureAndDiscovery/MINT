---
layout: page
title: MINT Release updates
---
<section id="overview">

    <header class="major">
        <h2>November, 2019</h2>
        <h4>MINT NetCDF</h4>
    </header>
    <ul>
        <li>Release of MINT NetCDF convention
        	<ul>
        		<li> We propose a self-describing data format for structured gridded datasets for MINT data catalog and visualization based on the NetCDF and the CF convention. Check <a href="https://github.com/mintproject/MINT-NetCDF-Convention">here</a> for the lastest document. Please open new issues on <a href="https://github.com/mintproject/MINT-NetCDF-Convention/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc">GitHub</a> or on <a href="https://docs.google.com/spreadsheets/d/1eT_Z51R4VwVen-qx7XGtNjoHuc2sMlYmmxbi5acumx0/edit#gid=0"> [Google doc]</a> for comments.</li>
        	</ul>
        <li>Release of MINT-GeoViz
        	<ul>
	        	<li> We are releasing the v1 of MINT-GeoViz, an interactive visualization library for large geospatial datasets that follow MINT NetCDF convention. Check out this <a href="https://github.com/mintproject/MINT-GeoViz/tree/master?">GitHub repo</a> for more details.</li>
	        	<li> Check out our full <a href="https://drive.google.com/drive/folders/1t9E5HsUOre0CgAevkdRAxgaRQghJ_i2v?usp=sharing">demo</a> and <a href="https://github.com/mintproject/MINT-GeoViz/tree/master/examples/notebooks">notebook examples</a> on how to use the library</li>        	</ul>     
        </ul>

    <header class="major">
	   <h2>October, 2019</h2>
        <h4>Data Catalog</h4>
    </header>
    <ul>
        <li>Release D-REPR: a library for reading heterogeneous datasets into common representations. Check its <a href="https://github.com/usc-isi-i2/d-repr">GitHub</a> for more information.</li>
    </ul>



    <header class="major">
	    <h2>May, 2019</h2>
        <h4>Model Catalog</h4>
	</header>
    
    <ul>
        <li>New content: The MINT model catalog has been expanded to include a semantic representation of units, scientific variables and links to Wikidata. Check the <a href="https://github.com/mintproject/ModelCatalog/releases">release on GitHub</a> for more information. </li>
        <li>New APIs for adding content: We have expanded our APIs with a new client based on Open API that allows anyone to insert models in the model catalog. The API is accessible in the following link: <a href="https://api.models.mint.isi.edu/v0.0.2/ui/#/">https://api.models.mint.isi.edu/v0.0.2/ui/#/</a></li>
        <li>New APIs for accessing content: 3 new methods have been added to our <a href="https://query.mint.isi.edu/api/mintproject/MINT-ModelCatalogQueries#/">GRLC API</a>. The first one, to obtain additional information of a Scientific Variable given its label (getStandardVariableMetadata). The other two (getInputCompatibleConfig) and (getOutputCompatibleConfig) retrieve those models or software compatible with a target model. This facilitates understanding which software has variables that may interoperate with other software.</li>
        <li>A new client for accessing content: With our new Python client, now it is possible to access the content in the model catalog without having to issue SPARQL queries or API queries. <a href="https://github.com/mintproject/MINT-ModelCatalogAPI-client">Check it out here</a>.</li>
        <li>New examples: Check out our <a href="https://github.com/mintproject/MINT-ModelCatalogAPI-client/blob/master/notebook-example-how-to-use.ipynb">notebook</a> for examples on how to use the client.</li>
        <li>The <a href="https://dev.models.mint.isi.edu">Model Explorer</a> has been updated to show the contents of models in a more user-friendly manner. Check <a href="https://dev.models.mint.isi.edu">here</a> the latest version. Please <a href="https://github.com/mintproject/MINT-ModelCatalogExplorer/issues/new">open new issues on GitHub</a> if you find bugs.
        </li>
        
    </ul>
    
</section>
