# Methodology 
Developing and maintaining open source software relies on an integration of technical, social and organisational aspects. A mixed methods study was therefore designed to understand all aspects. We collected quantitative and qualitative data concurrently and used one source's findings as cross-validation for the other. 
Thousands of projects were analysed along six dimensions:

- **General overview** - Project themes, growth and popularity, areas where projects are mature and where tools or processes exist that funders should support instead of forging a new path.

- **Technology -** Preferred programming languages, licence use and technical challenges facing developers.

- **Community** - What contributions from organisations and people are being made and how active is a community around a given software package.

- **Ecosystem collaborations** - What is the organisational makeup of contributions and what potential exists for more ecosystemic cooperation across and within sectors and disciplines.

- **Financial sustainability** - What is the different use of business models and funding mechanisms.

  ## Quantitative Analysis

  From October 2020 until August 2022, ~1300 **actively** developed open source projects were crowdsourced and curated. All entries are selected based on the contribution [guide](https://opensustain.tech/contributing/) of OpenSustain.tech. For a project to be listed, it must:

  - Follow at least one aspect of the Open Sustainability Principles 
  - Preserve natural ecosystems and mitigate climate & environmental change through open technology, methods, data, intelligence, knowledge or tools
  - Be used beyond the project's main developers. Be structured and documented so that it can be reused and extended by others.Be published under an open source licence.
  - The project dataset is entirely machine-generated based on data from OpenSustain.tech and the metadata from the GitHub API. The methodology and code with which the data is parsed and analysed can be found in the [AwesomeCure](https://github.com/protontypes/AwesomeCure) repository. 

  Various strategies were piloted to include as many projects as possible in data collection based on multiple keywords in relation to sustainable technology and environmental sustainability:

  - Searching OSS platforms like Gitlab, Github, Bitbucket or Zenodo
  - Mining scientific papers for terms like git, and searching in each paper’s keyword dictionary Using search engines for OSS, such as Libraries.io; and package managers such as PyPi or CRAN
  - Investigating journals focused on OSS such as the [Journal of Open Source Software](https://joss.theoj.org/) 
  - Crowdsourcing input, and interviewing people working in relevant domains
  - Browsing stars awarded by developers within the sectors 

  Despite extensive research and a comprehensive use of complementary strategies, this database is only representative of a subset of projects. We must acknowledge that a variety of technological developments of relevance to OSS in the domain of environmental sustainability are not directly aimed at analysing or improving the sustainability of the environment; rather, they provide the technical basis for software tools that can. This applies, for example, in domains such as earth observation or geographic information systems (GIS). The boundaries here are often fluid, and the extent to which a development contributes to environmental sustainability cannot be clearly predicted. For example, a geoscience development that contributes to the exploitation of oil fields could also contribute to the exploitation of geothermal energy. 

  Moreover, projects that are on self-hosted Git platforms are harder to find. While currently not supported, future re-analysis will consider other platforms, such as GitLab, more extensively. Also some important attributes could not be collected via the GitHub API – for example: the number of clones or the number of downloads. For Python and R, these numbers could be freely obtained via the package platform. However, the integration of this data was not possible until now. 

  The number of dependencies is another important attribute, indicative of the size and growth of a project. We were able to obtain this data for Python projects via GitHub using a web crawler; Something that was not possible during the study via the GitHub API Referring to open source projects within publications has also unfortunately been uncommon up to now, making it difficult to find out via citations how much a project has been reused.


  Other data, such as user permissions, cannot be viewed within individual projects without additional authorisation. For this reason, governance structures in most open source projects are difficult to determine. Individuals who did not contribute code were also invisible to our analyses. Even if such contributions are of central importance, it is not possible to obtain them simply via the GitHub API. For individual open source projects, it is possible to process all pull requests and issue comments to obtain more information about non-code contributors but even in this way other persons working in the background can not be included.

  ## Qualitative Analysis

  **OSS communities are keystone actors of OSS projects, and projects are typically initiated by an individual or a small group with a specific need** often not being met satisfactorily by existing software. We began our research with these individuals. 15 interviews were conducted with project developers and contributors from projects of variable sizes and sectors, including on emission intensity, sustainable Investment, climate modelling, green software, earth sciences, energy modelling, photovoltaic systems, battery modelling, wind turbines, environmental sciences and transportation.

  Because we used a concurrent rather than sequential triangulation strategy, we had the opportunity to revisit and enhance our model to account for information revealed by the interviews. We drew inspiration from the questions asked in [Roadwork ahead](https://recommendations.implicit-development.org/) to enquire about the developers’ challenges, incentives, needs, the financial viability of their projects, and the barriers that have hampered the development of best practices and more equitable developer communities. We asked about:

  - **Trajectories and positions in OSS** *(What are you working on, and how did you end up there? Where do you see your project related to the broader open sustainable ecosystem)*
  - **Technology & support** *(What open datasets and tools are you missing? What do you need to maintain your project in the near term?)*
  - **Community** *(How many users does your instrument have, and how is this metric tracked? What efforts are made to build a diverse developer base? What is the developer model? How are developers retained?)*
  - **Collaboration** *(In which field would you like to see more collaboration?)*
  - **Financial Sustainability** *(What efforts are being made to reach this definition of sustainability? From what sources do projects receive funding or sponsorship?)*
  - **Future outlook** *(Do you see your instrument being widely used by your community in the future? What are the top5 open sustainable projects on your radar?)*

 ```{figure} ../images/yukon.jpg
---
height: 400px
---
Beaver Creek, a tributary to the Yukon River, Alaska, USA. Visualization created with the Open Source Python package [RiverREM](https://github.com/OpenTopography/RiverREM)
``` 
