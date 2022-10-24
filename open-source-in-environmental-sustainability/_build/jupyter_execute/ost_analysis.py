#!/usr/bin/env python
# coding: utf-8

# # Open Source in Environmental Sustainability

# In[1]:


from IPython.display import display, HTML

import dateparser
import datetime
import handcalcs.render
import numpy as np
import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go
import plotly.express as px
import pycountry
from pycountry_convert import country_alpha2_to_continent_code, country_alpha3_to_country_alpha2


# In[2]:


### KK: add simple docstrings

# Clean up the dataset
def name_to_iso3(x):
    # fuzzy search does not like UK
    if x == "UK":
        x = "United Kingdom"
    try:
        iso3 = pycountry.countries.search_fuzzy(x)[0].alpha_3
    except:
        iso3 = ""
    return iso3

def alpha3_to_alpha2(x):
    try:
        alpha_2 = country_alpha3_to_country_alpha2(x)
    except:
        alpha_2 = ""
    return alpha_2

def alpha2_to_continent(x):
    try:
        continent = country_alpha2_to_continent_code(x)
    except:
        continent = ""
    return continent


def upper_string(lower_string):
    return lower_string.title()

def calc_age(x):
    return (datetime.datetime.now() - dateparser.parse(x, settings={'TIMEZONE': 'CEST'})).days/365

def count_strings(comma_seperated_string):
    if type(comma_seperated_string) == str:
        return comma_seperated_string.count(",")
    else:
        return 0


# ### Set Default Plotting Options 

# In[3]:


# default plotting options
# Palette https://coolors.co/palette/0e7c7b-17bebb-ffc857-e9724c-c5283d
height = (800,)  # Added parameter
color_continuous_scale = px.colors.sequential.Aggrnyl[::-1]
marker_color = "#0E7C7B"
color_discrete_sequence = ["#0E7C7B", "#17BEBB", "#FFC857", "#E9724C", "#C5283D"]

# Register your theme as a named template
pio.templates["OpenSustain"] = go.layout.Template(
    layout=dict(
        font=dict(
            family="Google Font",
            color="#040404",
            size=15,
        ),
        title_font_family="Google Font",
        title_font_color="#040404",
        legend_title_font_color="#040404",
    ),
)

# Combine your theme with plotly's default
pio.templates.default = "plotly+OpenSustain"


# In[4]:


df_raw = pd.read_csv("./csv/projects.csv")
df_raw.head(5)


# ## Calculate Age in Years

# In[5]:


## KK: I would suggest using a clearer object-naming convention. Below it becomes unclear what's the difference between df and df_raw
# Age plots are better in years
df_raw["project_age_in_years"] = df_raw["project_age_in_days"].apply(lambda x: x / 365)
max_age_in_years = 8.0


# ## Basis Statistics
# First let us get a routh overview of the project dataset
# 

# In[6]:


fig = go.Figure(
    data=[
        go.Table(
            header=dict(values=["Dimension", "Value"],line_color='#000000',
                        fill_color='#ffffff', font_size=18 ,  ),
            cells=dict(
                        fill_color='#ffffff',
                        line_color='#ffffff',
                        font_size=16,
                        height=30,
                values=[
                    [
                        "Total number of projects",
                        "Github projects",
                        "Gitlab projects",
                        "Other platforms",
                        "Number of projects in personal namespace",
                        "Total stars of all projects",
                        "Total contributers of all projects",
                        "Active GitHub projects",
                        "Inactive GitHub projects",
                        "Projects with contribution guide in %",
                        "Projects with code of conduct in %",
                        "Projects accepting donations in %",
                        "Median number of commits",
                        "Median stargazers",
                        "Median stars last year",
                        "Median Development Distribution Score",
                        "Median number of contributors",
                        "Median closed issues last year",
                        "Median commits last year",
                        "Median age in years",
                    ],
                    [
                        df_raw["project_name"].count(),
                        df_raw["platform"].value_counts()["github"],
                        df_raw["platform"].value_counts()["gitlab"],
                        df_raw["platform"].value_counts()["custom"],
                        df_raw["project_name"].count() - df_raw["organization"].count(),
                        df_raw["stargazers_count"].sum(),
                        df_raw["contributors"].sum(),
                        df_raw["project_active"].value_counts()[True],
                        df_raw["project_active"].value_counts()[False],
                        round(df_raw["contribution_guide"].value_counts(normalize=True)[True]*100,2),
                        round(df_raw["code_of_conduct"].value_counts(normalize=True)[True]*100,2),
                        round(df_raw["accepts_donations"].value_counts(normalize=True)[True]*100,2),
                        df_raw["total_number_of_commits"].median(),
                        df_raw["stargazers_count"].median(),
                        df_raw["stars_last_year"].median(),
                        round(df_raw["development_distribution_score"].median(),4),
                        df_raw["contributors"].median(),
                        df_raw["issues_closed_last_year"].median(),
                        df_raw["total_commits_last_year"].median(),
                        round(df_raw["project_age_in_years"].median(),2),
                        
                    ],
                ]
            ),
        )
    ]
)



