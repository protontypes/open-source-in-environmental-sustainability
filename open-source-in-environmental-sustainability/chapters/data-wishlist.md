# Data Wishlist

This is a list of datasets whose availability could accelerate progress or remove bottlenecks in different areas examined in this study. Since many open source projects subscribe to the concept of, and employ, other forms of openness, including open data, quantifying the available data stock based on this study's identified projects is possible in the future. This can help to create datasets on thematic priorities with temporal and geographical coverage.

This “wishlist” was obtained via interviews with project developers. Comparable [wishlists](https://www.climatechange.ai/dataset-wishlist.pdf) have previously been created by ClimateChangeAI. We classify potential datasets according to the topics selected within our study and the following types of data availability:
1. Public, needs structure
2. Private, needs to be released
3. Scattered, needs collation
4. Proxies, needs to be inferred
5. Scarce, needs collection

---
__Multicriteria data about bare-metal server manufacturing and their components.__

__Description:__
Measuring the power consumption of servers accounts for ~70% of the IT emissions. 30% of the footprint comes from server manufacturing. We cannot create comprehensive impact assessments without measuring resource depletion, the use of metals, the impact of resource extraction on biodiversity and people and the end of life of the product.

__Availability:__
1 and 4

__Next Steps:__

---
__Global detailed demographic data and Census breakdown at the city and neighbourhood level for transport planning interventions__

__Description:__
Analysis-ready census data for public transport simulations do not exist publicly. When planners simulate traffic, edit streets and intersections and plan bike networks, they need to investigate equity questions about any kind of intervention i.e. who is going to benefit from a low-traffic neighbourhood or see increased traffic. While census data sets are available in the US and the UK, they are cumbersome to work with i.e. parsing, merging two different census tracks or slicing them. Where they exist, they are expensive to licence.


__Availability:__
2 and 3


__Next Steps:__
Aggregate, contextualise, and standardise data from publicly available datasets

---

__Open UK map of curbside space— from parking meters, loading zones, curb cuts, and ramps to make the necessary changes for parking, ride-hail, and micro-mobility access for their community__

__Description:__
Curbs and their regulations have a significant impact on citizens and businesses daily. Curbs, for example, dictate where, when, and how long you can park, the dedicated use of a parking spot, such as loading, pick-up/drop-off, or accessible parking, and the type of vehicle a parking spot is reserved for (i.e. motorcycles, taxis, trucks), and so on. With so many different curb uses dispersed throughout a city, cities must have up-to-date information on curb assets that can then be incorporated into broader urban plans to make the most effective decisions to maximise a streetscape. Currently, the Ordnance survey holds curb data in the UK, which is not public. If the datasets were made public, the public sector would have the information required to make strategic decisions, advance policies, and respond to changing market dynamics with the same agility as their private sector counterparts.


__Availability:__
2 and 3


__Next Steps:__
Those data are available at a cost through various providers.

---

__Travel demand__

__Description:__
Traffic planning software requires detailed data on the trips that people take daily i.e. where they come from and where they go to. These can be built from aggregate census data, but they are hard to parse for transport simulations.


__Availability:__
2 and 3


---

__Electrical grid__

__Description:__
We need good data to tackle climate change. This data is available; it is published by the International Energy Agency (IEA). Despite being a largely public-funded organisation, a lot of IEA data is behind paywalls. Without it, subsectors and nations cannot accurately model their energy consumption or develop projections for usage in a range of scenarios, and they will ultimately be unable to manage their transition to zero-carbon economies. (OpenMod letter)


__Availability:__
2

__Next Steps:__
In certain parts of the United States, aggregated demand data may be publicly available through Independent System Operators or Regional Transmission Operators (ISOs/RTOs) and can simply be pulled from their websites. In the case where more granular data is needed, or in regions (within and outside the US) where such data is not public, it may be necessary to coordinate with relevant system operators.

---

__Consumer gas consumption__

__Description:__
Data on how much gas consumers use in their homes or industry doesn’t exist, and researchers are using heuristics to generate the data.


__Availability:__
4 and 2

---

__Gas grid infrastructure data (with a focus on the North Sea)__

__Description:__
To create more accurate IAMs and assess where wind turbines can be installed, researchers require spatially resolved demand datasets to be examined alongside data on shipping lanes and nature reserves, land restrictions, birdlife restrictions so that they can exclude certain areas from the models.


__Availability:__
2 and 3

__Next Steps:__
Environmental data for these kinds of assessments appear to be public sources for many regions, though they appear to be somewhat inaccessible, and the granularity of the measurements is unclear.

---

__Battery operation, electrical and mechanical response under many conditions__

__Description:__
There is a pressing need for more open battery data, including current, voltage, and capacity curves, operation cases and degradation information. Obtaining data for the entire lifetime of a battery with many batteries and many different conditions is time-consuming and expensive. The conditions that affect the lifecycle of batteries are complex and grow exponentially in size. While academic labs are willing to publish openly, industry (e.g car manufacturers) don’t want to share their proprietary data. Thus, academic labs working on battery modelling research are often constrained by not being able to compare their data with that of industry, and validating models becomes more difficult. This means researchers could be overfitting the battery models to the scant data available.

__Availability:__
3 and 2

__Next Steps:__
These datasets are available in various publications, so some degree of standardisation is required in addition to collection efforts.


---

__Wind Turbine Controllers (fixed and floating offshore wind turbines)__

__Description:__
The wind turbine systems research community uses reference controllers to compare and evaluate modern and advanced control algorithms and enable dynamic simulations in other wind turbine studies. Design constraints, such as blade tip deflection, have become increasingly important as wind turbines have grown and modelling tools have improved and increased in fidelity. Without a representative controller that performs consistently across turbine designs, dynamic simulations cannot provide reliable turbine design results. Reference wind turbine controllers are often difficult to modify for other turbines, making it difficult for researchers to run representative, fully dynamic simulations of other wind turbine designs. This is because the control software algorithms companies keep these data close. Any open commercial controllers or their data would be helpful in this line of research. To our knowledge, a modern, open source controller with specific logic for floating offshore wind turbines (FOWTs) is not available


__Availability:__
2


__Next Steps:__
Wind turbine modellers must collaborate with wind turbine companies and industrial manufacturers to create and/or access these datasets.

---

 ```{figure} ../images/emissions_api_small.jpeg
---
width: 100%
---
<br/>[Emissions API](https://emissions-api.org/)’s mission is to provide easy access to satellite based emissions data without the need of being an expert in satellite data analysis and without having to process terabytes of data.<br/>License: [MIT](https://github.com/emissions-api/emissions-api/blob/main/LICENSE)

 ```
