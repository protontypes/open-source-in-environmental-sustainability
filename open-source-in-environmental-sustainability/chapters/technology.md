# Technology

- **Create better technical interfaces and middleware between platforms, data, models and tools.** Most open source and open data projects are used in isolation and are not combined. This leads to an increased reinvention of the wheel and inhibits the innovation process. There is much to learn from other open source communities such as the [Robotic Operating System](https://www.ros.org/), where a high degree of modularity has led to increased collaboration between different open source communities from various subject areas. This has been made possible through common interfaces, workshops, community meetings, applications and standard architectures. The same mindset can also be applied to different areas within sustainable technologies. A digital Earth twin combined from different existing open source projects offers the advantage that the strengths of already existing knowledge and communities can be used. Many monolithic projects and platforms do not offer the necessary flexibility for different types of applications. Cities and communities play a special role here, as a multitude of environmentally relevant spheres come together in concrete applications. This is why the greatest opportunity exists in urban applications to create a modular cross-domain operating system for environmental sustainability. For subfields such as energy system modelling, earth observation and geosciences, developments such as [PyPSA](https://pypsa.org/), [Julia Climate](https://juliaclimate.org/), [Radiant.Earth](https://www.radiant.earth/), [WhiteBox](https://www.whiteboxgeo.com/), and [Pangeo](https://pangeo.io/) are already pointing in the right direction.

---

- **Developing Open Data Commons in conjunction with OSS**. All interviewed developers and contributors have an intimate understanding of the data landscape as well as the quality, provenance and accessibility or lack of open data in their respective fields. Organisations such as [Subak](https://subak.org/) can serve as a central link, investing in and stewarding missing data in climate technology. Establishing connections between open source code and data sets can help create horizontal applications and thus make them more applicable worldwide. A systematic analysis of the datasets associated with the listed open source projects can help close the gap between usage and open source development.

---

- **Standardise environmental data and models using open source across different levels of government.** The standardisation of data structures and APIs using open source approaches can contribute significantly to ensuring that local data about our natural environment are interoperable across government bodies and industries and can be easily integrated into larger datasets. The province of British Columbia is a pioneer in this regard, delivering a variety of [open source and open data developments](https://github.com/bcgov) on [water supply](https://github.com/bcgov/fasstr), [wetlands](https://github.com/bcgov/wetlandmapR), and [air quality](https://github.com/bcgov/pm25-caaqs-indicator). Such standardised environmental data are essential for scientific analyses. At the same time, they can also be used to better understand the environmental impacts of local production and consumption. However, such data can only be useful if the collection and provision conform to common standards. Analysis and presentation of such aggregated environmental data across different provinces, cities and municipalities can significantly contribute to a shared knowledge base for decision-makers and citizens. With many governments adopting the UN Sustainable Development Goals as part of their internal strategies, we encourage policy and decision-makers to assess their contribution towards these Global Goals within the context of open source and public good contributions for sustainability. 

---

- **Create open communities and software tools for observing and monitoring greenhouse gas emissions through Earth observation.** Although emissions are central to climate change, the software tools and communities studied allow for little collaboration on Earth observation. Free access to satellite data from [Sentinel-5P](https://en.wikipedia.org/wiki/Sentinel-5_Precursor), [GOSAT](https://en.wikipedia.org/wiki/Greenhouse_Gases_Observing_Satellite), [GOSAT2](https://en.wikipedia.org/wiki/Greenhouse_Gases_Observing_Satellite-2), [OCO2](https://en.wikipedia.org/wiki/Orbiting_Carbon_Observatory_2), [OCO3](https://en.wikipedia.org/wiki/Orbiting_Carbon_Observatory_3), [SABER](https://saber.gats-inc.com/), [MLS](https://mls.jpl.nasa.gov/) and the upcoming [CO2M](https://www.esa.int/ESA_Multimedia/Images/2021/02/CO2M) provides the basis for such collaboration<sup><a href="https://acp.copernicus.org/articles/22/9617/2022/acp-22-9617-2022-discussion.html">1</a></sup>. However, in many cases the integration of these data into a common format is costly. There is also a lack of powerful and open transport models that can trace these emission measurements back to individual point sources. Although open repositories such as [STILT](https://github.com/uataq/stilt) and [X-STILT](https://github.com/uataq/X-STILT) exist for these models, open licences and communities are lacking.  The first important steps in the right direction are shown by [Emissions API](https://github.com/emissions-api/emissions-api) and [oco2peak](https://github.com/dataforgoodfr/batch7_satellite_ges/). Monitoring point emissions through open and traceable satellite data and models has the long-term potential to prevent the obscuring of major emission sources and to attribute them to polluters.


---

 ```{figure} ../images/africa_osm_map.png
---
width: 100%
---
[PyPSA-Earth](https://pypsa-earth.readthedocs.io/) is the first open source global energy system model with data in high spatial and temporal resolution. It enables large-scale collaboration by providing a tool that can model the world energy system or any subset of it.
License: [GPL-3.0](https://github.com/pypsa-meets-earth/pypsa-earth/blob/main/LICENSE)
```