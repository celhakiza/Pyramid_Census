import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import datetime
import json
import pandas as pd
import plotly.graph_objs as go
import mysql.connector
df_pyramid=pd.read_excel(r'C:\Users\ENVY\Desktop\Data science\pop2.xlsx',skiprows=4)


app=dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP],
              meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )
server=app.server
app.layout=dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.H2('Population Pyramid Projection')

                ,width=4)
            ]
        ),

        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H6('Slide from left to right to get the population projection for each year'),
                       dcc.Slider(min=2013,max=2032,step=1,
                                  value=2013,
                                  id='pyram',
                                  marks=None,
                                  tooltip={"placement": "bottom", "always_visible": True}
                                  ),
                        dcc.Graph(id='graph-pyr',figure={})
                    ]
                )
            ]
        )
    ]
)
@app.callback(
    Output('graph-pyr','figure'),
    Input('pyram','value')
)

def pyramid(slctd_year):
    df_pyramid_1=df_pyramid[df_pyramid['year']==slctd_year]
    y_age = df_pyramid_1['age_group']
    x_Male = df_pyramid_1['Male']
    x_Female = df_pyramid_1['Female'] * -1

    # instantiate figure
    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=y_age,
        x=x_Male,
        name='Male',
        orientation='h'
    ))
    fig.add_trace(go.Bar(
        y=y_age,
        x=x_Female,
        name='Female',
        orientation='h'
    ))

    fig.update_layout(
        template='plotly_white',
        title='Rwanda Census Population Pyramid Projection in {}'.format(slctd_year),
        title_font_size=24,
        barmode='relative',
        bargap=0.0,
        bargroupgap=0,
        plot_bgcolor='white',
        xaxis=dict(
            tickvals=[-1000000,-800000, -600000, -400000, -200000, 0, 200000, 400000, 600000, 800000,1000000],
            ticktext=['1M','800k', '600k', '400k', '200k', 0, '200k', '400k', '600k', '800k','1M'],
            title='Population in Thousands'
        )
    )

    return fig








server=app.server
app.run_server(debug=True,port=3300)




# df_pyramid_1=df_pyramid[df_pyramid['year']==2019]
# print(df_pyramid_1)