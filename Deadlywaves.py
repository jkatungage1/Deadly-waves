from dash import Dash as d, html, dash, dash_table, dcc, callback, Output, Input,State,ctx
import dash,json, logging, time, os, pandas as pd, plotly.graph_objects as go
from PIL import Image


img_src= 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmZlerAavnOiz98igv9owprofau87uNoWPxrLL3OwJUQ&s'    
pil_img = Image.open("webimg.png")

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
external_stylesheet = ['https://codepen.io/chiriddyp/pen/bWLwgP.css']

# ANG_DIST_TABLE = get_table()


def Deadly_waves():

    app = d(__name__,use_pages=False)

    app.layout = html.Div([

            html.Div(html.Img(src=img_src),style={
                                                  'fontsize':'50',
                                                  'padding-top': '10px',
                                                  'padding-left' :'auto'
                                                  
                                                  }),
            
            html.H1(id='Title',
                    children=' Deadly waves :',
                    style={
                        'text-align' : 'center',
                        'color': 'blue',
                        'font-family':'monospace'
                    }),
            
            
            html.Div(id='container-button-basic',children='Who is the killer ? QUICK! The waves are comming and you only have three tries to start the disruptor !'),
        
                       
            
            html.Div(dcc.Input(id='input-on-submit', type='text')),
            html.Button(children = 'Submit', id='submit-val', n_clicks=0),
            dcc.Markdown('what frequency is represented by this CYMATICS '),
            dcc.Link('CYMATICS',href='https://en.wikipedia.org/wiki/Cymatics'),
            dcc.Dropdown(options=[250,440,1000,1000000],id='frequences',style={
                'width':'60%',
                'padding-left' : '35%'
                }),
            
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
        
        essais = 3 - n_clicks
        txt = "T'as cliqué 😉"+str(n_clicks)+" fois Il te reste : "+str(essais)+" essais !" 
        print(n_clicks,value) 
        if ( essais == 0) :
            if (value == 'Jacques') : 
                txt = " Gagné !!"
            else :
                txt = "PERDU !!"
        
        return txt
      


    return app


if __name__ == '__main__':
  Deadly_waves().run_server(host="0.0.0.0", debug=True)


