import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import datetime
import json
import pandas as pd
import plotly.graph_objs as go

#import datasets
df_age_group=pd.read_excel(r'C:\Users\ENVY\PycharmProjects\Pyramid\Data fro census dashboard\Sex_age_group_1.xlsx')
df_age_group_urban=pd.read_excel(r'C:\Users\ENVY\PycharmProjects\Pyramid\Data fro census dashboard\Sex_age_group_urban.xlsx')
df_age_group_rural=pd.read_excel(r'C:\Users\ENVY\PycharmProjects\Pyramid\Data fro census dashboard\Sex_age_group_rural.xlsx')

#instantiate an app
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
                    html.H2('Population Pyramid')

                ,width=4)
            ]
        ),

        dbc.Row(
            [
                dbc.Col(
                    [
                       dcc.Dropdown(id='pyram',
                                    value='Rwanda',
                                    options=['Rwanda','Rural','Urban']),
                        dcc.Graph(id='graph-pyr',figure={})
                    ]
                )
            ]
        )
    ]
)

@app.callback(
        Output('graph-pyr','figure'),
        Input('pyram','value'))
def pop_pyramid(slct_input):
    if slct_input=="Rwanda":
        y_age = df_age_group['age_cat']
        x_Male = df_age_group['Male']
        x_Female = df_age_group['Female'] * -1

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
            title='Rwanda Census Population Pyramid',
            title_font_size=24,
            barmode='relative',
            bargap=0.0,
            bargroupgap=0,
            plot_bgcolor='white',
            xaxis=dict(
                tickvals=[-800000, -600000, -400000, -200000, 0, 200000, 400000, 600000, 800000],
                ticktext=['800k', '600k', '400k', '200k', 0, '200k', '400k', '600k', '800k'],
                title='Population in Thousands'
            )
        )
        return fig

    elif slct_input=="Urban":
        y_age = df_age_group_urban['age_cat']
        x_Male = df_age_group_urban['Male']
        x_Female = df_age_group_urban['Female'] * -1

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
            title='Urban Census Population Pyramid',
            title_font_size=24,
            barmode='relative',
            bargap=0.0,
            bargroupgap=0,
            plot_bgcolor='white',
            xaxis=dict(
                tickvals=[-200000, -100000, 0, 100000, 200000],
                ticktext=['200k', '100k', 0, '100k', '200k'],
                title='Population in Thousands'
            )
        )

        return fig

    elif slct_input=="Rural":
        y_age = df_age_group_rural['age_cat']
        x_Male = df_age_group_rural['Male']
        x_Female = df_age_group_rural['Female'] * -1

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
            title='Rural Census Population Pyramid',
            title_font_size=24,
            barmode='relative',
            bargap=0.0,
            bargroupgap=0,
            plot_bgcolor='white',
            xaxis=dict(
                tickvals=[-600000, -400000, -200000, 0, 200000, 400000, 600000],
                ticktext=['600k', '400k', '200k', 0, '200k', '400k', '600k'],
                title='Population in Thousands'
            )
        )
        return fig





server=app.server
app.run_server(debug=True,port=3200)
