---
layout: page
title: MINT Release updates
---

<section id="overview">
    <header class="major">
	    <h2>May, 2019<h2>
        <h4>Model Catalog<h4>
	</header>
    
    <ul>
        <li>New content: The MINT model catalog has been expanded to include a semantic representation of units, scientific variables and links to Wikidata. Check the <a href="https://github.com/mintproject/ModelCatalog/releases">release on GitHub</a> for more information. </li>
        <li>New APIs for adding content: We have expanded our APIs with a new client based on Open API that allows anyone to insert models in the model catalog. The API is accessible in the following link: <a href="https://api.models.mint.isi.edu/v0.0.2/ui/#/">https://api.models.mint.isi.edu/v0.0.2/ui/#/</a></li>
        <li>New APIs for accessing content: 3 new methods have been added to our <a href="https://query.mint.isi.edu/api/mintproject/MINT-ModelCatalogQueries#/">GRLC API</a>. The first one, to obtain additional information of a Scientific Variable given its label (getStandardVariableMetadata). The other two (getInputCompatibleConfig) and (getOutputCompatibleConfig) retrieve those models or software compatible with a target model. This facilitates understanding which software has variables that may interoperate with other software.</li>
        <li>A new client for accessing content: With our new Python client, now it is possible to access the content in the model catalog without having to issue SPARQL queries or API queries. <a href="https://github.com/mintproject/MINT-ModelCatalogAPI-client">Check it out here</a>.</li>
        <li>New examples: Check out our <a href="https://github.com/mintproject/MINT-ModelCatalogAPI-client/blob/master/notebook-example-how-to-use.ipynb">notebook</a> for examples on how to use the client.</li>
        <li>The <a href="https://dev.models.mint.isi.edu">Model Explorer</a> has been updated to show the contents of models in a more user-friendly manner. Chek <a href="https://dev.models.mint.isi.edu">here</a> the latest version. Please <a href="https://github.com/mintproject/MINT-ModelCatalogExplorer/issues/new">open new issues on GitHub</a> if you find bugs.
        </li>
        
    </ul>
    
</section>