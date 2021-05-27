# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Space Exploration

            Ever since the first space missions, humans have dreamed of building 
            space ships and exploring the Universe. However, propulsion technology 
            has not improved much since in the past century. With how vast space is, 
            other methods were created to "explore" space. One such method is the use 
            of telescopes and satalites to find distant planets.

            The Kepler Space Telescope just finished its mission in 2018 and the Data is collected
            is stored in a NASA database. With the help of machine learning we are able to predict
            whether the data observed from the chaning sun light are possible distant exoplanets
            or comsic noise. So join us as we explore the Universe!

            """
        ),
        dcc.Link(dbc.Button('Find Exoplanets', color='primary'), href='/predictions')
    ],
    md=4,
)

# gapminder = px.data.gapminder()
# fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
#            hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        html.Img(src='assets/pexels-philippe-donn-1169754.jpg', className='img-fluid')
        # dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])