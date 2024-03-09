from dash import Dash as d, html, dash, dash_table, dcc, callback, Output, Input,State,ctx
import dash,json, logging, time, os, pandas as pd, plotly.graph_objects as go
from PIL import Image
from flask import request

EQUIPES = [[]]
img_src= 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmZlerAavnOiz98igv9owprofau87uNoWPxrLL3OwJUQ&s'  
game_src= ''  
pil_img = Image.open("webimg.png")

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
external_stylesheet = ['https://codepen.io/chiriddyp/pen/bWLwgP.css']

colors = {'background': '#ffffff',
          'bg_home': '#666666',
          'text': '#ffa500',
          'background_plot': '#cccccc',
          'text_plot': '#000000'}



def Deadly_waves():

    app = d(__name__,use_pages=True,external_stylesheets = external_stylesheet)

    app.layout = html.Div(
        
        # style={
        # #         'background-image': 'url(img_src)',
        # #         'background-repeat': 'no-repeat',
        # #         'background-position': 'right top',
        # #         'background-size': '150px 100px'
        #     },
        
        # 'background-image': 'url("/assets/wallpaper.jpg")', 
        #                      'background-size': 'cover', 'background-repeat': 'no-repeat',
        #                      'background-position': 'center', 'height': '100vh'},
    
        [
        


            html.Div([html.Img(id='cachan_image',
                              src=img_src,style={
                                                  'width':'100px',
                                                  'height':'auto',
                                                  'padding-top': '0px',
                                                  'padding-left' :'0px'
                                                  
            })
    
            ]),
            
            html.H1(id='Title',
                    children=' BEWARE.. the Deadly waves are coming  :',
                    style={
                        'textAlign' : 'center',
                        'color': 'blue',
                        'font-family':'monospace'
                    }),
            
            html.Div([
                
                dcc.Link(page['name']+"  |  ",href=page['path'])
                for page in dash.page_registry.values()
            ]),
            
            html.Hr(),
            
            dash.page_container,
            
            
            
            html.Div(id='container-button-basic',children='What is the name of your team ? !'),
            html.Div(dcc.Input(id='input-on-submit', type='text',
                    style={
                        'width':'180px',
                        'height':'23px',
                        'padding-top': '5px',
                        'verticalAlign':'middle'
                    })),
            html.Button(children = 'Submit', id='submit-val', n_clicks=0)
            
            
            # { this is the style sheet for the button 

#     display: inline-block;
#     height: 24px;
#     padding: 0 30px;
#     color: #555;
#     text-align: justify;
#     font-size: 9px;
#     font-weight: 600;
#     line-height: 2;
#     letter-spacing: .1rem;
#     text-transform: uppercase;
#     text-decoration: none;
#     white-space: nowrap;
#     background-color: transparent;
#     border-radius: 4px;
#     border: 1px solid #bbb;
#     cursor: pointer;
#     box-sizing: border-box;
# }


            ,
           
            html.Button(children = 'Start game !', id='start game', n_clicks=0,),
           
           
            # dcc.Markdown('what frequency is represented by this CYMATICS '),
            # dcc.Link('CYMATICS',href='https://en.wikipedia.org/wiki/Cymatics'),
            # dcc.Dropdown(options=[250,440,1000,1000000],id='frequences',style={
            #     'width':'60%',
            #     'padding-left' : '35%'
            #     }),
            
            dcc.Interval(id="refresh-interval", disabled=False, interval=100)
            
    ])
    @callback(
            Output(component_id='container-button-basic', component_property='children'),
            # Input("refresh-interval", "n_intervals"),
            Input("submit-val","n_clicks"),
            # State('input-on-submit', 'value'),
            prevent_initial_call=True  
        )
    def rien (n_clicks) :
        global EQUIPES
       
        
        return None


    return app


if __name__ == '__main__':
  Deadly_waves().run_server(host="192.168.137.1", debug=True)


