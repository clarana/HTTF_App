
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/'
    'cb5392c35661370d95f300086accea51/raw/'
    '8e0768211f6b747c0db42a9ce9a0937dafcbd8b2/'
    'indicators.csv')

colors = {
    'background': '#DDDDDF',
    'text': '#333333'
}



available_indicators = df['Indicator Name'].unique()

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.Div([
        html.H1(
            children='Calculate your UVA Green Score',
            style={
                'padding': '20pt',
                'textAlign': 'center',
                'color': colors['text']
        }),

        # Drinks
        html.Div([
            html.H2(
                children='Drinks'
            ),
            html.H3(
                children='How many servings of each beverage do you drink per day?',
                style={
                    'font-weight': 'normal'
                }
            ),
            html.Div(
                children=[
                    html.Div(
                        children=[
                            'Water',
                            dcc.Slider(
                                id='Q1',
                                min=0,
                                max=20,
                                value=0,
                                marks={str(year): str(year) for year in range(0, 21, 5)},
                            )],
                        style={
                            'margin': '10pt',
                            'width': '40%',
                            'display': 'inline-block'
                        }
                    ),
                    html.Div(
                        id='F1',
                        style={
                            'margin': '10pt',
                            'width': '50%',
                            'display': 'inline-block',
                        }
                    )
                ],
                style={
                    # 'display': 'inline-block'
                    'width': '90%'
                }
            ),
            # Coffee: Q2, F2
            html.Div(
                children=[
                    html.Div(
                        children=[
                            'Coffee',
                            dcc.Slider(
                                id='Q2',
                                min=0,
                                max=20,
                                value=0,
                                marks={str(year): str(year) for year in range(0, 21, 5)},
                            )],
                        style={
                            'margin': '10pt',
                            'width': '40%',
                            'display': 'inline-block'
                        }
                    ),
                    html.Div(
                        id='F2',
                        style={
                            'margin': '10pt',
                            'width': '50%',
                            'display': 'inline-block',
                        }
                    )
                ],
                style={
                    # 'display': 'inline-block'
                    'width': '90%'
                }
            ),
            # Soft Drinks: Q3, F3
            html.Div(
                children=[
                    html.Div(
                        children=[
                            'Soft Drinks',
                            dcc.Slider(
                                id='Q3',
                                min=0,
                                max=20,
                                value=0,
                                marks={str(year): str(year) for year in range(0, 21, 5)},
                            )],
                        style={
                            'margin': '10pt',
                            'width': '40%',
                            'display': 'inline-block'
                        }
                    ),
                    html.Div(
                        id='F3',
                        style={
                            'margin': '10pt',
                            'width': '50%',
                            'display': 'inline-block'
                        }
                    )
                ],
                style={
                    # 'display': 'inline-block'
                    'width': '90%'
                }
            ),
            # Alcohol: Q4, F4
            html.Div(
                children=[
                    html.Div(
                        children=[
                            'Alcohol',
                            dcc.Slider(
                                id='Q4',
                                min=0,
                                max=20,
                                value=0,
                                marks={str(year): str(year) for year in range(0, 21, 5)},
                            )],
                        style={
                            'margin': '10pt',
                            'width': '40%',
                            'display': 'inline-block'
                        }
                    ),
                    html.Div(
                        id='F4',
                        style={
                            'margin': '10pt',
                            'width': '50%',
                            'display': 'inline-block'
                        }
                    )
                ],
                style={
                    # 'display': 'inline-block'
                    'width': '90%'
                }
            ), 
        ],
        style={
            'width': '90%',
            'padding': '10pt'
        }),

        # Transport
        html.Div(
            [
                html.H2(
                    children='Transportation'
                ),
                html.Div(
                [
                    html.H3(
                        children='How many miles do you drive in your car per week?',
                        style={
                            'font-weight': 'normal'
                        }
                    ),
                    dcc.Slider(
                        id='Q5',
                        min=0,
                        max=20,
                        value=0,
                        marks={str(i): str(i) for i in range(0, 201, 50)},
                    ),
                ],
                style={
                    'margin': '10pt',
                    'width': '40%',
                    'display': 'inline-block'
                })
            ],
            style={
                'width': '90%',
                'padding': '10pt'
            }
        ),

        # Figure
        html.Div(
            dcc.Graph(id='Pie')
        )
    ]),


])

@app.callback(
    [Output('F1', component_property='children'),
     Output('F2', component_property='children'),
     Output('F3', component_property='children'),
     Output('F4', component_property='children'),
     Output('Pie', 'figure')
     ],
    [Input('Q1', 'value'),
     Input('Q2', 'value'),
     Input('Q3', 'value'),
     Input('Q4', 'value')
     ])
def update(q1, q2, q3, q4):
    red = int(q2) + int(q3) + int(q4) - int(q1)
    green = 100-red

    out1 = ''
    out2 = ''
    out3 = ''
    out4 = ''

    if int(q1) > 0:
        out1 = 'Water is the “greenest” drink! Producing one liter of bottled water requires only one liter of water (plus transportation and distribution)'
    if int(q2) > 0:
        out2 = 'It takes 140 liters of water to produce one cup of coffee, and 50 cups of water to grow every teaspoon of sugar'
    if int(q3) > 0:
        out3 = 'It takes much more water than this to produce [this amount] of your drink of choice! What’s more, it takes 50 cups of water to grow every teaspoon of sugar, and the energy costs of transporting it are also high. One glass of fruit juice or milk requires 170 to 200 liters of water to produce.'
    if int(q4) > 0:
        out4 = 'A glass of beer takes 75 liters of water to produce, and a glass of wine takes 120 liters of water to produce'
    return out1, out2, out3, out4, { 'data': 
        [go.Pie(values=[red, green], 
                labels=['Red points', 'Green points'],
                marker=dict(colors=['#FF0000', '#00FF00'])
        )]
    }


if __name__ == '__main__':
    app.run_server(debug=True)


#
# # -*- coding: utf-8 -*-
# import dash
# import dash_core_components as dcc
# import dash_html_components as html
#
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#
# colors = {
#     'background': '#CCCCCF',
#     'text': '#1111FF'
# }
#
# app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
#     html.H1(children='Calculate your UVA Green Score',
#             style={
#                 'textAlign': 'center',
#                 'color': colors['text']
#             }),
#
#     html.Div(children='''
#         Answer questions and get feedback about your daily habits!
#     ''',
#              style={
#                  'textAlign': 'center',
#                  'color': colors['text']
#              }),
#
#
#
#
#     # dcc.Graph(
#     #     id='example-graph',
#     #     figure={
#     #         'data': [
#     #             {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
#     #             {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
#     #         ],
#     #         'layout': {
#     #             'plot_bgcolor': colors['background'],
#     #             'paper_bgcolor': colors['background'],
#     #             'font': {
#     #                 'color': colors['text']
#     #             }
#     #         }
#     #     }
#     # )
# ])
#
# if __name__ == '__main__':
#     app.run_server(debug=True)
