from dash import Dash as d, html, dash, dash_table, dcc, callback, Output, Input,State,ctx
import json, logging, time, os, pandas as pd, plotly.graph_objects as go
from PIL import Image


img_src= 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmZlerAavnOiz98igv9owprofau87uNoWPxrLL3OwJUQ&s'    #
pil_img = Image.open("C:/Users/Muken/OneDrive/Travail/Mukendi_jacques/English/Escape game/webimg.png")

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
ANG_DIST_TABLE = None
# CPT = 0
PLOT_ON = False
# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
external_stylesheet = ['https://codepen.io/chiriddyp/pen/bWLwgP.css']

# ANG_DIST_TABLE = get_table()


def lidar_plot():

    app = d(__name__)

    app.layout = html.Div([
            html.Div(html.Img(src=pil_img),style={'width':'150','height':'150'}),
            html.Div(id='container-button-basic',children='Enter a value and press submit'),
        
            html.Div(id='Title',
                    children=' Deadly waves :',
                    style={
                        'vertical-align' : 'center',
                        'color': 'blue'
                    }),
            
            
            html.Div(dcc.Input(id='input-on-submit', type='text')),
            html.Button(children = 'Submit', id='submit-val', n_clicks=0),
            
            
            dcc.Interval(id="refresh-interval", disabled=False, interval=100)
    ])


    @callback(
            Output(component_id='container-button-basic', component_property='children'),
            # Input("refresh-interval", "n_intervals"),
            Input("submit-val","n_clicks"),
            State('input-on-submit', 'value'),
            prevent_initial_call=True  
        )
    def rien (n_clicks,value) :
        txt = "T'as cliqué 😉" 
        print(n_clicks,value) 
        return txt
        # if ( (n_clicks%1) == 2) :
        #     txt = "T'as cliqué 😉"
        


    return app


if __name__ == '__main__':
  lidar_plot().run_server(host="0.0.0.0", debug=True)


