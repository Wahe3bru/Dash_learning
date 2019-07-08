# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output # new - needed for Callbacks

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


###---   Data Wrangling   ---###
Follower_count_df = pd.read_csv('data\Follower_count_gsheet.csv')

def correct_num_data(x):
    """turn (1,234 and 11.7K) strings into integer values
    eg 1,234 -> 1234 and 11.7K -> 11700
    """
    y = str(x)
    if '.' in y:
        x_split = y.split('.')
        x_split[0] = int(x_split[0])*1000
        x_split[1] = x_split[1].replace('k', '00')
        y = x_split[0] + int(x_split[1])
    else:
        y = y.replace(',', '').replace('k', '000')
    return int(y)

Follower_count_df = Follower_count_df.set_index('Date')
Follower_count_df = Follower_count_df.applymap(correct_num_data)

###---   Pre Layout things    ---###
# color pallette coloors.co
colors = {
    'dim_gray': '#706C61',
    'lightr_blue': '#99C5B5',
    'light_blue': '#5AB1BB',
    'pistachio': '#A5C882',
    'mel_yellow': '#F7DD72'
}

# possibly programatically change text
intro_text = '''
#### Intro text
So I will be going way over the top with customizing nearly everything that i
can or think i will need to in terms of styling.
'''

####---   Layout   ---###
app.layout = html.Div(children=[
    html.Div(style={'width':'100%', 'align':'center'}, children=[
        html.Img(src='/assets/Instatrakkr.png')                      # add image
    ]),

        html.Div(children=[
            html.H1(children='InstaTrakr'),
            html.P(children='A Work in progress...')
        ], className='row'),

        html.Div(children=[
        dcc.Markdown(children=intro_text)
        ]),

        html.Div(children=[
            html.Div(children=[
                html.H5(children='Follower Count',
                     style={'backgroundColor': colors['dim_gray'], 'color':colors['light_blue']}),
                dcc.RadioItems(
                    id='follower_count_graph_data',
                    options=[
                        {'label': 'Raw Numbers', 'value': 'raw'},
                        {'label': 'Difference', 'value': 'diff'},
                        {'label': 'Percentage change', 'value': 'pcnt'}
                    ],
                    value='raw',
                    labelStyle={'display': 'inline-block'}
                )
            ], className='row', style={'text-align': 'center'}),


            dcc.Graph(
                id='follower_count_graph',
                config={
        	      'modeBarButtonsToRemove': [
                	'sendDataToCloud',
        	        'pan2d',
                	'zoomIn2d',
        	        'zoomOut2d',
        	        'autoScale2d',
        	        'resetScale2d',
        	        'hoverCompareCartesian',
        	        'hoverClosestCartesian',
        	        'toggleSpikelines'
                      ],
                	'displayModeBar': True,
                	'displaylogo': False
                }
            )
        ], className='ten columns', style={'margin-bottom':'10'})
    ], className='container')

###---   Callbacks   ---###
@app.callback(
    Output('follower_count_graph', 'figure'),
    [Input('follower_count_graph_data', 'value')])
def update_follower_count_graph(selected_data):
    ''' returns plot data based on selection
    '''
    # calc Data based on radio
    if selected_data == 'diff':
        df = Follower_count_df.diff()
    elif selected_data == 'pcnt':
        df = Follower_count_df.pct_change()
    else:
        df = Follower_count_df

    # prep data for return
    traces = []
    for i in df.columns:
        traces.append(
            go.Scatter(
                x=df.index,
                y=df[i],
                mode='markers+lines',
                name=i,
            )
        )
    return {
        'data': traces,
        'layout': go.Layout(
            title='Follower Count',
            xaxis = dict(
                title='Date',
                titlefont=dict(
                    family='Helvetica, monospace',
                    size=20,
                    color=colors['light_blue']
                ),
                tickangle=45,
            )
        )
    }

if __name__ == '__main__':
    app.run_server(debug=True)
