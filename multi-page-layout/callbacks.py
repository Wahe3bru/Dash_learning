from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
from app import app

###---   Data Wrangling   ---###
follower_count_df = pd.read_csv('data/Follower_count_gsheet.csv')
following_count_df = pd.read_csv('data/Following_count_gsheet.csv')
post_count_df = pd.read_csv('data/Post_count_gsheet.csv')

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

follower_count_df = follower_count_df.set_index('Date')
follower_count_df = follower_count_df.applymap(correct_num_data)

following_count_df = following_count_df.set_index('Date')
following_count_df = following_count_df.applymap(correct_num_data)

post_count_df = post_count_df.set_index('Date')
post_count_df = post_count_df.applymap(correct_num_data)


@app.callback(
    Output('follower_count_graph', 'figure'),
    [Input('tabs-followers', 'value')])
def update_follower_count_graph(selected_data):
    ''' returns plot data based on selection
    '''
    # calc Data based on radio
    if selected_data == 'tab-diff':
        df = follower_count_df.diff()
    elif selected_data == 'tab-perc':
        df = follower_count_df.pct_change()
    else:
        df = follower_count_df

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
            autosize = True,
            height = 400,
            width = 725,
            # title='Follower Count',
            xaxis = dict(
                tickangle=45,
            ),
        )
    }


@app.callback(
    Output('following_count_graph', 'figure'),
    [Input('tabs-following', 'value')])
def update_following_count_graph(selected_data):
    ''' returns plot data based on selection
    '''
    # calc Data based on radio
    if selected_data == 'tab-diff':
        df = following_count_df.diff()
    elif selected_data == 'tab-perc':
        df = following_count_df.pct_change()
    else:
        df = following_count_df

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
            autosize = True,
            height = 400,
            width = 725,
            xaxis = dict(
                tickangle=45,
            ),
        )
    }


@app.callback(
    Output('post_count_graph', 'figure'),
    [Input('tabs-post', 'value')])
def update_post_graph(selected_data):
    ''' returns plot data based on selection
    '''
    # calc Data based on radio
    if selected_data == 'tab-diff':
        df = post_count_df.diff()
    elif selected_data == 'tab-perc':
        df = post_count_df.pct_change()
    else:
        df = post_count_df

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
            autosize = True,
            height = 400,
            width = 725,
            xaxis = dict(
                tickangle=45,
            ),
        )
    }
