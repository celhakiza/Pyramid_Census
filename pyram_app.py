import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import datetime
import json
import pandas as pd
import plotly.graph_objs as go

df_pyramid=pd.read_excel(r'C:\Users\ENVY\Desktop\Data science\pop2.xlsx',skiprows=4)
df_tot_population=pd.read_excel(r'C:\Users\ENVY\PycharmProjects\Pyramid\Pyramid_Census\Total population.xlsx')


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

                ,className="text-center text-primary mb-4 font-weight-bold",width=12),
                dcc.Markdown('![Image](https://pbs.twimg.com/profile_images/1115228529812287489/5ciAZeIe_200x200.png)') #add image of NISR
            ]
        ),

        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Slider(id='line-input'),
                        dcc.Graph(id='line-trend',figure={}),
                        dcc.Markdown('*N.B: Hover on line chart to generate corresponding pyramid*'), #to format in italic
                        dcc.Markdown(' *for more info click on link to get NISR website: [Link] (https://www.statistics.gov.rw)*') #to get link
                    ]
                ,width=5),
                dbc.Col(
                    [
                        dcc.Graph(id='graph-pyr',figure={}),
                        dcc.Markdown('*This is population pyramid projection from Rwanda '
                                     'Population and Housing Census 2012*')
                    ]
                ,width=7)
            ]
        )
    ]
)
@app.callback(
    Output('line-trend','figure'),
    Input('line-input','value')

)
def line(line_input):
    fig=px.line(data_frame=df_tot_population,
                x='Year',
                y='Population Projection ',
                markers=True)
    fig.update_layout(xaxis_title='Year',
                      yaxis_title='Total Population',
                      title='Population across year',
                      title_font_size=24,
                      title_font_color='blue',
                      plot_bgcolor='cornsilk')
    return fig
@app.callback(
    Output('graph-pyr','figure'),
    Input('line-trend',component_property='hoverData')
)
def pyramid(slctd_year):
    if slctd_year is None:
        df_pyramid_1=df_pyramid[df_pyramid['year']==2013]
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
            title='Rwanda Population Pyramid in {}'.format(2013),
            title_font_size=24,
            barmode='relative',
            bargap=0.0,
            bargroupgap=0,
            plot_bgcolor='white',
            title_font_color='blue',
            xaxis=dict(
                tickvals=[-1000000,-800000, -600000, -400000,-200000,-100000, 0,100000,200000, 400000, 600000, 800000,1000000],
                ticktext=['1M','800k', '600k', '400k', '200k','100k', 0,'100k', '200k', '400k', '600k', '800k','1M'],
                title='Population in Thousands'
            )
        )

        return fig

    else:
        hover_year=slctd_year['points'][0]['x']
        df_pyramid_1 = df_pyramid[df_pyramid['year'] == hover_year]
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
            title='Rwanda Population Pyramid in {}'.format(hover_year),
            title_font_size=24,
            barmode='relative',
            bargap=0.0,
            bargroupgap=0,
            plot_bgcolor='white',
            title_font_color='blue',
            xaxis=dict(
                tickvals=[-1000000, -800000, -600000, -400000, -200000, -100000, 0, 100000, 200000, 400000, 600000,
                          800000, 1000000],
                ticktext=['1M', '800k', '600k', '400k', '200k', '100k', 0, '100k', '200k', '400k', '600k', '800k',
                          '1M'],
                title='Population in Thousands'
            )
        )

        return fig


server=app.server
app.run_server(debug=True,port=3300)

#print(df_tot_population.head())