fig.update_layout(
height=1000,
width=1000
)
fig.show()


# ## Development Distribution Score
# 
# The Development Distribution Score (DDS) weights how the development is distributed between projects contributors by setting contributor with the most commits in relation with the other contributors. Distribution of knowledge, work, and governance of an project ensure sustainability. When people are leaving a project or don't find time anymore for an open source project other can still continue and jump into leading positions. 
# 
# DDS is created in the preprocessing script and is similar to the bus factor.
# It is only based on quantiative values derived from git statistics. This value is calculated in preprocessing.
# 
# 

# ## Filter Data 

# In[7]:


df_active = df_raw.copy()
# Filter out the inactive project for further analysis
df_active = df_active[(df_active["project_active"] == True)]
# Ciruated Lists are no classical open source projects and are not included into the analysis
df_active = df_active[(df_active["rubric"] != "Curated Lists")]
# Filter out the projects not on the GitHub platform
df_active = df_active[(df_active["platform"] == "github")]


# ## Score Projects 

# In[8]:


# Calculate the scores on activity, community and size
df_active["activity"] = (
    df_active["total_commits_last_year"].rank(pct=True)
    + df_active["issues_closed_last_year"].rank(pct=True)
    + df_active["days_until_last_issue_closed"].rank(pct=True)
    + df_active["last_released_date"].rank(pct=True, na_option="top")
)

df_active["community"] = (
    df_active["contributors"].rank(pct=True)
    + df_active["development_distribution_score"].rank(pct=True)
    + df_active["reviews_per_pr"].rank(pct=True)
)

df_active["size"] = (
    df_active["total_number_of_commits"].rank(pct=True)
    + df_active["contributors"].rank(pct=True)
    + df_active["closed_issues"].rank(pct=True)
    + df_active["closed_pullrequests"].rank(pct=True)
)

# All scores are weighted equal and normalized to one
df_active["total_score"] = (
    df_active["activity"] / df_active["activity"].max()
    + df_active["community"] / df_active["community"].max()
    + df_active["size"] / df_active["size"].max()
) / 3


# In[9]:


# Save the dataset with the scores
df_active_path = "./csv/project_analysis.csv"
df_active.to_csv(df_active_path)


# In[10]:


get_ipython().run_cell_magic('render', '', '## The calcluation within this cell shall reader give an understanding on how the DDS is been calculated. \n## Values calculated here are not used in any other cell.\nn_MaxCommitsSingleContributor = 90\nn_total_commits = 100\n\n\nDDS = 1 - n_MaxCommitsSingleContributor / n_total_commits\n')


# In[11]:


### KK: this is where a clear object naming convention + comments would really help: is syntax df[df_raw[..]] appropriate here? 
### KK: it might be helpful to plot boxplots for the below scores per category to better show their distribution, including median

df_personal_projects = df_active[df_active["organization"].isna()]
df_organization_projects = df_active[df_active["organization"].notna()]
df_inactive = df_raw[(df_raw["project_active"] == False)]
df_top_stargazers = df_active[(df_active["stargazers_count"] > 100)]

fig = go.Figure(
    data=[
        go.Table(
            header=dict(values=["Median DDS", "Value"],line_color='#000000',fill_color='#ffffff',font_size=18),
            cells=dict(
                        line_color='#ffffff',fill_color='#ffffff', font_size=16, height =30,
                values=[
                    [
                        "All projects",
                        "Active projects in personal namespace",
                        "Active organization projects",
                        "Active projects",
                        "Inactive projects",
                        "Active projects with more than 50 Stars",

                    ],
                    [
                        round(df_raw["development_distribution_score"].median(),3),
                        round(df_personal_projects["development_distribution_score"].median(),3),
                        round(df_organization_projects["development_distribution_score"].median(),3),
                        round(df_active["development_distribution_score"].median(),3),
                        round(df_inactive["development_distribution_score"].median(),3),
                        round(df_top_stargazers["development_distribution_score"].median(),3),
                    ],
                ]
            ),
        )
    ]
)

