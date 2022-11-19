# Open Source in Environmental Sustainability
**<center>Preserving a stable climate and natural resources with openness</center>**
<center> Tobias Augspurger, Eirini Malliaraki and Josh Hopkins </center>
<center> Report Issue 2022 </center>
<br />

```{image} ./images/mycelium_sustainability.png
:width: 300px
:align: center
```

<br />

## Executive Summary 

Despite the strong transformative impact of Open Source Software (OSS) and open data, the potential for developing environmentally sustainable technologies is not well understood. This study provides the first analysis of the open source software ecosystem in the field of environmental sustainability and climate technology. Thousands of actively developed OSS projects and organisations have been collected through the Open Sustainable Technology database and systematically analysed using qualitative and quantitative methods.

The analysis covers multiple dimensions – including the technical, the social, and the organisational. It highlights key risks and challenges for users, developers, and decision makers, as well as opportunities for more systemic collaboration and positive impact generation.

This study identifies common Open Sustainability Principles, which are critical for achieving sustainability goals. They provide transparency and trust in the development and deployment of various technologies, support traceable decision-making, foster collaborative innovation, and build capacity for the localisation and customisation of climate technologies.

Open source still plays a minor role as a long-term transformation strategy in sustainability compared to other domains transformed by Open Source Software. Half of all identified projects are in data-rich domains such as climate science, biosphere, energy system modelling, transportation and buildings. Other topics, such as carbon offsets, battery technology, sustainable investment, emission observation and integrated assessment modelling, show few notable developments. 

Newly emerging topics such as green software were identified based on popularity growth. Most identified projects are relatively young, with a median age of about 4 years. The programming languages Python and R dominate the ecosystem. Permissive licences such as MIT are the first choice for most projects, followed by copyleft licence GPLv3.

Analysis of the distribution of knowledge, work, and project governance further reveals that small open source communities lead most of the development, and open source projects rely heavily on a single developer contributing on average 70% of the commits to a project. It further indicates a sectoral and geographical imbalance in open information and knowledge exchange, with large proportion of OSS projects originating in academia and some large government agencies. In particular, the participation of private companies is remarkably low. The geographic focus is on Europe and the U.S., while the number of projects from the Global South is low. 

The low participation of for-profit organisations and start-ups with open source business models is remarkable. Almost all developments focus on understanding environmental change at the state or sectoral level without examining the causes on a company level. Larger developments by organisations based in India and China are underrepresented or virtually nonexistent, despite the current significant emissions and environmental impacts of these countries.

When combined with the right support, community, and funding structures, OSS accelerates collaboration and can have a fundamental impact on climate change and environmental sustainability. On the basis of our analyses, we therefore make recommendations such as:
- Strengthening the interconnectivity and knowledge exchange of the identified communities 
- Closing the knowledge gap on the environmental impact of industries and companies 
- Creating incubators and other support programmes for OSS in the field of environmental sustainability as well as dedicated funds that provide core and maintenance funding 
- Developing better technical interfaces and middleware between platforms, data, models and OSS tools across and within sectors to “stop reinventing the wheel”
- Transforming financial institutions through transparent and scientific decision making for sustainable investments.

To summarise, we conclude that digital and sustainable transformations must converge as a digital public good if we are to meet agreed environmental targets, and create a safe and just corridor for people and the planet. Open Sustainability Principles can help governments, research institutes, NGOs, and companies to rapidly move toward science-based decarbonisation of the economy and the conservation of natural resources and ecosystems. The use of open source and open science methods prevents greenwashing by making decision-making processes transparent and traceable.

This report presents the first of its kind analysis of open source technology in sustainability to provide the empirical backbone for guiding community building, policy development and investment. Strengthening OSS for sustainability is the first step toward creating an open environmental intelligence to enable a prosperous and sustainable future for all. 

---

