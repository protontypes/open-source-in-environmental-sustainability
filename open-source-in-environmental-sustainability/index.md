# Open Source in Environmental Sustainability
**<center>Preserving climate and natural resources with openness</center>**
<center> <a href="https://www.linkedin.com/in/tobias-augspurger-5116b6191/">Tobias Augspurger</a>, <a href="https://www.linkedin.com/in/eirinimalliaraki/">Eirini Malliaraki</a> and <a href="https://www.linkedin.com/in/hopkins-josh/">Josh Hopkins</a> </center>
<center> Report 2023 </center>
<br />

```{image} ./images/mycelium_sustainability.png
:width: 300px
:align: center
```

> _"The struggle to understand and steer the interaction between the bitsphere and the biosphere is the struggle for community in the broadest ecological context."_<br/>[Ursula M. Franklin](https://en.wikipedia.org/wiki/Ursula_Franklin), The Real World of Technology (1989)


## Executive Summary


The transition to a more sustainable future requires not only technological innovation, but also new opportunities for society to involve in the development and adoption of technologies. Open source culture has demonstrated how transparent and collaborative innovation can support modern digital services, data and infrastructure. Open source software accelerates the transition to a sustainable economy by supporting traceable decision-making, building capacity for localisation and customisation of climate technologies, and most importantly, helping to prevent greenwashing. Yet, despite the transformative impact of open source culture and its use within an estimated 97%<sup><a href="https://www.synopsys.com/blogs/software-security/open-source-trends-ossra-report/">1</a></sup> of digital products, its potential for developing environmentally sustainable technologies is not well understood.

This study provides the first analysis of the open source software ecosystem in sustainability and climate technology. More than one thousand actively developed open source projects and organisations were collected and systematically analysed using qualitative and quantitative methods as part of the [Open Sustainable Technology](https://opensustain.tech/) project and the [associated database](https://airtable.com/shr9we419r2TkpLkc). The analysis covers multiple dimensions – including the technical, the social, and the organisational. It highlights key risks and challenges for users, developers, and decision-makers as well as opportunities for more systemic collaboration. Based on these unique insights, we were also able to define four key {ref}`open-sustainability-principles`.

This analysis indicates that open source still plays a minor role as a long-term transformation strategy in sustainability compared to other domains. Half of all identified projects are in data-rich fields such as climate science, biosphere, energy system modelling, transportation and buildings. Other topics, such as carbon offsets, battery technology, sustainable investment, emission observation and integrated assessment modelling, show few notable developments. Newly emerging topics such as green software were identified based on popularity growth. Most identified projects are relatively young, with a median age of 4.45 years. Moreover, the programming languages Python and R dominate the ecosystem, while permissive licences such as MIT are preferred, followed by the copyleft licence GPLv3.

Analysis of the distribution of knowledge, work, and project governance reveals that small open source communities lead most of the development. On average, open source software projects rely heavily on a single developer responsible for ~70% of the contributions to a project. In addition, academia and several government agencies contribute significantly to open source, while the lack of for-profit organisations and start-ups with open source business models is remarkable. Finally, most OSS projects are based largely in Europe and North America, with a small number of projects from the Global South. Larger development efforts by organisations based in India and China are underrepresented or nonexistent.

This report presents the first-of-its-kind analysis of open source technology in sustainability and climate technology, providing the empirical backbone for guiding community building, policy development and future investment. Based on this analysis, we, therefore, propose recommendations for those interested in supporting open source software in environmental sustainability more effectively via:

- Strengthening the interconnectivity and knowledge exchange of the identified open source communities.
- Building capacity and increasing potential for real-world impact by connecting projects to local use cases.
- Closing the knowledge gap on the environmental impact of companies through open source principles.
- Adapting and extending existing open source projects for underrepresented countries in the global south.
- Creating incubators and other support programmes for open source software in environmental sustainability as well as dedicated funds that provide core funding for development and maintenance.
- Developing better technical interfaces between platforms, data, models and open source tools across and within sectors to “stop reinventing the wheel”.
- Standardising environmental data exchange across different levels of government.
- Transforming financial institutions through transparent and scientific decision-making for sustainable investments.
<!-- - Adopting an "open source first" criteria when providing funding towards sustainable technologies. -->
<!-- - Prioritising open source outputs as an investor, research institute, or funding body (ie., government, NGO, venture capitalist). -->
<!-- - Including open source contributions within Sustainable Development Goals (SDGs), more broadly. -->
<!-- - Building knowledge and capacity for both open source and sustainability through primary, secondary and tertiary curricula. -->

Digital and sustainable transformation needs converge as a digital public good to achieve agreed environmental goals and create a safe and equitable corridor for people and the planet. Open sustainability principles can help governments, research institutes, nongovernmental organisations, and businesses move quickly toward science-based decarbonisation and conservation of natural resources and ecosystems by providing critical transparency, traceable decision-making, and collaboration on innovation.

---


## Acknowledgements

Thanks for all the valuable insights and interviews: <br/> 
[**Jackson Hoffart**](https://github.com/jdhoffa) ([Rocky Mountain Institute](https://rmi.org/)), [**Daniel Huppmann**](https://github.com/danielhuppmann/) ([International Institute for Applied Systems Analysis](https://iiasa.ac.at/)), [**Benoit Petit**](https://github.com/bpetit) ([Hubblo](https://hubblo.org/)), [**Ryan Abernathey**](https://github.com/rabernat) ([Earthmover](https://earthmover.io/)), [**Tom Brown**](https://github.com/nworbmot) ([PyPSA](https://pypsa.readthedocs.io/)), [**Clifford Hansen**](https://github.com/cwhanse) ([pvlib](https://pvlib-python.readthedocs.io/)), [**Valentin Sulzer**](https://github.com/tinosulzer) ([PyBaMM](https://github.com/pybamm-team/)), [**Jenni Rinker**](https://github.com/jennirinker) ([DTU Wind and Energy Systems](https://wind.dtu.dk/)), [**Julia Wagemann**](https://github.com/jwagemann) (Independent), [**Dustin Carlino**](https://github.com/dabreegster) ([A/B Street](https://github.com/a-b-street/abstreet)), [**Shuli Goodman**](https://www.linkedin.com/in/shuligoodman) ([Linux Foundation Energy](https://www.lfenergy.org/)), [**Rafael Mudafort**](https://github.com/rafmudaf) ([US National Renewable Energy Laboratory](http://www.nrel.gov/)), [**Joe Hamman**](https://github.com/jhamman) ([CarbonPlan](https://carbonplan.org/)), [**Sylwester Arabas**](https://github.com/slayoo) ([PySDM](https://github.com/atmos-cloud-sim-uj/PySDM)),  [**Trystan Lea**](https://github.com/TrystanLea) ([Open Energy Monitor](https://openenergymonitor.org/))

Special thanks to [**Katarzyna Kulma**](https://github.com/kkulma) for reviewing and contributing to the data analysis and visualisation.

Thanks to the contributions and support of:<br />
[Tjark Döring](https://github.com/tjarkdoering), [Alejandro Aristi](https://linkedin.com/in/alejandro-aristi), [Victoria Lo](https://www.linkedin.com/in/victoria-lo), [Nithiya Streethran](https://linkedin.com/in/nmstreethran), [Felix Dietze](https://github.com/fdietze), [Johannes Karoff](https://fr.linkedin.com/in/johannes-karoff-3110011b6),  [Joe Torreggiani](https://www.linkedin.com/in/joetorreggiani), [Malgorzata Augspurger](https://de.linkedin.com/in/malgorzata-augspurger-9a28987b), [Miriam Winter](https://linkedin.com/in/miriam-winter-11b763225/), Lars Oliver Zlotos and [Nick Fiege](https://linkedin.com/in/nickfiege).

This report would have not been possible without people from all around the world contributing to [OpenSustain.tech](https://opensustain.tech/):<br />
<br />
<a href="https://github.com/protontypes/open-sustainable-technology/graphs/contributors">
  <img width="80%" src="https://contrib.rocks/image?repo=protontypes/open-sustainable-technology" />
</a>
<br />

OpenSustain.tech is a community-driven, non-profit project. However, we would like to thank the organisations that provided us with financial and consulting support.

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

(support-us)=
## How to Contribute 

More than ever, free and open source projects are enabling citizens, scientists, developers, civil society, industry and government to mitigate climate change. We want to hear from you if you:

- Like to participate in future studies of this form. 
- Have experience developing, supporting or systematically using open source software for sustainability applications.
- Want to [contribute](https://opensustain.tech/contributing/) to OpenSustain.tech by identifying new and missing projects.
- Have experience visualising or processing data with Python and know how to integrate such data into a new website.
- Are a funder and want to support these developer communities via open infrastructure funds, consortia-based support or other collaborative models across institutions and regions.
- Want to help us build any of the recommendations and future directions of OpenSustain.tech.

For these and any other enquiry please reach out via email to [Tobias](mailto:tobias.augspurger@protontypes.eu), [Eirini](mailto:eirinimalliaraki@gmail.com) or [Josh](mailto:josh@opencorridor.org):

## Stay Informed

To stay informed about this projects or to connect with the community please join our [Gitter Chat](https://gitter.im/protontypes/community), Follow us on [Twitter](https://twitter.com/protontypes), [GitHub](https://github.com/protontypes) or [LinkedIn](https://de.linkedin.com/company/protontypes). 

## Table of Contents

```{tableofcontents}
```