fig.update_layout(
width=800

)

fig.show()


# In[12]:


df_active.iloc[300]


# ## Process Active GitHub Projects

# In[13]:


# Read the scored dataset and configure the plotting backend
df_active = pd.read_csv(df_active_path)


# # Start Plotting

# In[14]:


license_his = (
    df_active["license"]
    .value_counts()
    .to_frame()
    .rename_axis("license_names")
    .reset_index()
)
fig = px.pie(license_his, values="license", names="license_names", color_discrete_sequence=color_discrete_sequence, hole=0.2)

fig.update_layout(title="Distribution of Licenses", showlegend=True, font_size=16)
fig.update_traces(textposition='inside', textinfo='percent+label', marker=dict(line=dict(color='#000000', width=1)))
fig.show()


# In[15]:


fig = px.histogram(
    df_active,
    x="project_age_in_years",
    nbins=50,
    title="Distribution of Project Age in Years",
)
fig.update_layout(
    yaxis_title="Projects",
    xaxis_title="Project Age",
)
fig.update_traces(marker_color=marker_color)
fig.show()


# In[16]:


fig = px.histogram(
    df_active,
    x="total_number_of_commits",
    nbins=50,
    title="Distribution of Total Commits",
)
fig.update_layout(
    yaxis_title="Projects",
    xaxis_title="Project Total Commits",
)
fig.update_traces(marker_color=marker_color)
fig.show()


# In[17]:


rubric_his = (
    df_active["rubric"]
    .value_counts()
    .to_frame()
    .rename_axis("rubric_names")
    .reset_index()
)
fig = px.pie(rubric_his, values="rubric", names="rubric_names", color_discrete_sequence=color_discrete_sequence, hole=0.2)

fig.update_layout(title="Projects within Rubrics", height=1200, showlegend=False)
fig.update_traces(textposition='outside', textinfo='value+label', marker=dict(line=dict(color='#000000', width=2)))
fig.show()



# In[18]:


fig = px.pie(df_active.groupby('rubric')['contributors'].sum().reset_index(), values="contributors", names="rubric", color_discrete_sequence=color_discrete_sequence, hole=0.2)

fig.update_layout(title="Contributors within Rubrics", height=1200, showlegend=False)
fig.update_traces(textposition='outside', textinfo='value+label', marker=dict(line=dict(color='#000000', width=2)))
fig.show()


# In[19]:


fig = px.pie(df_active.groupby('rubric')['stargazers_count'].sum().reset_index(), values="stargazers_count", names="rubric", color_discrete_sequence=color_discrete_sequence, hole=0.2)

fig.update_layout(title="Stars within Rubrics", height=1000, showlegend=False)
fig.update_traces(textposition='outside', textinfo='value+label', marker=dict(line=dict(color='#000000', width=2)))
fig.show()


# In[20]:


fig = px.pie(df_active.groupby('rubric')['development_distribution_score'].median().reset_index(), values="development_distribution_score", names="rubric", color_discrete_sequence=color_discrete_sequence, hole=0.2)

fig.update_layout(title="Median Development Distribution Score within Rubrics", height=1000, showlegend=False)
fig.update_traces(textposition='outside', textinfo='value+label', marker=dict(line=dict(color='#000000', width=2)))
fig.show()


# In[21]:


fig = px.pie(df_active.groupby('rubric')['stars_last_year'].sum().reset_index(), values="stars_last_year", names="rubric", color_discrete_sequence=color_discrete_sequence, hole=0.2)

fig.update_layout(title="Stars within Rubrics", height=1200, showlegend=False)
fig.update_traces(textposition='outside', textinfo='value+label', marker=dict(line=dict(color='#000000', width=2)))
fig.show()


# In[22]:


license_dominating_language = (
    df_active["dominating_language"]
    .value_counts()
    .to_frame()
    .rename_axis("dominating_language_names")
    .reset_index()
)
license_dominating_language
license_dominating_language = license_dominating_language[(license_dominating_language["dominating_language"] > 4)]
fig = px.pie(license_dominating_language, values="dominating_language", names="dominating_language_names", color_discrete_sequence=color_discrete_sequence, hole=0.2)

