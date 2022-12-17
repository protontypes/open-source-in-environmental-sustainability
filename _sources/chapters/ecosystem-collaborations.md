# Ecosystem Collaborations

The OSS ecosystem can not be sustained unless projects, supporting organisations, and businesses collaborate to develop and foster a shared digital infrastructure. Collaboration within and across sectors reduces duplication, concentrates efforts to tackle major issues, and builds social capital. Bridging sub-communities also creates connections between projects, which can affect the sustainability of the projects. For example, research has shown that social network ties between developers influence the survival of OSS projects and that GitHub contributors are more likely <sup><a href="http://reports-archive.adm.cs.cmu.edu/anon/isr2021/CMU-ISR-21-103.pdf">1</a></sup> to join projects with which they have prior social connections. For these reasons, combined with the urgency to decarbonise various industries, we consider areas where more collaboration is needed. See recommendations, for general recommendations on {ref}`collaboration`.

## Across and Within Fields

One promising area for more collaboration is between the **physics-based modelling and data science communities and machine learning**. For example, in modelling physical systems for Earth system science or other physics-based models in battery and energy applications. Furthermore, many recent technological advances in machine learning exist, and several sustainable applications could benefit from those advancements. However, such collaborations are hampered by an underlying methodological gap. While new efforts are already being made to integrate machine learning and physics-based models, these distinct communities could join forces to combine the best of both methods: highly accurate forecasts based on machine learning models, long-term knowledge building, and a deep understanding of causal relationships based on physical models. This reduces the risk of relying too much on purely statistical models without understanding the causal relationships. Models thus remain “open source” in the sense that they are still traceable for humans. Decision-making based on these models remains traceable to humans in the final instance.

**Competition in both industry and academia hampers cooperation.** This is particularly challenging in the energy systems community, where dozens of similar OSS modelling frameworks exist, and there is little to no incentive from different academic groups to coordinate. Only very few attempts to combine open source projects can be identified. [OS-Climate](https://github.com/os-climate) is one of the few efforts to combine different open datasets to provide an integrated environmental rating for sustainable investment. Such approaches are called [Integrated Assessment Modelling](https://en.wikipedia.org/wiki/Integrated_assessment_modelling). In total, three active projects from this field were found that attempt to build this bridge: [Dynamic Integrated Model of Climate and the Economy](https://github.com/Libbum/DICE.jl), [Global Change Analysis Model](https://github.com/JGCRI/gcam-core) and [Integrated Assessment Modeling Consortium](https://github.com/IAMconsortium). The following figure shows a typical result of this modelling, where various economic and social scenarios change the release of carbon dioxide.

```{figure} ../images/pyam_trajectories.png
---
width: 100%
---
<br/>Integrated Assessment Modeling with [pyam](https://pyam-iamc.readthedocs.io/en/stable/) enables the calculation of scenarios for our society by combining ecological and economic models. 
```

The coupling of different Earth systems is another important development in modelling that allows a better understanding and prediction of complex interrelationships, such as climate feedback effects. Notable examples are [The Community Earth System Model](https://github.com/ESCOMP/CESM), the [Energy Exascale Earth System Model](https://github.com/E3SM-Project/E3SM) and [Pangeo](https://github.com/pangeo-data/pangeo), which each have their own open source ecosystems and large communities.

In the field of data processing of Earth observation data, the application of Google Earth Engine is ubiquitous. The platform offers open interfaces but is a closed platform and therefore bears the risk, like other large closed-source online platforms, of developing against the users' interest. With their [Planetary Computer](https://planetarycomputer.microsoft.com/), Microsoft is taking a different approach. Instead of a proprietary "Earth Engine," it is possible that a free and open community will form around the platform due to its open licence. Moreover, various open source tools and datasets offer an easy entry into this field. [Awesome Earth Engine Apps](https://github.com/philippgaertner/awesome-earth-engine-apps) and [Awesome Gee Community Datasets](https://github.com/samapriya/awesome-gee-community-datasets) provide an overview of the healthy software ecosystem that has emerged in recent years.

Many of the identified projects and communities use similar programming languages and software tools, but few visible links exist between the models and communities — resulting in the "reinvention of the wheel" often occurring within each community. To close the silo of Earth observation archives and to simplify data access, the [SpatioTemporal Asset Catalogs API](https://stacspec.org/) (STAC) was developed. This standard is becoming increasingly widespread with its own tool chains and [software ecosystem](https://stacindex.org/). It enables developers to access almost all open satellite data from around the world and combine data from various sources in a standardised format. It is an excellent example of how generic applications can be built from OSS components, and different isolated projects can be bridged using standard APIs.

<!-- Another prime example is FIWARE Open Data Models, which seek to improve interoperability between smart devices, including environmental data collection -->

```{figure} ../images/mean_surface_temperature.png
---
width: 100%
---

<br/>Global Mean Surface Temperature prediction with [Pangeo](https://pangeo.io/), an open source development environment for the earth science. By providing simple interfaces, [examples](http://gallery.pangeo.io/repos/pangeo-gallery/cmip6/global_mean_surface_temp.html#), and data access to state-of-the-art climate simulations like Coupled Model Intercomparison Project ([CMIP6](https://www.wcrp-climate.org/wgcm-cmip/wgcm-cmip6)), anyone with little Python knowledge can see for themselves the science behind topics like climate change.

```

## Between Different Actors

**There is a reasonable level of industry-academia collaboration in domains dominated by the private sector**, such as energy modelling and optimisation, battery modelling, wind turbine modelling, PVs, and transportation. Collaboration, however, does not occur at a sectoral or systematic level. In particular, sector-wide coordination in data collection and analysis lags behind. Opening up data requires global collaboration between industry and academia, and new incentives must be created for companies to open up relevant data safely and effectively. Similarly, in sustainable investment and ESG, there is a lack of open data and open source frameworks to evaluate corporate sustainability in a scientific and verifiable way.

<!-- TODO: consider partly moving to collaboration recommendation -->
**Collaboration between state and non-state actors is lacking in many places**. Very few multi-sector and cross-sector OSS collaborations can be identified. State and regional governments can accelerate their digital and sustainability transformations by collaborating more closely with industry, academia and NGOs towards shared objectives. This requires transition brokers to guide and facilitate multi-stakeholder alliances from a politically neutral standpoint, and help create the necessary preconditions for change to emerge across scales and system boundaries. Open sustainability principles can be applied here to:
- Generate advocacy and support
- Support cross-agency coordination
- Promote and guide innovation funding
- Bridge knowledge and information gaps between municipal, regional and state governments
- Identify challenges and opportunities for effective action
- Build capacity for local community groups to take effective action
- Guide stakeholders towards science-based decision-making

By doing so, state and non-state alliances are strengthened through a shared digital infrastructure, all while supporting the OSS ecosystem.