>  “The struggle to understand and steer the interaction between the bitsphere and the biosphere is the struggle for community in the broadest ecological context.” <br/><br/>
> [Ursula M. Franklin](https://en.wikipedia.org/wiki/Ursula_Franklin), The Real World of Technology (1989)

---

## Acknowledgement

Thanks for all the valuable insights and interviews: <br/> 
[**Jackson Hoffart**](https://github.com/jdhoffa) ([Rocky Mountain Institute](https://rmi.org/)), [**Daniel Huppmann**](https://github.com/danielhuppmann/) ([International Institute for Applied Systems Analysis](https://iiasa.ac.at/)), [**Benoit Petit**](https://github.com/bpetit) ([Hubblo](https://hubblo.org/)), [**Ryan Abernathey**](https://github.com/rabernat) ([Earthmover](https://earthmover.io/)), [**Tom Brown**](https://github.com/nworbmot) ([PyPSA](https://pypsa.readthedocs.io/)), [**Clifford Hansen**](https://github.com/cwhanse) ([pvlib](https://pvlib-python.readthedocs.io/)), [**Valentin Sulzer**](https://github.com/tinosulzer) ([PyBaMM](https://github.com/pybamm-team/)), [**Jenni Rinker**](https://github.com/jennirinker) ([DTU Wind and Energy Systems](https://wind.dtu.dk/)), [**Julia Wagemann**](https://github.com/jwagemann) (Independent), [**Dustin Carlino**](https://github.com/dabreegster) ([A/B Street](https://github.com/a-b-street/abstreet)), [**Shuli Goodman**](https://www.linkedin.com/in/shuligoodman) ([Linux Foundation Energy](https://www.lfenergy.org/)), [**Rafael Mudafort**](https://github.com/rafmudaf) ([US National Renewable Energy Laboratory](http://www.nrel.gov/)), [**Joe Hamman**](https://github.com/jhamman) ([CarbonPlan](https://carbonplan.org/)), [**Sylwester Arabas**](https://github.com/slayoo) ([PySDM](https://github.com/atmos-cloud-sim-uj/PySDM)),  [**Trystan Lea**](https://github.com/TrystanLea) ([Open Energy Monitor](https://openenergymonitor.org/))

Special thanks to [**Katarzyna Kulma**](https://github.com/kkulma) for reviewing and contributing to the data analysis and visualisation. 

Thanks to the contributions and support of:<br />
[Tjark Döring](https://github.com/tjarkdoering), [Victoria Lo](https://www.linkedin.com/in/victoria-lo), [Nithiya Streethran](https://linkedin.com/in/nmstreethran), [Felix Dietze](https://github.com/fdietze), [Johannes Karoff](https://fr.linkedin.com/in/johannes-karoff-3110011b6), [Alejandro Aristi](https://linkedin.com/in/alejandro-aristi), [Joe Torreggiani](https://www.linkedin.com/in/joetorreggiani), [Malgorzata Augspurger](https://de.linkedin.com/in/malgorzata-augspurger-9a28987b), [Miriam Winter](https://linkedin.com/in/miriam-winter-11b763225/) and [Nick Fiege](https://linkedin.com/in/nickfiege).

This report would have been impossible without people all round the world contributing to [OpenSustain.tech](https://opensustain.tech/):<br />
<br />
<a href="https://github.com/protontypes/open-sustainable-technology/graphs/contributors">
  <img width="100%" src="https://contrib.rocks/image?repo=protontypes/open-sustainable-technology" />
</a>
<br />

The people behind OpenSustain.tech and this report are an free and open source community. However, we would like to thank the organizations that provided us with financial and consulting support. 

::::{grid}
:gutter: 3

:::{grid-item-card} 
[![](./images/subak.png)](https://subak.org/)
:::

:::{grid-item-card} 
[![](./images/protontypes_text_only.png)](https://github.com/protontypes)
:::

:::{grid-item-card} 
[![](./images/open_corridor.png)](https://www.opencorridor.org/)
:::
::::
