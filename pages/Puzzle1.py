from dash import html, dash, dash_table, dcc, callback, Output, Input,State,ctx
import json, logging, time, os, pandas as pd, plotly.graph_objects as go, dash as d, dash_bootstrap_components as dbc
from PIL import Image
from Deadlywaves import EQUIPES,hots
from Deadlywaves import PAGES
from flask import request


#variables setup
img_width = 220
img_height = img_width*2
img_src= 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmZlerAavnOiz98igv9owprofau87uNoWPxrLL3OwJUQ&s' 

VALIDATED = [[1,False],[2,False],[3,False]]  
pz1 = 'data:image/jpeg;base64,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'
pz1a = 'IUT'

pz2 = None
pz2a='DE'

pz3 = None
pz3a='CACHAN'
# pz4 = None
# pz1 = None 


#Layout setup
d.register_page(__name__) #'/' means it's the maine page

layout = html.Div([
    
     html.H1(id='Title',
                    children=' Puzzle 1',
                    style={
                        'font-size':'2em',
                        'text-align' : 'center',
                        'color': 'red',
                        'font-family':'monospace',
                        'margin-bottom' : '2px'
    }),
     
    html.Div(children = [
            
            html.Img(id='pz1',
                        src=pz1,style={
                                            'width':str(img_width)+'px',
                                            'height':str(img_height)+'px',
                                            'padding-top': '0px',
                                            'padding-left' :str(img_width)+'px'
                                            
    }),
             html.Img(id='pz2',
                        src=pz2,style={
                                            'width':str(img_width)+'px',
                                            'height':str(img_height)+'px',
                                            'padding-top': '0px',
                                            'padding-left' :str(img_width)+'px'
                                            
    }),
             html.Img(id='pz3',
                        src=pz3,style={
                                            'width':str(img_width)+'px',
                                            'height':str(img_height)+'px',
                                            'padding-top': '0px',
                                            'padding-left' :str(img_width)+'px'
                                            
    })]),
            
   
    # html.Div(className='flex-container',children=[1,2,3] ),
    html.Div(id='',children=''),
    html.Div([
        #Image 1 input
        dcc.Input(id='pz1a', type='text',
            style={
                'width':'180px',
                'height':'23px',
                'margin-left': str(img_width)+'px',
                'verticalAlign':'middle'
            }),
        html.Button(style ={
                'width':'100px',
                'height':'30px',
                'line-height': '15px',
                'verticalAlign':'middle'
                            },
                    children = 'Submit', id='submit-val', n_clicks=0),
        
        #Image 2 input
        dcc.Input(id='pz2a', type='text',
            style={
                'width':'180px',
                'height':'23px',
                'margin-left': str(img_width-31)+'px',
                'verticalAlign':'middle'
            }),
        # html.Button(style ={
        #         'width':'100px',
        #         'height':'30px',
        #         'line-height': '15px',
        #         'verticalAlign':'middle'
        #                     },
        #             children = 'Submit', id='submit-val', n_clicks=0),
        
        
        #Image 3 input
        dcc.Input(id='pz3a', type='text',
            style={
                'width':'180px',
                'height':'23px',
                'margin-left': str(img_width-31)+'px',
                'verticalAlign':'middle'
            })
        # html.Button(style ={
        #         'width':'100px',
        #         'height':'30px',
        #         'line-height': '15px',
        #         'verticalAlign':'middle'
        #                     },
        #             children = 'Submit', id='submit-val', n_clicks=0)
        
        
        
        
        
        
        ]),
    
    
    html.Div(children=[
        
        html.Div(id ='pz1av',children ="?"),html.Div(id ='pz2av',children ="?"),html.Div(id ='pz3av',children ="?")
    ]),
    
    
    
    html.Button(style ={
            'text-align' : 'center',
            'display': 'block',
            'margin-left' :'auto',
            'margin-right' :'auto', 
            'margin-top' :'20px'
        },
                children = dbc.Button(id='Start',children = "Start !",href='http://'+hots+':8050/puzzle1',disabled=True)) #href='http://127.0.0.1:8050/puzzle1'
])
@callback(
            Output(component_id='pz1av', component_property='children'),
            # Input("refresh-interval", "n_intervals"),
            [Input("refresh-interval", "n_intervals")],
            [State('pz1a', 'value'),],
            prevent_initial_call=True  

        )
def check_pz (n_intervals,value) :
    if ( value == pz1a ) :
        return 'Correct !'