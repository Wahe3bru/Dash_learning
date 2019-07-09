# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output # new - needed for Callbacks

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',
                        'https://codepen.io/lindsayrichman/pen/MqYegV.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# reusable dash_core_components
def print_button():
    printButton = html.A(['Print PDF'],
                         className="button no-print print",
                         style={'position': "absolute", 'top': '-40', 'right':'0'})
    return printButton

def get_logo():
    logo = html.Div([

        html.Div([
            html.Img(src='/assets/logo.png',
                     height='100', width='160')
        ], className="ten columns padded"),

        html.Div([
            dcc.Link('Full View   ', href='/full-view')
        ], className="two columns page-view no-print")

    ], className="row gs-header")
    return logo


def get_header():
    header = html.Div([

        html.Div([
             html.H5('Tracking overtime to gain insight')
        ], className="twelve columns padded")

    ], className="row gs-header gs-text-header")
    return header


def get_menu():
    menu = html.Div([

    dcc.Link('overview   ', href='/overview', className="tab first"),
    dcc.Link('followers   ', href='/followers', className="tab"),
    dcc.Link('following   ', href='/following', className="tab"),
    dcc.Link('posts   ', href='/posts', className="tab"),
    dcc.Link('analysis   ', href='/analysis', className="tab"),

    ], className="row")
    return menu

###    ---page layout---   ###
overview = html.Div([

    print_button(),

    html.Div([

        # header
        get_logo(),
        get_header(),
        html.Br([]),
        get_menu(),

        # Row 3
        html.Div([
            html.H4(children='Testing')
        ])
    ])
])

followers = html.Div([])
following = html.Div([])
posts = html.Div([])
analysis = html.Div([])
noPage = html.Div([  # 404

    html.P(["404 Page not found"])

    ], className="no-page")
###   ---App Layout---   ###
app.layout = html.Div([

    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
]) # end of container div


###   ---Callbacks---   ###
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/' or pathname =='/overview':
        return overview
    elif pathname == '/followers':
        return followers
    elif pathname == '/following':
        return following
    elif pathname == '/posts':
        return posts
    elif pathname == '/analysis':
        return analysis
    elif pathname == '/full-view':
        return overview, followers, following, posts, analysis
    else:
        noPage


external_css = ["https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
                "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                "//fonts.googleapis.com/css?family=Raleway:400,300,600",
                "https://codepen.io/lindsayrichman/pen/MqYegV.css",
                 "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"
                ]

for css in external_css:
    app.css.append_css({"external_url": css})

external_js = ["https://code.jquery.com/jquery-3.2.1.min.js",
               "https://codepen.io/bcd/pen/YaXojL.js"]

for js in external_js:
app.scripts.append_script({"external_url": js})


if __name__ == '__main__':
    app.run_server(debug=True)
