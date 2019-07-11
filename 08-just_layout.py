# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output # new - needed for Callbacks

external_css = ["https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
                "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                "//fonts.googleapis.com/css?family=Raleway:400,300,600",
                #"https://codepen.io/lindsayrichman/pen/MqYegV.css",
                 "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"
                ]
app = dash.Dash(__name__, external_stylesheets=external_css)

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
    menu = html.Div([    # Enclosed div to center menu
        html.Div([       # style "display" to center entire menu
            dcc.Link('overview   ', href='/overview', className="tab first"),
            dcc.Link('followers   ', href='/followers', className="tab"),
            dcc.Link('following   ', href='/following', className="tab"),
            dcc.Link('posts   ', href='/posts', className="tab"),
            dcc.Link('analysis   ', href='/analysis', className="tab"),
        ], style={"display":"inline-block"}),
    ], className="row", style={'text-align': 'center'})
    return menu

###    ---page layout---   ###
# page1
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
            html.H4(children='Introduction', className="gs-header gs-text-header padded"),
            html.P(children= "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quam sint aliquid dignissimos placeat iste vero atque iusto iure nulla dolore. Odio libero doloremque repellat neque quibusdam deserunt aut necessitatibus culpa."),
            html.P(children= "Consectetur adipisicing elit. Quam sint aliquid dignissimos placeat iste vero atque iusto iure nulla dolore. Odio libero doloremque repellat neque quibusdam deserunt aut necessitatibus culpa."),
        ], className="ten columns")

    ], className="subpage")
], className="page")

# Page2
followers = html.Div([

    print_button(),

    html.Div([

        # header
        get_logo(),
        get_header(),
        html.Br([]),
        get_menu(),

        # Row 3
        html.Div([
            html.H4(children='Followers')
        ])
    ], className="subpage")
], className="page")

#Page3
following = html.Div([

    print_button(),

    html.Div([

        # header
        get_logo(),
        get_header(),
        html.Br([]),
        get_menu(),

        # Row 3
        html.Div([
            html.H4(children='Following')
        ])
    ], className="subpage")
], className="page")

# Page4
posts = html.Div([

    print_button(),

    html.Div([

        # header
        get_logo(),
        get_header(),
        html.Br([]),
        get_menu(),

        # Row 3
        html.Div([
            html.H4(children='Post')
        ])
    ], className="subpage")
], className="page")

# Page5
analysis = html.Div([

    print_button(),

    html.Div([

        # header
        get_logo(),
        get_header(),
        html.Br([]),
        get_menu(),

        # Row 3
        html.Div([
            html.H4(children='analysis')
        ])
    ], className="subpage")
], className="page")


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


external_js = ["https://code.jquery.com/jquery-3.2.1.min.js",
               "https://codepen.io/bcd/pen/YaXojL.js"]

for js in external_js:
    app.scripts.append_script({"external_url": js})


if __name__ == '__main__':
    app.run_server(debug=True)