fig.update_layout(title="Distribution of Programming Languages", showlegend=True, font_size=16,height=800)
fig.update_traces(textposition='outside', textinfo='percent+label', marker=dict(line=dict(color='#000000', width=1)))
fig.show()


# In[23]:


# df_sorted = df.groupby(['rubric'], as_index=False)['dominating_language'].agg('sum')
df_language_distribution = (
    df_active.value_counts(["rubric", "dominating_language"]).to_frame().reset_index()
)

df_language_distribution.rename(columns={0: "counts"}, inplace=True)
fig = px.scatter(
    df_language_distribution, x="dominating_language", y="rubric", size="counts", 
)


fig.update_layout(
    height=1000,  # Added parameter
    xaxis_title="Dominating Language",
    yaxis_title="Rubric",
)
fig.update_traces(marker_color=marker_color)


fig.show()


# In[24]:


# df_sorted = df.groupby(['rubric'], as_index=False)['dominating_language'].agg('sum')
df_license_distribution = (
    df_active.value_counts(["rubric", "license"]).to_frame().reset_index()
)

df_license_distribution.rename(columns={0: "counts"}, inplace=True)
fig = px.scatter(df_license_distribution, x="license", y="rubric", size="counts")


fig.update_layout(
    height=1000,  # Added parameter
    xaxis_title="License",
    yaxis_title="Rubric",
    title="License Distribution over Rubric",
    autosize=True,
)
fig.update_traces(marker_color=marker_color)


fig.show()


# In[25]:


fig = px.histogram(
    df_active,
    x="contributors",
    nbins=100,
    title=" Contributors",
)
fig.update_layout(
    yaxis_title="Projects",
    xaxis_title="Contributors",
)
fig.update_traces(marker_color=marker_color)
fig.show()


# In[26]:


most_listed_projects = df_active["git_namespace"].value_counts(ascending=False).to_frame().rename_axis("Namespace").reset_index().rename(columns={"git_namespace": "counts"})
fig = go.Figure(data=[go.Table(
    header=dict(values=list(most_listed_projects.columns), line_color='#000000', fill_color='#ffffff',font_size=18 ),
    cells=dict(line_color='#ffffff', fill_color='#ffffff', font_size=16, height=30, values=[most_listed_projects.Namespace, most_listed_projects.counts])
)])

fig.update_layout(
autosize=False,
)

fig.show()


# In[27]:


oldest_projects = df_active.nlargest(40, "project_age_in_years")


fig = px.bar(
    oldest_projects,
    x=oldest_projects["project_age_in_years"],
    y=oldest_projects["project_name"],
    orientation="h",
    range_x=(9.6, 14),
    hover_name=oldest_projects["git_url"],
    hover_data=["oneliner","rubric","git_namespace"],
    color=oldest_projects["development_distribution_score"],
    color_continuous_scale=color_continuous_scale
)

fig.update_layout(
    height=1000,  # Added parameter
    yaxis_title="Rubric",
    xaxis_title="Project Age in Years",
    title="The oldest Projects still active",
    coloraxis_colorbar=dict(
    title="DDS",
    ),
    hoverlabel=dict(
    bgcolor="white"
    )
)



fig.update(layout_showlegend=False)


# In[28]:


contributors = df_active.nlargest(40, "contributors")

fig = px.bar(
    contributors,
    x=contributors["contributors"],
    y=contributors["project_name"],
    orientation="h",
    title="Projects with most contributors",
    hover_name=contributors["git_url"],
    hover_data=["oneliner","rubric","git_namespace"],
    color=contributors["development_distribution_score"],
    color_continuous_scale=color_continuous_scale
)

fig.update_layout(
    height=1200,  # Added parameter
    xaxis_title="Contributors",
    yaxis_title="Project",
    title="Projects with the most contributors",
    coloraxis_colorbar=dict(
    title="DDS",
    ),
    hoverlabel=dict(
    bgcolor="white"
    )
)

fig.update(layout_showlegend=False)


# In[29]:


top_stargazers = df_active.nlargest(40, "stargazers_count")

fig = px.bar(
    top_stargazers,
    x=top_stargazers["stargazers_count"],
    y=top_stargazers["project_name"],
    orientation="h",
    hover_name=top_stargazers["git_url"],
    hover_data=["oneliner","rubric","git_namespace"],
    color=top_stargazers["development_distribution_score"],
    color_continuous_scale=color_continuous_scale

)

