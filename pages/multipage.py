from dash import html, dash_table, dcc, callback, Output, Input,State,ctx
import json, logging, time, os, pandas as pd, plotly.graph_objects as go, dash as d, dash_bootstrap_components as dbc
from PIL import Image
from Deadlywaves import EQUIPES,hots
from Deadlywaves import PAGES
from flask import request




back_img = 'data:image/jpeg;base64,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'
img_src= 'data:image/png;base64,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'    
d.register_page(__name__,path='/') #'/' means it's the maine page

layout = html.Div([
    

    
    html.Div(html.Img(id='Network',
                        src=img_src,style={
                                    'margin-top':'400px',
                                    'width':'200px',
                                    'height':'auto',
                                    'display': 'block',
                                    'margin-left' :'auto',
                                    'margin-right' :'auto'                                          
    })),
    
    html.Div([html.Div([
        
        html.Img()
        
    ])]),
            
    html.H1(id='Title',
                    children=' Identification ',
                    style={
                        'font-size':'1.5em',
                        'text-align' : 'center',
                        'color': 'blue',
                        'font-family':'monospace'
    }),
    html.Div(style ={
            'text-align' : 'center',
            'display': 'block',
            'margin-left' :'auto',
            'margin-right' :'auto' 
        },
        id='Start Text',
        children='What is the name of your team ? 😶‍🌫️'),
    html.Div(style ={
            'text-align' : 'center',
            'display': 'block',
            'margin-left' :'auto',
            'margin-right' :'auto' 
        },
             
    children = [dcc.Input(id='input-on-submit', type='text',
            style={
                
                'width':'180px',
                'height':'23px',
                'padding-top': '5px',
                'verticalAlign':'middle'
    }),
                html.Button(style ={
                'width':'100px',
                'height':'30px',
                'line-height': '15px',
                'verticalAlign':'middle'
    },
                            children = 'Submit', id='submit-val', n_clicks=0),
    
    ]),
      
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

            html.Button(style ={
            'text-align' : 'center',
            'display': 'block',
            'margin-left' :'auto',
            'margin-right' :'auto' 
        },children = dbc.Button(id='Start',children = "Start !",href='http://'+hots+':8050/puzzle1',disabled=True)), #href='http://127.0.0.1:8050/puzzle1'
           
           
            # dcc.Markdown('what frequency is represented by this CYMATICS '),
            
    
   
])

@callback(
            Output(component_id='Title', component_property='children'),
            Input("submit-val","n_clicks"),
            
            prevent_initial_call=True  
        )
def rien (n_clicks) :
   
    from Deadlywaves import EQUIPES
    ipa = request.remote_addr
    free = True
    id = None
    for teams in EQUIPES:
        
        if ipa == teams[1] :
            free = False 
            id = teams[0]
          
        else : 
            free = True
            id = teams[0]
         
        if ( free == 0) :
            
            txt = "Welcome team {value} the game will start as you press the start Button !".format(value=id )
            return txt
        else : 
            txt = "Welcome team {value} the game will start as you press the start Button !".format(value=id )
            return txt
    
    # txt = "Welcome team {value} the game will start as you press the start Button !".format(value=str(EQUIPES[][0]) )
    # print(n_clicks,value) 


@callback(Output('Start', 'disabled'),
             [Input('submit-val', 'n_clicks'),Input('Team Ip address','children')])
def set_button_enabled_state(n_clicks,children):
    
    if (n_clicks > 0 and children != 'IP') :
        on_off = False
    else : on_off = True
    return on_off
    
    
    
