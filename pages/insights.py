# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Insights
            
            After Creating Essentially two models there are many things that did not go as I had
            expected. One example would be the fact my app model only lost roughly 3 percent
            validation accuracy compared to the full model. This seems like a rather small drop
            in accuracy rating for the amount of Data that was lost.

            #### The Different Models
            Three models had been tested for both features including a Logistic Regression,
            Random Forest and XGBoost model. The Random Forest Model and the XGBoost model stayed
            relatively close to each other in accuracy. 
            """
        ),
        html.Img(src='assets/ROC.jpg', className='img-fluid'),
        html.Img(src='assets/Accuracy.jpg', className='img-fluid'),
        
        dcc.Markdown(
            """

            Even the ROC score had the models relatively the same. Though the XGBoost model
            always managed to perform slightly better with a .93 ROC score compared to a .92
            validation score the Random Forest model had. Even the validation score for the XGBoost
            model was typically a percent higher than the Random forest model. However after XGBoost
            model was chosen and the app had been created I ran the Random Forest model against
            the test data set. It managed to perform a percent or two higher than the XGBoost model.
        
            """
        ),

    ],
)

layout = dbc.Row([column1])