fig.update_layout(
    height=1000,  # Added parameter
    xaxis_title="Stars",
    yaxis_title="Project",
    title="Projects with the most Stars",
    coloraxis_colorbar=dict(
    title="DDS",
    ),
    hoverlabel=dict(
    bgcolor="white"
    )
)

fig.update(layout_showlegend=False)


# In[30]:


df_top_100_stargazers = df_active[(df_active["stargazers_count"]) > 100].copy()
df_top_100_stargazers["star_growth"] = (
    df_top_100_stargazers["stars_last_year"] / df_top_100_stargazers["stargazers_count"]
)

df_top_40_star_growth = df_top_100_stargazers.nlargest(40, "star_growth")
fig = px.bar(
    df_top_40_star_growth,
    x=df_top_40_star_growth["star_growth"] * 100,
    y=df_top_40_star_growth["project_name"],
    orientation="h",
    hover_name=df_top_40_star_growth["git_url"],
    hover_data=["oneliner","rubric","git_namespace"],
    color=df_top_40_star_growth["development_distribution_score"],
    color_continuous_scale=color_continuous_scale
)

fig.update_layout(
    height=1000,  # Added parameter
    xaxis_title="Star Growth last Year [%]",
    yaxis_title="Project",
    title="Projects with the highest Star Growth",
    hoverlabel=dict(
    bgcolor="white"
    )
)


# In[31]:


df_top_40_growth = df_active.nlargest(40, "total_commits_last_year")
df_top_40_growth = df_top_40_growth[df_top_40_growth["project_name"] != "ElexonDataPortal"]
fig = px.bar(
    df_top_40_growth,
    x=df_top_40_growth["total_commits_last_year"],
    y=df_top_40_growth["project_name"],
    orientation="h",
    color=df_top_40_growth["development_distribution_score"],
    hover_name=df_top_40_growth["git_url"],
    hover_data=["oneliner","rubric","git_namespace"],
    color_continuous_scale=color_continuous_scale,
)

fig.update_layout(
    height=1000,  # Added parameter
    xaxis_title="Commit Growth last Year [%]",
    yaxis_title="Project",
    title="Projects with the highest Commit Growth",
    coloraxis_colorbar=dict(
    title="Rubric",
    ),
    hoverlabel=dict(
    bgcolor="white"
)
)


# In[32]:


df_total_score = df_active.nlargest(40, "total_score")

fig = px.bar(
    df_total_score,
    x=df_total_score["total_score"],
    y=df_total_score["project_name"],
    orientation="h",
    range_x=(0.85, 1),
    hover_name=df_total_score["git_url"],
    hover_data=["oneliner","rubric","git_namespace"],
    color = df_total_score["development_distribution_score"],
    color_continuous_scale=color_continuous_scale
)

fig.update_layout(
    height=1000,  # Added parameter
    xaxis_title="Total Score",
    yaxis_title="Project",
    title="Top Total Score",
    coloraxis_colorbar=dict(
    title="DDS",
    ),   
    hoverlabel=dict(
    bgcolor="white"
)
)
fig.update(layout_showlegend=False)


# In[33]:


df_activity_score = df_active.nlargest(40, "activity")

fig = px.bar(
    df_activity_score,
    x=df_activity_score["activity"],
    y=df_activity_score["project_name"],
    orientation="h",
    range_x=(2.9, 3.2),
    hover_name=df_activity_score["git_url"],
    hover_data=["oneliner","rubric","git_namespace"],
    color=df_activity_score["development_distribution_score"],
    color_continuous_scale=color_continuous_scale
)

fig.update_layout(
    height=1000,  # Added parameter
    xaxis_title="Activity Score",
    yaxis_title="Project",
    title="Projects with the highest Activity Score",
    coloraxis_colorbar=dict(
    title="DDS",
    ),
    hoverlabel=dict(
    bgcolor="white"
)
)

fig.update(layout_showlegend=False)


# In[34]:


df_size_score = df_active.nlargest(40, "size")

fig = px.bar(
    df_size_score,
    x=df_size_score["size"],
    y=df_size_score["project_name"],
    orientation="h",
    range_x=(3.75, 4),
    hover_name=df_size_score["git_url"],
    hover_data=["oneliner","rubric","git_namespace"],
    color=df_size_score["development_distribution_score"],
    color_continuous_scale=color_continuous_scale
)

