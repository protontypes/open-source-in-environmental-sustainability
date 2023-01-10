# Open Source in Environmental Sustainability
**Preserving climate and natural resources with openness.**
<img src="./open-source-in-environmental-sustainability/images/mycelium_sustainability.png" align="right" width="300">

This study provides the first analysis of the open source software ecosystem in sustainability and climate technology. Thousands of actively developed open source projects and organisations have been collected through the [Open Sustainable Technology](https://opensustain.tech/) project and systematically analysed using qualitative and quantitative methods. The collected raw data can be browsed [here](https://airtable.com/shr9we419r2TkpLkc). 

The analysis covers multiple dimensions – including the technical, the social, and the organisational. It highlights key risks and challenges for users, developers, and decision-makers as well as opportunities for more systemic collaboration. The data acquisition and generation of the plots is almost completely automated. Thus, the study can be repeated in the future. 

## Usage

### Reading the book
To help you navigate and to give you a better overview of the ecosystem, all plots are interactive. Project and organisation names are linked within the plots. The book can be read on the following URL: 

[https://report.opensustain.tech/](https://report.opensustain.tech/)

### Building the book

If you'd like to develop and/or build the Open Source in Environmental Sustainability book, you should:

1. Clone this repository
2. Run `pip install -r requirements.txt` (it is recommended you do this within a virtual environment)
3. Run `jupyter-book clean open_source_in_environmental_sustainability/` to remove any existing builds
4. Run `jupyter-book build open_source_in_environmental_sustainability/`

### Update the database

All plots are based on the CSV files in the `open-source-in-environmental-sustainability/csv/` folder. The [AwesomeCure](https://github.com/protontypes/AwesomeCure) projects is used to update and recreate the raw data of this study. Just place the new `projects.csv` and `github_organizations.csv` files into the CSV folder. The only data that is not automatically generated are the `form_of_organization` and `location_country`.

## How to Contribute

More than ever, free and open source projects are enabling citizens, scientists, developers, civil society, industry and government to mitigate climate change. Funders have the opportunity to play an active role in promoting a larger, more systematic shift towards open, community-driven infrastructure at the institutional level. We want to hear from you if you:

- Have experience developing, supporting or systematically using open source software for sustainability applications.
- Want to [contribute](https://opensustain.tech/contributing/) to OpenSustain.tech by identifying new and missing projects.
- Have experience visualising or processing data with Python and know how to integrate such data into a new website.
- Are a funder and want to support these developer communities via open infrastructure funds, consortia-based support or other collaborative models across institutions and regions.
- Want to help us build any of the recommendations and future directions of OpenSustain.tech.

## BibTeX Citation
```
@book{augspurger-malliaraki-hopkins,     
    Author     =  {Augspurger T., Malliaraki E., Hopkins J.},    
    Date-Added =  {2023-01-10},    
    Title      =  {Open Source in Environmental Sustainability},    
    Year       =  {2023}}   
```
