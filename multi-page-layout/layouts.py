import dash_core_components as dcc
import dash_html_components as html

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
# Page1
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
            html.H6(children='Introduction', className="gs-header gs-text-header padded"),
            html.P(children='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
        ], className="row ten columns"),

        # Row 4
        html.Div([
            html.Div([
                html.H6(children='How to use this report', className="gs-header gs-text-header padded"),
                html.P(children='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
            ], className="six columns"),
            html.Div([
                html.H6(children='Another section here', className="gs-header gs-text-header padded"),
                html.P(children='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
            ], className="six columns"),
        ], className="row twelve columns"),

    ], className="subpage")
], className="page")

# page2
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
            html.H6(children='Summary', className="gs-header gs-text-header padded"),
            html.P(children= "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quam sint aliquid dignissimos placeat iste vero atque iusto iure nulla dolore. Odio libero doloremque repellat neque quibusdam deserunt aut necessitatibus culpa."),
            html.P(children= "Consectetur adipisicing elit. Quam sint aliquid dignissimos placeat iste vero atque iusto iure nulla dolore. Odio libero doloremque repellat neque quibusdam deserunt aut necessitatibus culpa."),
        ], className="row ten columns"),

        # Row 4
        html.Div([
            html.H6(children='Follower Counts', className="gs-header gs-text-header padded"),
            dcc.Tabs(id='tabs-followers' ,value='tab-perc', children=[
                dcc.Tab(label='Raw Numbers', value='tab-raw'),
                dcc.Tab(label='Difference', value='tab-diff'),
                dcc.Tab(label='Percentage Change', value='tab-perc'),
            ], className="custom-tabs-container custom-tab custom-tabs custom-tab--selected "),
            html.Div([
                dcc.Graph(
                    id='follower_count_graph',
                    style={'height':'450', 'width':'720'},
                    config={
                        'displayModeBar': False,
                        'displaylogo': False
                    }
                )
            ], className="twelve columns"),


        ], className="row twelve columns"),

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
            html.H6(children='Summary', className="gs-header gs-text-header padded"),
            html.P(children= "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quam sint aliquid dignissimos placeat iste vero atque iusto iure nulla dolore. Odio libero doloremque repellat neque quibusdam deserunt aut necessitatibus culpa."),
            html.P(children= "Consectetur adipisicing elit. Quam sint aliquid dignissimos placeat iste vero atque iusto iure nulla dolore. Odio libero doloremque repellat neque quibusdam deserunt aut necessitatibus culpa."),
        ], className="row ten columns"),

        # Row 4
        html.Div([
            html.H6(children='Folowing Counts', className="gs-header gs-text-header padded"),
            dcc.Tabs(id='tabs-following', value='tab-diff', children=[
                dcc.Tab(label='Raw Numbers', value='tab-raw'),
                dcc.Tab(label='Difference', value='tab-diff'),
                dcc.Tab(label='Percentage Change', value='tab-perc'),
            ], className="custom-tabs-container custom-tab custom-tabs custom-tab--selected "),
            html.Div([
                dcc.Graph(
                    id='following_count_graph',
                    style={'height':'450', 'width':'720'},
                    config={
                        'displayModeBar': False,
                        'displaylogo': False
                    }
                )
            ], className="twelve columns"),
        ], className="row twelve columns")

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
            html.H6(children='Summary', className="gs-header gs-text-header padded"),
            html.P(children= "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quam sint aliquid dignissimos placeat iste vero atque iusto iure nulla dolore. Odio libero doloremque repellat neque quibusdam deserunt aut necessitatibus culpa."),
            html.P(children= "Consectetur adipisicing elit. Quam sint aliquid dignissimos placeat iste vero atque iusto iure nulla dolore. Odio libero doloremque repellat neque quibusdam deserunt aut necessitatibus culpa."),
        ], className="row ten columns"),

        # Row 4
        html.Div([
            html.H6(children="Post Count", className="gs-header gs-text-header padded"),
            dcc.Tabs(id='tabs-post', value='tab-raw', children=[
                dcc.Tab(label='Raw Numbers', value='tab-raw'),
                dcc.Tab(label='Difference', value='tab-diff'),
                dcc.Tab(label='Percentage Change', value='tab-perc'),
            ], className="custom-tabs-container custom-tab custom-tabs custom-tab--selected "),
            html.Div([
                dcc.Graph(
                id='post_count_graph',
                style={'height':'450', 'width':'720'},
                config={
                    'displayModeBar': False,
                    'displaylogo': False
                }
            )
            ], className="twelve columns"),
        ], className="row twelve columns")

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
    html.Div([
        get_logo(),
        get_header(),
        html.Br([]),
        get_menu(),
        html.H1(["404 Page not found"]),
    ], className="subpage")
], className="page")
