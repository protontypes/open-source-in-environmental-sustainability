import plotly.io as pio
import plotly.graph_objects as go
import plotly.express as px
from PIL import Image
logo_img = Image.open('logo.png') # image path
# default plotting options
# Palette https://coolors.co/palette/0e7c7b-17bebb-ffc857-e9724c-c5283d
color_continuous_scale = px.colors.sequential.Aggrnyl[::-1]
marker_color = "#0E7C7B"
color_discrete_sequence = ["#3e59fb","#007dff","#0097ff","#00acff","#00bef9","#00cdde","#00dac1","#26e5a9"]
color_single_hue_scale = ["#159485","#3ca394","#58b1a3","#70c0b3","#87cfc3","#9edfd3","#b5eee3"]
color_divergent_scale = ["#3e59fb","#9089f9","#c5bcf6","#f1f1f1","#bfeed8","#86eac1","#26e5a9"]

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
