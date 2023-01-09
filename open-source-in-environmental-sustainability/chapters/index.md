---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Open Source in Environmental Sustainability
**<center>Preserving climate and natural resources with openness</center>**
<center> <a href="https://www.linkedin.com/in/tobias-augspurger-5116b6191/">Tobias Augspurger</a>, <a href="https://www.linkedin.com/in/eirinimalliaraki/">Eirini Malliaraki</a> and <a href="https://www.linkedin.com/in/hopkins-josh/">Josh Hopkins</a> </center>
<center> Report 2023 </center>
<br />

```{image} ../images/mycelium_sustainability.png
:width: 300px
:align: center
```

> _"The struggle to understand and steer the interaction between the bitsphere and the biosphere is the struggle for community in the broadest ecological context."_<br/>[Ursula M. Franklin](https://en.wikipedia.org/wiki/Ursula_Franklin), The Real World of Technology (1989)

## Executive Summary

Open source is everywhere. Its culture has demonstrated how transparent and collaborative innovation can transform modern society, with over 97% of critical digital infrastructure and services depending on it.<sup><a href="https://www.synopsys.com/content/dam/synopsys/sig-assets/reports/rep-ossra-2022.pdf#page=8">1</a></sup> Open source software accelerates the transition to a sustainable economy by supporting traceable decision-making, building capacity for localisation and customisation, providing new opportunities for participation, and preventing greenwashing by ensuring transparency and trust. Yet, despite the transformative impact of open source culture, its potential within environmental sustainability is not well understood.

This report provides the first analysis of the open source software ecosystem in the field of sustainability and climate technology. More than one thousand actively developed open source projects and organisations were collected and systematically analysed using qualitative and quantitative methods as part of the [Open Sustainable Technology](https://opensustain.tech/) project and the [associated database](https://airtable.com/shr9we419r2TkpLkc). The analysis covers multiple dimensions – including the technical, social, and organisational, providing an empirical backbone for guiding community building, policy development and future investment. It highlights key risks and challenges for users, developers, and decision-makers, as well as opportunities for more systemic collaboration. Based on these unique insights, four guiding principles we define as {ref}`open-sustainability-principles` have been identified.

Our findings indicate that open source still plays a minor role as a transformation strategy within sustainability compared to other domains. Half of all identified projects are in data-rich fields such as climate science, biosphere, energy system modelling, transportation and buildings. Other topics, such as carbon offsets, battery technology, sustainable investment, emission observation and integrated assessment modelling, show few notable developments. Newly emerging topics, such as green software, were identified based on popularity growth. Most identified projects are relatively young, with a median age of 4.45 years. The programming languages Python and R dominate the ecosystem, while developers favour permissive licences such as MIT, followed by the copyleft licence GPLv3.

Analysis of the distribution of knowledge, work, and project governance reveals that small, open source communities lead most of the development. On average, open source software projects rely heavily on a single programmer responsible for ~70% of the contributions to a project. In addition, academia and several government agencies contribute significantly to open source in environmental sustainability, while the lack of for-profit organisations and start-ups with open source business models is remarkable. Finally, most open source software projects within the ecosystem are largely based in Europe and North America, with a small number of projects from the Global South. Larger development efforts by organisations based in India and China are underrepresented or nonexistent.

Based on the results, we identify several action areas for those interested in supporting open source software in environmental sustainability more effectively:

- Strengthen the interconnectivity and knowledge exchange of the identified open source communities.
- Build capacity and increase the potential for real-world impact by connecting projects to local use cases.
- Close the knowledge gap on the environmental impact of state and non-state actors.
- Adapt and extend existing projects to underrepresented countries in the Global South.
- Create incubators and other support programmes for open source in environmental sustainability, including dedicated funds that provide core funding for development and maintenance.
- Develop better technical interfaces between platforms, data, models and open source tools across and within sectors to avoid “reinventing the wheel”.
- Standardise environmental data exchange across different levels of government.
- Transform financial institutions through transparent and scientific decision-making for sustainable investments.
- Apply an "Open Source First" criterion when providing funding for sustainable technologies.
- Recognise the contributions of open source in advancing sustainable development on a global scale.

<!-- 
- [ ] Enhance collaboration between state and non-state actors
- [x] Close the knowledge gap on the environmental impact of industry
- [x] Adapt and extend existing OSS to underrepresented countries in the Global South
- [x] Establish an open Earth Intelligence Incubator
- [x] Transform financial institutions through transparent and scientific decision-making for sustainable investments
- [x] Apply an "Open Source First" criterion when providing funding for sustainable technologies
- [x] Create better technical interfaces and middleware between platforms and tools
- [x] Standardise environmental data and models using open source across different levels of government.
- [ ] Develop Open Data Commons in conjunction with open source code
- [ ] Understand resources moving through supply chains using open source approaches
- [ ] Monitor environmental sustainability through open Earth observation and open source data processing
- [ ] Decarbonise power systems through digitalisation and open source
- [ ] Apply open sustainability principles to hardware and design blueprints
- [x] Connect projects to local use cases
- [x] Strengthen the interconnectivity of communities
- [x] Provide maintainers with training and support to preserve open source projects
- [ ] Create open communities for monitoring greenhouse gas emissions through remote sensing
- [ ] Maintain and defend an open orientation within academia
- [ ] Support the use of open source products and software development within government
- [x] Deploy dedicated funds for core development and maintenance
- [ ] Make open source a priority for government investment
- [ ] Embed open source principles within philanthropic and impact investment 
-->

Digital and sustainable transformation must converge as a digital public good if we are to achieve agreed environmental goals and create a safe and equitable corridor for people and the planet. **Openness provides the basis for collaborative sense-making, enables meaningful consensus – based on an accurate, shared understanding of the state of our planet – provides direction on how to best coordinate our choice-making, and builds capacity for effective action**. Open sustainability principles can help governments, research institutes, nongovernmental organisations, and businesses move quickly toward science-based decarbonisation and the conservation of natural resources and ecosystems by providing critical transparency, traceable decision-making, and collaboration on innovation.

---

## Project Data

`````{admonition} Tip
:class: tip
The plot is fully interactive. Drill into fields, topics, and projects via hovering your mouse! Click on the project names to jump to the repositories.
`````

```{code-cell} ipython3
:tags: [remove-input]


import numpy as np
import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go
import plotly.express as px

color_continuous_scale = px.colors.sequential.Aggrnyl[::-1]

df_active = pd.read_csv("../csv/project_analysis.csv")
# color_divergent_scale = [[0, '#dffe4b'], [0.5, '#f1f1f1'],[1, '#1a566a']]
fig = px.sunburst(
    df_active.assign(
        hole='<a href="https://opensustain.tech/" style = "color: black >Open Sustainable Technology</a>'
    ),
    path=["hole", "field", "topic", "project_name"],
    maxdepth=3,
    color="development_distribution_score",
    custom_data=["oneliner", "topic", "git_url"],
    # Diverging colors
    color_continuous_scale=color_continuous_scale,
    # color_continuous_midpoint=df_active['development_distribution_score'].median(),
)

fig.update_layout(
    coloraxis_colorbar=dict(title="Development Distribution Score",
    orientation='h',
    y=-0.15,
    x=0.5
    ),
    height=1000,
    width=850,
    title_font_size=22,
    font_size=12,
    dragmode=False,
)
# animated transitions are currently not implemented when uniformtext is used
fig.update_traces(
    insidetextorientation="radial",
    textinfo="label",
    marker=dict(line=dict(color="#000000", width=1)),
    hovertemplate="<br>".join(
        [
            "Project Info: <b>%{customdata[0]}</b>",
            "Topic: <b>%{customdata[1]}</b>",
            "Git URL: <b>%{customdata[2]}</b>",
        ]
    ),
)
fig.show()
```

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
[![](../images/subak.png)](https://subak.org/)
:::

:::{grid-item-card} 
[![](../images/protontypes_text_only.png)](https://github.com/protontypes)
:::

:::{grid-item-card} 
[![](../images/open_corridor.png)](https://www.opencorridor.org/)
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
To stay informed about this projects or to connect with the community please join our [Gitter Chat](https://gitter.im/protontypes/community), follow us on [Twitter](https://twitter.com/protontypes), [GitHub](https://github.com/protontypes) or [LinkedIn](https://de.linkedin.com/company/protontypes). 

## BibTeX Citation
```
@book{augspurger-malliaraki-hopkins,     
    Author     =  {Augspurger T., Malliaraki E., Hopkins J.},    
    Date-Added =  {2023-01-10},    
    Title      =  {Open Source in Environmental Sustainability},    
    Year       =  {2023}}   
```

---



## Table of Contents

```{tableofcontents}
```
