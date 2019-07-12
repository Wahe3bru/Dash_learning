import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from layouts import overview, followers, following, posts, analysis, noPage
import callbacks

app.layout = html.Div([

    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

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
        return noPage


external_js = ["https://code.jquery.com/jquery-3.2.1.min.js",
               "https://codepen.io/bcd/pen/YaXojL.js"]

for js in external_js:
    app.scripts.append_script({"external_url": js})


if __name__ == '__main__':
    app.run_server(debug=True)
