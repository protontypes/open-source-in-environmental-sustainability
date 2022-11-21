# Ecosystem collaborations

The OSS ecosystem can not be sustained unless projects, supporting organisations, and businesses collaborate to develop and foster a shared digital infrastructure. Collaboration within and across sectors lowers duplication, concentrates efforts to tackle major issues and builds up social capital. Bridging sub-communities also creates connections between projects, which can effect the sustainability of the projects. For example, research has shown that social network ties between developers influence the survival of OSS projects and that GitHub contributors are more likely to join projects with which they have prior social connections. For these reasons, combined with the urgency to decarbonise various industries, below we consider areas where more collaboration is needed.

## Across and within fields

One promising area for more collaboration is between the **physics-based modelling and data science communities**; for example, in modelling physical systems for Earth system science or other physics-based models in battery and energy applications. In addition, many recent technological developments in machine learning exist, and several sustainable applications could benefit from those advances. But there is an underlying methodological gap which affects such collaborations. So while new efforts are already integrating machine learning and physics-based models, the communities could join forces to combine the best from both methods: highly accurate forecasts based on machine learning models and long-term knowledge building and deep understanding of causal relationships based on physical models. 

**Also, competition in both industry and academia hampers cooperation.** This is particularly challenging in the energy systems community, where dozens of similar OSS modelling frameworks exist, and there is little to no incentive from different academic groups to coordinate. Only very few attempts to combine open source projects can be identified. [OS-Climate](https://github.com/os-climate) is one of the few efforts to combine different open datasets to a global environmental rating for sustainable investment. Such approaches are called [Integrated Assessment Modelling](https://en.wikipedia.org/wiki/Integrated_assessment_modelling). In total, three active projects from this field were found which attempt to build this bridge: [Dynamic Integrated Model of Climate and the Economy](https://github.com/Libbum/DICE.jl), [Global Change Analysis Model](https://github.com/JGCRI/gcam-core) and [Integrated Assessment Modeling Consortium](https://github.com/IAMconsortium). 

```{figure} ../images/pyam_trajectories.png
---
height: 300px
name: directive-fig
---
Integrated Assessment Modeling with [pyam](https://pyam-iamc.readthedocs.io/en/stable/) enables the calculation of scenarios for our society by combining ecological and economic models. 
```


The coupling of different Earth systems is another important development in modelling that allows better understanding and prediction of complex interrelationships, such as climate feedback effects. Notable examples are [The Community Earth System Model](https://github.com/ESCOMP/CESM), the [Energy Exascale Earth System Model](https://github.com/E3SM-Project/E3SM) and [Pangeo](https://github.com/pangeo-data/pangeo), which all have their own open source ecosystems and large communities. 

Google Earth Engine is widely used in data processing of Earth observation data. The platform offers open interfaces but is a closed platform of Google and therefore bears the risk, like other large closed-source online platforms, of developing against the users' interest.  
With their [Planetary Computer](https://planetarycomputer.microsoft.com/), Microsoft is taking a different approach. Instead of a proprietary "Earth Engine," it is possible that a free and open community will form around the platform due to its open license. Moreover, various open-source tools and datasets offer an easy entry into this field. [Awesome Earth Engine Apps](https://github.com/philippgaertner/awesome-earth-engine-apps) and [Awesome Gee Community Datasets](https://github.com/philippgaertner/awesome-earth-engine-apps) provide an overview of the healthy software ecosystem that has emerged in recent years.  

To simplify access to Earth observation data, the [SpatioTemporal Asset Catalogs API](https://stacspec.org/) (STAC) was developed. This standard is becoming increasingly widespread with its own tool chains and [software ecosystem](https://stacindex.org/). It enables developers to access almost all open satellite data from around the world and combine data from various sources. It is a good example of how generic applications can be built from OSS components and different isolated projects can be bridged using standard APIs. All of these developments and communities use similar programming languages and basic software tools, but no visible links exist between the models and communities — the wheel is reinvented in each community. 

```{figure} ../images/mean_surface_temperature.png
---
height: 300px
---

Global Mean Surface Temperature prediction with [Pangeo](https://pangeo.io/), an open source development environment for the earth science. By providing simple interfaces, [examples](http://gallery.pangeo.io/repos/pangeo-gallery/cmip6/global_mean_surface_temp.html#), and data access to state-of-the-art climate simulations like Coupled Model Intercomparison Project ([CMIP6](https://www.wcrp-climate.org/wgcm-cmip/wgcm-cmip6)), anyone with little Python knowledge can see for themselves the science behind topics like climate change.

```

## Between different actors

There is a reasonable level of industry-academia collaboration in domains dominated by the private sector, such as energy modelling and optimisation, transportation, battery modelling, wind turbine modelling, PVs, and transport. Collaboration, however, does not occur at a sectoral or systematic level. In particular, sector-wide coordination in data collection and analysis lags. Opening up data requires global collaboration between industry and academia and new incentives must be created for companies to open up relevant data. This is also directly related to sustainable investment and ESG, where there is a lack of data and open source frameworks to evaluate corporate sustainability in a scientific and verifiable way. 
