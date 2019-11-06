---
layout: page
title: Architecture
images-array:
    - image: assets/images/architecture/legend.svg
    - image: assets/images/architecture/mint-services.svg
      alt: <p> Last update 11/06/2019 </p>
---

{% for item in page.images-array %}
  <img class="img-responsive" src="{{ item.image }}" alt="{{ item.alt }}">
{% endfor %}
<!--p>Some Text.</p>

<hr class="major" /-->
