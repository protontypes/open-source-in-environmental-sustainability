# Ecosystem Collaborations

The OSS ecosystem can not be sustained unless projects, supporting organisations, and businesses collaborate to develop and foster a shared digital infrastructure. Collaboration within and across sectors reduces duplication, concentrates efforts to tackle major issues, and builds social capital. Bridging sub-communities also creates connections between projects, which can affect the sustainability of the projects. For example, research has shown that social network ties between developers influence the survival of OSS projects and that GitHub contributors are more likely to join projects with which they have prior social connections.<sup><a href="http://reports-archive.adm.cs.cmu.edu/anon/isr2021/CMU-ISR-21-103.pdf">1</a></sup> For these reasons, combined with the urgency to decarbonise various industries, we consider areas where more collaboration is needed. For general recommendations, see {ref}`collaboration`.

## Across and Within Fields

One promising area for more collaboration is between the **physics-based modelling and data science communities and machine learning**. For example, in modelling physical systems for Earth system science or other physics-based models in battery and energy applications. Furthermore, many recent technological advances in machine learning exist, and several sustainable applications could benefit from those advancements. However, such collaborations are hampered by an underlying methodological gap. While new efforts are already being made to integrate machine learning and physics-based models, these distinct communities could join forces to combine the best of both methods: highly accurate forecasts based on machine learning models, long-term knowledge building, and a deep understanding of causal relationships based on physical models. This reduces the risk of relying too much on purely statistical models without understanding the causal relationships. Models thus remain “open source” in the sense that they are still traceable for humans. Decision-making based on these models remains traceable to humans in the final instance.

**Competition in both industry and academia can hamper cooperation.** This is particularly challenging in the energy systems community, where dozens of similar OSS modelling frameworks exist, and there is little to no incentive from different academic or industry groups to coordinate. Only very few attempts to combine open source projects can be identified. [OS-Climate](https://github.com/os-climate) is one of the few efforts to combine different open datasets to provide an integrated environmental rating for sustainable investment. Such approaches are known as [Integrated Assessment Modelling](https://en.wikipedia.org/wiki/Integrated_assessment_modelling). In total, three active projects from this field were found that attempt to build this bridge: [Dynamic Integrated Model of Climate and the Economy](https://github.com/Libbum/DICE.jl), [Global Change Analysis Model](https://github.com/JGCRI/gcam-core) and [Integrated Assessment Modeling Consortium](https://github.com/IAMconsortium). The following figure shows a typical result of this modelling, where various economic and social scenarios change the release of carbon dioxide.

```{figure} ../images/pyam_trajectories.png
---
width: 100%
---
\- Integrated Assessment Modeling with [pyam](https://pyam-iamc.readthedocs.io/en/stable/) enables the calculation of scenarios for our society by combining ecological and economic models. 
```

The coupling of different Earth systems is another important development in modelling that allows a better understanding and prediction of complex interrelationships, such as climate feedback effects. Notable examples are [The Community Earth System Model](https://github.com/ESCOMP/CESM), the [Energy Exascale Earth System Model](https://github.com/E3SM-Project/E3SM) and [Pangeo](https://github.com/pangeo-data/pangeo), which each have their own open source ecosystems and large communities.

In the field of data processing of Earth observation data, the application of Google Earth Engine is ubiquitous. The platform offers open interfaces but is a closed platform and therefore bears the risk, like other large closed-source online platforms, of developing against the users' interest. With their [Planetary Computer](https://planetarycomputer.microsoft.com/), Microsoft is taking a different approach. Instead of a proprietary "Earth Engine," it is possible that a free and open community will form around the platform due to its open licence. Moreover, various open source tools and datasets offer an easy entry into this field. [Awesome Earth Engine Apps](https://github.com/philippgaertner/awesome-earth-engine-apps) and [Awesome Gee Community Datasets](https://github.com/samapriya/awesome-gee-community-datasets) provide an overview of the healthy software ecosystem that has emerged in recent years.

Many of the identified projects and communities use similar programming languages and software tools, but few visible links exist between the models and communities — resulting in the "reinvention of the wheel" often occurring within each community. To close the silo of Earth observation archives and to simplify data access, the [SpatioTemporal Asset Catalogs API](https://stacspec.org/) (STAC) was developed. This standard is becoming increasingly widespread with its own toolchains and [software ecosystem](https://stacindex.org/). It enables developers to access almost all open satellite data from around the world and combine data from various sources in a standardised format. It is an excellent example of how generic applications can be built from OSS components, and different isolated projects can be bridged using standard APIs. Another prime example is the FIWARE [Smart Data Models](https://github.com/smart-data-models/data-models), which seek to improve interoperability between smart devices, sectors and organisations, including the consolidation and dissemination of environmental data.


```{figure} ../images/mean_surface_temperature.png
---
width: 100%
---

\- Global Mean Surface Temperature prediction with [Pangeo](https://pangeo.io/), an open source development environment for the earth science. By providing simple interfaces, [examples](http://gallery.pangeo.io/repos/pangeo-gallery/cmip6/global_mean_surface_temp.html#), and data access to state-of-the-art climate simulations like Coupled Model Intercomparison Project ([CMIP6](https://www.wcrp-climate.org/wgcm-cmip/wgcm-cmip6)), anyone with little Python knowledge can see for themselves the science behind topics like climate change.

```

## Between Different Actors

**There is a reasonable level of industry-academia collaboration in domains dominated by the private sector**, such as energy modelling and optimisation, battery modelling, wind turbine modelling, PVs, and transportation. Collaboration, however, does not occur at a sectoral or systematic level. In particular, sector-wide coordination in data collection and analysis lags behind. Opening up data requires global collaboration between industry and academia, and new incentives must be created for companies to open up relevant data safely and effectively. Similarly, in sustainable investment and ESG, there is a lack of open data and open source frameworks to evaluate corporate sustainability in a scientific and verifiable way.

**Collaboration between state and non-state actors is lacking in many places**. State and non-state actors can accelerate their digital and sustainability transformations by collaborating more closely towards shared objectives. This often requires transition brokers to guide and facilitate multi-stakeholder alliances – which bring together governments, industry, academia and civic society – from a politically neutral standpoint, to help create the necessary preconditions for change to emerge across scales and system boundaries. By adopting an open source approach, multi-sector and cross-sector alliances are strengthened through shared knowledge and resources, further strengthing the OSS ecosystem. Very few OSS collaboration efforts of this kind can be identified outside of Europe.

**Collaboration between government agencies is uncommon**. While several governments promote the sharing and reuse of OSS solutions between agencies,<sup><a href="https://commission.europa.eu/about-european-commission/departments-and-executive-agencies/informatics/open-source-software-strategy_en">2</a>,<a href="https://www.cio.gov/2016/08/11/peoples-code.html">3</a></sup> very few OSS projects within environmental sustainability can be identified as a result of multi-agency collaboration efforts; neither horizontally across, nor vertically between many levels of government. The interoperability of open knowledge and information is critical to navigating increasingly complex environmental and societal challenges. Given the importance of multi-level governance in tackling climate change, the lack of open collaboration and innovation here is concerning.

```{figure} ../images/africa_soil_map.png
---
width: 70%
---
\- [iSDA](https://www.isda-africa.com/isdasoil/) built the first field-level soil map for Africa, with 20+ soil properties predicted at 30m resolution for the entire continent. License: [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)
```
