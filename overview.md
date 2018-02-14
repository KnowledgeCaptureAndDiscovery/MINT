---
layout: page
title: Overview
---

<section id="overview">
    <hr class="major" />
	<header class="major">
		<h4>Modeling</h4>
	</header>
   <figure>
      <img src="assets/images/overview/modeling.png" style="width: 25em"/>
      <figcaption style="font-size: 0.8em; font-variant: ">Diagram representing external forcing factors and databases needed to drive the Cycles model or a Random Forest model. The components "Cycles", "Random Forest" and the associated databases will be integrated in the MINT framework for seamless operation alongside other modeling components.</figcaption>
    </figure> 
    <p>
        The MINT project team will address primarily food production under changing 
        scenarios, changes in the water cycle due to external forcing such as climate 
        or market changes, and internal changes such as changes in food and water 
        demand due to land use change including urban growth and purchasing power. 
        Food production will be predicted based on process-based models (model Cycles) 
        that are able to use daily or sub-daily climate information, and machine learning 
        (Random Forest).  The Cycles model is an evolution of C-Farm [1] 
        and shares many modules with CropSyst [2]. The Cycles model 
        simulates yield and environmental impacts of food production based on fundamental 
        biophysical principles that control plant growth, water and nutrient cycling. 
        Its modular structure, transparent input and output structure, documentation in 
        Github, and power to model any crop and crop rotation make the Cycles model an 
        ideal component for integration in a modeling workflow alongside other models. 
        Unlike process based models, machine learning algorithms can predict single 
        indicators faster and using multiple sources of information, regardless of 
        the specific mechanistic connection between predictor and predicted variable. 
        They can be particularly powerful to predict crop production [3]. 
    </p>
    <h5>Task Leaders</h5>
    <p style="font-size: 0.9em; line-height: 1.3em">
        <strong><a href="http://plantscience.psu.edu/research/labs/kemanian" target="_blank">
        Dr. Kemanian</a></strong> has background in agroecology, systems modeling, and several 
        disciplines central to agricultural and natural systems. He developed the Cycles 
        model, components of the CropSyst model, and made contributions to the SWAT 
        model and associated models EPIC and APEX. He is currently using the PIHM and 
        Hydroterre platform, migrating to fully distributed models to represent terrestrial 
        and aquatic processes. These models have been used in numerous projects of local, 
        national and international reach. 
    </p>
    <h5>References</h5>
    <ol style="font-size: 0.9em; line-height: 1.2em">
        <li>Kemanian, A.R. and Stöckle, C.O., 2010. C-Farm: A simple model to evaluate the carbon balance of soil profiles. European Journal of Agronomy, 32(1), pp.22-29.</li>
        <li>Stöckle, C.O., Kemanian, A.R., Nelson, R.L., Adam, J.C., Sommer, R. and Carlson, B., 2014. CropSyst model evolution: From field to regional to global scales and from research to decision support systems. Environmental Modelling & Software, 62, pp.361-369.</li>
        <li>Hoffman, A.L., Kemanian, A.R. and Forest, C.E., 2018. Analysis of climate signals in the crop yield record of sub‐Saharan Africa. Global Change Biology, 24(1), pp.143-157.</li>
    </ol>
</section>