fig.update_layout(
    height=1000,  # Added parameter
    xaxis_title="Size Score",
    yaxis_title="Project",
    title="Projects with the highest Size Score",
    coloraxis_colorbar=dict(
    title="DDS",
    ),
    hoverlabel=dict(
    bgcolor="white"
)
)

fig.update(layout_showlegend=False)


# In[35]:


fig = px.scatter(
    df_active.query("project_age_in_years<@max_age_in_years"),
    x="project_age_in_years",
    y="rubric",
    size="size",
    color="total_score",
    hover_name="git_url",
    hover_data=["oneliner","rubric","git_namespace"],
    size_max=20,
)

fig.update_layout(
    coloraxis_colorbar=dict(title="Total Score"),
    height=1000,  # Added parameter
    xaxis_title="Project Age in Years",
    yaxis_title="Rubric",
    title="Total Score of Projects",
    hoverlabel=dict(
    bgcolor="white"
)
)


fig.show()


# In[36]:


fig = px.scatter(
    df_organization_projects.query("project_age_in_years<@max_age_in_years"),
    x="project_age_in_years",
    y="rubric",
    size="size",
    color="development_distribution_score",
    hover_name="git_url",
    hover_data=["oneliner","rubric","git_namespace"],
    size_max=20,
)

fig.update_layout(
    coloraxis_colorbar=dict(
        title="DDS",
    ),
    yaxis_title="Rubric",
    xaxis_title="Project Age in Years",
    height=1000,  # Added parameter
    title="Development Distribution Score",
    hoverlabel=dict(
    bgcolor="white"
)
)
fig.show()


# In[37]:


personal_stargazers = df_personal_projects.nlargest(40, "stargazers_count")

fig = px.bar(
    personal_stargazers,
    x=personal_stargazers["stargazers_count"],
    y=personal_stargazers["git_namespace"],
    orientation="h",
    hover_name=personal_stargazers["git_url"],
    hover_data=["oneliner","rubric","git_namespace"],
    color=personal_stargazers["development_distribution_score"],
    color_continuous_scale=color_continuous_scale
)

fig.update_layout(
    height=1000,  # Added parameter
    yaxis_title="Rubric",
    xaxis_title="Stars",
    title="Projects with most Stars in User Namespace",
    coloraxis_colorbar=dict(
    title="DDS",
    ),
    hoverlabel=dict(
    bgcolor="white"
)
)


fig.update(layout_showlegend=False)


# In[38]:


df_active["dependents_count"] = df_active["dependents_repos"].apply(count_strings)

most_dependent_projects = df_active.nlargest(50, "dependents_count")
most_dependent_projects = most_dependent_projects[most_dependent_projects["project_name"] != "Mission Support System"]
print("DDS of most used Python project:",round(most_dependent_projects["development_distribution_score"].median(),3))


fig = px.bar(
    most_dependent_projects,
    x=most_dependent_projects["dependents_count"],
    y=most_dependent_projects["project_name"],
    orientation="h",
    hover_name=most_dependent_projects["git_url"],
    hover_data=["oneliner","rubric","git_namespace"],
    color=most_dependent_projects["development_distribution_score"],
    color_continuous_scale=color_continuous_scale
)

fig.update_layout(
    height=1000,  # Added parameter
    yaxis_title="Rubric",
    xaxis_title="Dependents",
    title="Most used Python Projects vs. DDS",
    coloraxis_colorbar=dict(
    title="DDS",
    ),
    hoverlabel=dict(
    bgcolor="white"
)
)


# ## Process the organizations

# In[39]:


df_organizations = pd.read_csv("./csv/github_organizations.csv")
df_organizations.head()


# In[40]:


df_organizations["ISO_3"] = df_organizations["location_country"].apply(name_to_iso3)
df_organizations["ISO_3_alpha2"] = df_organizations["ISO_3"].apply(alpha3_to_alpha2)
df_organizations["continent"] = df_organizations["ISO_3_alpha2"].apply(alpha2_to_continent)


# In[41]:


continent_his = df_organizations["continent"].value_counts().to_frame().rename_axis("continent_name")
continent_his.rename(index={"EU": "Europe", "NA": "North America", "": "Global", "OC":"Oceania", "AS":"Asia", "SA":"South America", "AF":"Africa"},inplace=True)

