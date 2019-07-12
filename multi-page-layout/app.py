import dash

external_css = ["https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
                "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                "//fonts.googleapis.com/css?family=Raleway:400,300,600",
                #"https://codepen.io/lindsayrichman/pen/MqYegV.css",
                 "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css",
                ]
app = dash.Dash(__name__, external_stylesheets=external_css)
# allows for callbacks that are not used immediately (ie on page load)
app.config['suppress_callback_exceptions']=True
