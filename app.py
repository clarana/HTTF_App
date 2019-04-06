
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
                'textAlign': 'center',
                'color': colors['text']
        }),

        html.Div(
            children='''Answer questions and get feedback about your daily habits!''',
            style={
                'textAlign': 'center',
                'color': colors['text']
        }),

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
                        children='asdfasdfasdf', # will hold variable now
                        style={
                            'margin': '10pt',
                            'width': '40%',
                            'display': 'inline-block'
                        }
                    )
                ],
                style={
                    # 'display': 'inline-block'
                    'width': '90%'
                }
            ),

            # 'Coffee',
            # dcc.Slider(
            #     id='Q2',
            #     min=0,
            #     max=20,
            #     value=0,
            #     marks={str(year): str(year) for year in range(0, 21, 5)},
            # ),
            # 'Tea',
            # dcc.Slider(
            #     id='Q3',
            #     min=0,
            #     max=20,
            #     value=0,
            #     marks={str(year): str(year) for year in range(0, 21, 5)},
            # ),
            # 'Soft drinks',
            # dcc.Slider(
            #     id='Q4',
            #     min=0,
            #     max=20,
            #     value=0,
            #     marks={str(year): str(year) for year in range(0, 21, 5)},
            # ),
            # 'Alcohol (per week)',
            # dcc.Slider(
            #     id='Q5',
            #     min=0,
            #     max=20,
            #     value=0,
            #     marks={str(year): str(year) for year in range(0, 21, 5)},
            # ),
        ],
        style={'width': '90%'}),
    ])


])

# @app.callback(
#     Output('indicator-graphic', 'figure'),
#     [Input('Q1')
#      ])
# def update_graph(xaxis_column_name, yaxis_column_name,
#                  xaxis_type, yaxis_type,
#                  year_value):
#
#
#     return {
#         # 'data': [go.Scatter(
#         #     x=dff[dff['Indicator Name'] == xaxis_column_name]['Value'],
#         #     y=dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
#         #     text=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'],
#         #     mode='markers',
#         #     marker={
#         #         'size': 15,
#         #         'opacity': 0.5,
#         #         'line': {'width': 0.5, 'color': 'white'}
#         #     }
#         # )],
#         # 'layout': go.Layout(
#         #     xaxis={
#         #         'title': xaxis_column_name,
#         #         'type': 'linear' if xaxis_type == 'Linear' else 'log'
#         #     },
#         #     yaxis={
#         #         'title': yaxis_column_name,
#         #         'type': 'linear' if yaxis_type == 'Linear' else 'log'
#         #     },
#         #     margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
#         #     hovermode='closest'
#         # )
#     }


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
