from dash import html, dash, dash_table, dcc, callback, Output, Input,State,ctx
import json, logging, time, os, pandas as pd, plotly.graph_objects as go, dash as d, dash_bootstrap_components as dbc
from PIL import Image
from flask import request
from Deadlywaves import EQUIPES,hots,T
from Deadlywaves import PAGES


img_src= 'https://cdn.discordapp.com/attachments/1075182862598414377/1215771024243691712/image.png?ex=65fdf600&is=65eb8100&hm=67d065ae66a2a94f6cfddd2b59f6c93f3864b6b1f2da10176485a693026ca7f0&'    
d.register_page(__name__) #'/' means it's the maine page
victoire = 'oui'


layout = html.Div([
    
    html.Div(html.Img(
                      id='cachan_image',
                              src=img_src,style={
                                  
                                'width':'500px',
                                'display':'block',
                                'height':'auto',
                                'margin-right': 'auto',
                                'margin-left' :'auto'
                                                  
            }),style={
            'margin-top':'300px'
        }),
            
    html.H1(id='Title3',
                    children=' Puzzle 3',
                    style={
                        'text-align' : 'center',
                        'color': 'Red',
                        'font-family':'monospace'
                    }),
    
    
    dcc.Input(id='input-on-submit', type='text',
            style={
                'margin-top':'40px',
                'margin-left':'500px',
                'width':'180px',
                'height':'23px',
                'padding-top': '5px',
                'verticalAlign':'middle'
    }),
                html.Button(style ={
                'margin-top':'40px',
                'margin-left':'0',
                'width':'100px',
                'height':'30px',
                'line-height': '15px',
                'verticalAlign':'middle'
    },id='FIN',children = 'Submit',  n_clicks=0)
    
    
])

@callback(Output('Title3', 'children'),
             [Input('FIN', 'n_clicks'),Input('input-on-submit','value')] 
        )
def victory(n_clicks,value):
    # print (n_clicks)
    
    if (n_clicks == 0 ) :
        print(n_clicks,'they are...')        
        return 'They are coming !'
        
    elif (n_clicks == 1 ) : 
        if(value == victoire):
             
            # T.stop()
            return "You won ! "
            
        else : return 'WRONG, be quicker, They are coming !'
    elif (n_clicks == 2 ) : 
        if(value == victoire): 
            
            # T.stop()
            return "You barely won ! "
        else : return 'LAST TRY, FOCUS RECRUIT ! '
    
    elif (n_clicks == 3 ) : 
        if(value == victoire): 
            return "You almost DIED but.. you'll make it home this time.. ! "
        else : return 'YOU DIED !'
        
    # elif (n_clicks == 3 and value == victoire): 
    #     return 'vous êtes mort(s)!'
    elif (n_clicks > 3 ) : return 'YOU DIED !'
    
    
    