print(continent_his)
fig = px.pie(continent_his.reset_index(), values="continent", names="continent_name", color_discrete_sequence=color_discrete_sequence, hole=0.2)

fig.update_layout(title="Distribution of Organizations between Continents", font_size=16)
fig.update_traces(textposition='outside', textinfo='value+label', marker=dict(line=dict(color='#000000', width=2)))
fig.show()


# In[42]:


## https://octoverse.github.com/
values = {31.5,31.2,27.3,5.9,2.3,1.7}
index_labels=['Oceania','Africa','South America','Europe','Asia','North America']
df_users_continent_cotoverse = pd.DataFrame(values,index=index_labels).reset_index()


# In[43]:


fig = px.pie(df_users_continent_cotoverse, values=0, names="index", color_discrete_sequence=color_discrete_sequence, hole=0.2)

fig.update_layout(title="Distribution of Users between Continents", font_size=16)
fig.update_traces(textposition='outside', textinfo='value+label', marker=dict(line=dict(color='#000000', width=2)))
fig.show()


# In[44]:


organization_his = (
    df_organizations["form_of_organization"]
    .value_counts()
    .to_frame()
    .rename_axis("organization")
    .reset_index()
)

organization_his["organization"] = organization_his["organization"].apply(upper_string)
print(organization_his)
fig = px.pie(organization_his, values="form_of_organization", names="organization", color_discrete_sequence=color_discrete_sequence, hole=0.2)

fig.update_layout(title="Distribution of Organizational Forms", font_size=16)
fig.update_traces(textposition='outside', textinfo='percent+label', marker=dict(line=dict(color='#000000', width=2)))
fig.show()


# In[45]:


df_countries = (
    df_organizations["ISO_3"]
    .value_counts()
    .to_frame()
    .rename_axis("country")
    .reset_index()
)
df_countries = df_countries.rename(columns={"ISO_3": "counts"})

fig = px.choropleth(
    df_countries,
    locations="country",
    locationmode="ISO-3",
    color="counts",
    color_continuous_scale=color_continuous_scale
)

fig.update_layout(title="Distribution of Organizational Locations Worldwide",
                    coloraxis_colorbar=dict(
                    title="Organizations",
                    ),)

fig.show()


# In[46]:


df_public_repos = df_organizations.nlargest(40, "organization_public_repos")

df_public_repos.head()


# In[47]:


df_organizations["organizations_age_in_years"] = df_organizations[
    "organization_created"
].apply(calc_age)


# In[48]:


fig = px.scatter(
    df_organizations.query("organizations_age_in_years<@max_age_in_years"),
    x="organizations_age_in_years",
    y="location_country",
    size="organization_public_repos",
    color="form_of_organization",
    hover_name="organization_website",
    hover_data=["organization_name"],
    size_max=20,
    color_continuous_scale=color_continuous_scale,
)

fig.update_layout(
    coloraxis_colorbar=dict(
        title="DDS",
    ),
    yaxis_title="Rubric",
    xaxis_title="Project Age in Years",
    height=1000,  # Added parameter
    title="Organizations forms within different countries",
    hoverlabel=dict(
    bgcolor="white"
)
)
fig.show()


# ## Not included Projects
# Within the first version of this study we were not able to integrate a GitLab API interfaces. Also other projects on self-hosted repositories and other colloboaritve website could not be included in the study. Another group that was not included in the study are the inactive projects. Here we try to give an insight into these projects. 

# In[49]:


df_raw[(df_raw["platform"] == "gitlab")]


# In[50]:


df_inactive = df_raw[(df_raw["project_active"] == False)].copy()

# Age plots are better in years
df_inactive["project_age_in_years"] = df_inactive["project_age_in_days"].apply(lambda x: x / 365)

fig = px.scatter(
    df_inactive,
    x="project_age_in_years",
    y="rubric",
    size="contributors",
    color="development_distribution_score",
    hover_name="git_url",
    size_max=20,
    color_continuous_scale=color_continuous_scale.reverse(),
)

fig.update_layout(
    coloraxis_colorbar=dict(
        title="DDS",
    ),
    paper_bgcolor="lightgray",
    height=1000,  # Added parameter
    yaxis_title="Rubric",
    xaxis_title="Project Age in years",
    title="Development Distribution Score within inactive Projects",
    hoverlabel=dict(
    bgcolor="white"
)
)

fig.show()

