# Ecosystem collaborations

The open source ecosystem can not be sustained unless projects, supporting organisations, and businesses collaborate to develop and support a shared digital infrastructure. Collaboration within and across sectors lowers duplication, helps join forces to tackle major issues and builds up social capital. 

Bridging sub-communities also creates connections between projects, which can have an effect on the sustainability of the projects. For example, research has shown that social network ties between developers influence the survival of open-source software projects and that GitHub contributors are more likely to join projects with which they have prior social connections. For these reasons, combined with the urgency to decarbonise various industries, we considered the areas where more collaboration is needed.

## Across and within fields

One promising area for more collaboration is between the **physics-based modelling and data science communities**; for example, in modelling physical systems for Earth system science or other physics-based models in battery and energy applications. In addition, there's a lot of recent technological developments in machine learning, and several sustainable applications could benefit from those advances. But there is an underlying methodological gap which affects such collaborations. While new efforts are already integrating machine learning and physics-based models, the communities could join forces to combine the best from both methods: Highly accurate forecasts based on machine learning models; and long-term knowledge building and deep understanding of causal relationships based on physical models. 

**Also, competition in both industry and academia hampers cooperation within the same field.** This is particularly challenging in the energy systems community, where dozens of similar OSS modelling frameworks exist, and there is little to no incentive from different academic groups to coordinate.

Only very few attempts to combine open source projects with each other can be identified. [OS-Climate](https://github.com/os-climate) is one of the few exceptions with the attempt to combine different open datasets to a global environmental rating for sustainable investment. Such approaches are called [Integrated Assessment Modelling](https://en.wikipedia.org/wiki/Integrated_assessment_modelling).  In total, three active projects from the scientific field were found which attempt to build this bridge: [Dynamic Integrated Model of Climate and the Economy](https://github.com/Libbum/DICE.jl), [Global Change Analysis Model](https://github.com/JGCRI/gcam-core) and [Integrated Assessment Modeling Consortium](https://github.com/IAMconsortium). 

```{figure} ../images/pyam_trajectories.png
---
height: 300px
name: directive-fig
---
Integrated Assessment Modeling with [pyam](https://pyam-iamc.readthedocs.io/en/stable/) enables the calculation of scenarios for our society by combining ecological and economic models. 
```



The coupling of different Earth systems is another important development in modelling, allowing better understanding and prediction of complex interrelationships, such as climate feedback effects. Here projects can be found such as [The Community Earth System Model](https://github.com/ESCOMP/CESM), [Energy Exascale Earth System Model](https://github.com/E3SM-Project/E3SM) or [Pangeo](https://github.com/pangeo-data/pangeo). They all have their own open source ecosystems and large communities. 

Within the field of data processing of Earth observation data, the application of Google Earth Engine is ubiquitous. Various open source tools and datasets offer an easy entry into this field. [Awesome Earth Engine Apps](https://github.com/philippgaertner/awesome-earth-engine-apps) and [Awesome Gee Community Datasets](https://github.com/philippgaertner/awesome-earth-engine-apps) provide an overview of the healthy software ecosystem that has developed in this area in recent years. The platform offers open interfaces, but is itself a closed platform of Google and therefore bears the risk, like other large closed source online platforms, to develop against the interest of the users. Microsoft is taking a different approach here with their [Planetary Computer](https://planetarycomputer.microsoft.com/). Instead of a proprietary "Earth Engine", there is the chance that a free and open community is formed around it due to the open licence behind the platform itself. 

To close the silo of Earth observation archives and to simplify data access, the [SpatioTemporal Asset Catalogs API](https://stacspec.org/) (STAC) was developed. This standard is becoming more and more widespread with its own tool chains and [software ecosystem](https://stacindex.org/). It is an example of how bridges can be built between different isolated projects using a standard API or middleware. Developers are enabled to access almost all open satellite data worldwide and thus combine data from different sources. Therefore, it is possible to develop generic applications that can be applied to a variety of different data sets.

All these developments and communities use similar programming languages and basic software tools, but there are no visible links between the models and communities. Within each community, the wheel is reinvented. For data formats outside of a typical GIS application, NetCDF shows a strong adoption. Especially in the field of atmospheric research and climate modelling this format is strongly represented. 

```{figure} ../images/mean_surface_temperature.png
---
height: 300px
---

Global Mean Surface Temperature prediction with [Pangeo](https://pangeo.io/), an open source development environment for the earth science. By providing simple interfaces, [examples](http://gallery.pangeo.io/repos/pangeo-gallery/cmip6/global_mean_surface_temp.html#), and data access to state-of-the-art climate simulations like Coupled Model Intercomparison Project ([CMIP6](https://www.wcrp-climate.org/wgcm-cmip/wgcm-cmip6)), anyone with little Python knowledge can see for themselves the science behind topics like climate change.

```

## Between different actors

There is a reasonable level of industry-academia collaboration in domains dominated by the private sector, such as energy modelling and optimization, transportation, battery modelling, wind turbine modelling, PVs, and transportation. Collaboration, however, does not occur at a sectoral or systematic level. In particular, sector-wide coordination in data collection and analysis lags behind. Opening up data requires either global collaboration between industries and academia. At the same time, incentives must be created for companies to open up relevant data. This is also directly related to the area of sustainable investment and ESG. Here, again, there is a lack of data and open source frameworks to examine corporate sustainability in a scientific and verifiable way. 
