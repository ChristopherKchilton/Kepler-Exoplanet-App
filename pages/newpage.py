from joblib import load
pipeline = load('assets/model_xgbapp.joblib')
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
import pandas as pd

# @app.callback(
#     Output('prediction-content', 'children'),
#     [Input('Planetar_Radius', 'value'), 
#     Input('Insoluation_Flux', 'value'),
#     Input('Transit_Signal', 'value'),
#     Input('Transit_Duration', 'value'),
#     Input('Keplar_Band', 'value'),
#     Input('Orbital_Period_Days', 'value'),
#     Input('Stellar_Effective_Temperature', 'value'),
#     ],
# )
# def predict(Planetar_Radius,Insoluation_Flux,
# Transit_Signal,Transit_Duration,Keplar_Band,
# Orbital_Period_Days,Stellar_Effective_Temperature):
#     df = pd.DataFrame(
#         columns=['Planetar_Radius',
#         'Insoluation_Flux',
#         'Transit_Signal',
#         'Transit_Duration',
#         'Keplar_Band',
#         'Orbital_Period_Days',
#         'Stellar_Effective_Temperature'], 
#         data=[[Planetar_Radius, Insoluation_Flux,
#         Transit_Signal,Transit_Duration,Keplar_Band,
#         Orbital_Period_Days,Stellar_Effective_Temperature]]
#     )
#     y_pred = pipeline.predict(df)[0]
#     return f'{y_pred}'

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## PAGE NAME


            """
        ),
        html.H2('Exoplanet Prediction Type', className='mb-5'),
        html.Div(id='prediction-content', className='lead')
    ],
    md=4,
)

column2 = dbc.Col(
    [
        dcc.Markdown('## Predictions', className='mb-5'), 
        dcc.Markdown('#### Planetary Radius'), 
        dcc.Slider(
            id='Planetar_Radius', 
            min=1, 
            max=21, 
            step=2, 
            value=800, 
            marks={n: str(n) for n in range(1,22,2)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Insolation Flux'), 
        dcc.Slider(
            id='Insoluation_Flux', 
            min=20, 
            max=200, 
            step=20, 
            value=100, 
            marks={n: str(n) for n in range(20,201,20)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Transit Signal'), 
        dcc.Slider(
            id='Transit_Signal', 
            min=1, 
            max=101, 
            step=10, 
            value=10, 
            marks={n: str(n) for n in range(1,102,10)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Transit Duration'), 
        dcc.Slider(
            id='Transit_Duration', 
            min=1, 
            max=20, 
            step=2, 
            value=10, 
            marks={n: str(n) for n in range(1,22,2)}, 
            className='mb-5', 
        ),
        dcc.Markdown('#### Keplar Band'), 
        dcc.Slider(
            id='Keplar_Band', 
            min=1, 
            max=20, 
            step=2, 
            value=14, 
            marks={n: str(n) for n in range(1,20,2)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Orbital Period (Days)'), 
        dcc.Slider(
            id='Orbital_Period_Days', 
            min=1, 
            max=101, 
            step=10, 
            value=50, 
            marks={n: str(n) for n in range(1,102,10)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Stellar Effective Temperature'), 
        dcc.Slider(
            id='Stellar_Effective_Temperature', 
            min=2500, 
            max=10000, 
            step=1000, 
            value=5000, 
            marks={n: str(n) for n in range(2500,10000,1000)}, 
            className='mb-5', 
        ), 
    ],
    md=4,
)

layout = dbc.Row([column1, column2])
