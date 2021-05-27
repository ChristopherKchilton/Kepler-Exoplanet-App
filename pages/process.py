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
        
            ## The Process

            After exploring the Data through the use of a profile report and a few other key 
            features we were able to determine that the Equilibrium Error columns had to be 
            dropped due to missing data.

            Now that we cleaned up the Data some we would have to decide what we would like to 
            predict. Well of course the most interesting would be to make a machine learning 
            model for its intended purpose. That is to say, predict on whether or not the object 
            is a candidate for being an Exoplanet. There were a couple other options we could 
            have chosen including the Disposition score which is how likely the object would be 
            a candidate however that does not seem as impressive. In this case we chose the more 
            clear cut Disposition on whether it was a Candidate for being a exoplanet or if it was 
            a False positive.

            #### Leakage
            Now that we have chosen what we want to predict we need to explore the Data further 
            to make sure there is no leakage. In other words, does any of this Data hold 
            information that directly relates to the Disposition of the planet. Exoplanet 
            Archive Disposition and Disposition Score are obvious leakage as they both have 
            information regarding the Disposition of the object so they are dropped. This was 
            also verified by checking their gini score in a base model. After dropping those 
            features we looked further into the data and there were 4 other columns that were 
            questionable.

            While there is documentation for the Data, it is not always easy to determine what 
            the Data actually represents. After reading the documentation closely, it appears 
            these Flag columns are a binary classification representing the Data is flagged for 
            some type of error. I looked into the Data even further and the Flag columns provided 
            a feature score substantially higher than the other features. I tried researching 
            more about these columns but was unable to determine if this flagging was done 
            automatically and what data was used to flag the  Kepler Data, so I removed it to 
            make sure all forms of leakage

            #### The Model

            The original model kept the majority of the features and even combined the Upper
            and Lower uncertainty into an Error column for each data type. However to help
            reduce the number of features for the App we dropped the majority of the features
            and took the 7 most important features by looking at the gini importance / feature
            importance and permutation importance from the top performing models. 


            """
        ),
        html.Img(src='assets/Random-Feature-Importance.jpg', className='img-fluid'),
        html.Img(src='assets/XGBFeature-Importance.jpg', className='img-fluid'),
        html.Img(src='assets/Permutation-Importance.jpg', className='img-fluid'),

        dcc.Markdown(""" As you can see the most of the data came from the same main features
        and their Error counter parts. After reducing the features the Logistic Regression,
        Random Forest and XGBoost model were tested again. Surprisingly the validation accuracy
        only dropped around 4 percent for the Random Forest model and the XGBoost model. The
        Random Forest model and the XGboost model were still significantly better than the
        Logistic Regression model so we tuned the parameter on both models and the XGBoost
        model performed slightly better so it was chosen as the model for this application.
        

        
        """
        ),



    ],
)

layout = dbc.Row([column1])