import plotly.io as pio
import plotly.graph_objects as go
import plotly.express as px
# default plotting options
# Palette https://coolors.co/palette/0e7c7b-17bebb-ffc857-e9724c-c5283d
color_continuous_scale = px.colors.sequential.Aggrnyl[::-1]
marker_color = "#0E7C7B"
color_discrete_sequence = ["#0E7C7B", "#17BEBB", "#FFC857", "#E9724C", "#C5283D"]

# Register your theme as a named template
pio.templates["OpenSustain"] = go.layout.Template(
    layout=dict(
        margin=dict(
        b=0 #bottom margin
    ),
        font=dict(
            family="Open Sans",
            color="#040404",
            size=15,
        ),
        title_font_family="Open Sans",
        title_font_color="#040404",
    ),
)

# Combine your theme with plotly's default
pio.templates.default = "plotly+OpenSustain"
