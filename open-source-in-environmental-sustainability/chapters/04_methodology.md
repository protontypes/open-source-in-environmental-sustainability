# Methodology 
Developing and maintaining open source software relies on an integration of technical, social and organisational aspects. A mixed methods study was therefore designed to understand all aspects. We collected quantitative and qualitative data concurrently and used one source's findings as cross-validation for the other. Thousands of projects were analysed along six dimensions:

- **General overview** - Project themes, growth, age and popularity, areas where projects are mature.

- **Technology -** Preferred programming languages, licence use and technical challenges facing developers.

- **Community** - What contributions from organisations and people are being made and how active is a community around a given software package.

- **Ecosystem collaborations** - What is the organisational makeup of contributions and what potential exists for more ecosystemic cooperation across and within sectors and disciplines.

- **Financial sustainability** - What is the use of different business models and funding mechanisms.

  ## Quantitative Analysis


From October 2020 until August 2022, ~1300 **actively** developed open source projects were crowdsourced and curated. All entries are selected based on the contribution [guide](https://opensustain.tech/contributing/) of OpenSustain.tech. For a project to be listed, it must:

- Follow at least one aspect of the Open Sustainability Principles. 
- Preserve natural ecosystems and mitigate climate & environmental change through open technology, methods, data, intelligence, knowledge or tools.
- Be used beyond the project's main developers
- Be structured and documented so that it can be reused and extended by others.
- Be published under an open source licence.

The project dataset is entirely machine-generated based on data from OpenSustain.tech and metadata from the GitHub API. The methodology and code used to parse and analyse the data are available in the [AwesomeCure](https://github.com/protontypes/AwesomeCure) repository. Several strategies were tested to include as many projects as possible in data collection using multiple keywords related to sustainable technology and environmental sustainability:

- Searching OSS platforms like Gitlab, Github, Bitbucket or Zenodo
- Mining scientific papers for terms like git, and searching in each paper’s keyword dictionary using search engines for OSS, such as Libraries.io and package managers such as PyPi or CRAN.
- Investigating OSS related journals such as the [Journal of Open Source Software](https://joss.theoj.org/) 
- Crowdsourcing input, and interviewing people working in relevant domains
- Browsing stars awarded by developers

Despite extensive research and a comprehensive use of complementary strategies, this database is only representative of a subset of projects. We must acknowledge that several technological developments relevant to OSS in environmental sustainability are not directly aimed at analysing or improving environmental sustainability; instead, they provide the technical foundation for software tools that can. The lines here are frequently blurred, and the extent to which a development contributes to environmental sustainability is difficult to predict. For example, a geoscience development that contributes to the exploitation of oil fields could also contribute to the exploitation of geothermal energy.

Furthermore, some important attributes, such as the number of clones and downloads could not be collected via the GitHub API. Projects hosted on self-hosted Git platforms are also more difficult to find. While not currently supported, future re-analysis will consider other platforms, such as GitLab, more extensively. The number of dependencies is another important attribute, indicative of the size and growth of a project and we were able to obtain this data for Python projects via GitHub using a web crawler. Other data, such as user permissions, cannot be viewed in individual projects without additional authorisation. For this reason, governance structures in most open source projects are difficult to determine. Individuals who did not contribute code were excluded from our analyses. Even if such contributions are critical, they cannot be obtained through the GitHub API. 

  ## Qualitative Analysis

**OSS communities are keystone actors of OSS projects**, and projects are typically initiated by an individual or a small group with a specific need often not being met satisfactorily by existing software. We conducted 15 interviews with project developers and contributors from projects of variable sizes and sectors, including on emission intensity, sustainable Investment, climate modelling, green software, earth sciences, energy modelling, photovoltaic systems, battery modelling, wind turbines, environmental sciences and transportation. Because we used a concurrent rather than sequential triangulation strategy, we had the opportunity to revisit and enhance our model to account for information revealed by the interviews. We drew inspiration from the questions asked in [Roadwork ahead](https://recommendations.implicit-development.org/) to enquire about the developers’ challenges, incentives, needs, the financial viability of their projects, and the barriers that have hampered the development of best practices. We asked about:

  - **Trajectories and positions in OSS** *(What are you working on, and how did you end up there? Where do you see your project related to the broader open sustainable ecosystem)*
  - **Technology & support** *(What open datasets and tools are you missing? What do you need to maintain your project in the near term?)*
  - **Community** *(How many users does your project have, and how is this metric tracked? What efforts are made to build a diverse developer base? What is the developer model? How are developers retained?)*
  - **Collaboration** *(In which field would you like to see more collaboration?)*
  - **Financial Sustainability** *(What efforts are being made to reach your definition of sustainability? What are your sources of funding or sponsorship?)*
  - **Future outlook** *(Do you see your project being widely used by your community in the future? What are the top 5 open sustainable projects on your radar?)*

 ```{figure} ../images/yukon.png
---
width: 100%
---
Beaver Creek, a tributary to the Yukon River, Alaska, USA. Visualization created with the Open Source Python package [RiverREM](https://github.com/OpenTopography/RiverREM)
 ```
