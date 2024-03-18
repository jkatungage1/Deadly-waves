from dash import html, dash, dash_table, dcc, callback, Output, Input,State,ctx
import json, logging, time, os, pandas as pd, plotly.graph_objects as go, dash as d, dash_bootstrap_components as dbc
from PIL import Image
from flask import request
from Deadlywaves import EQUIPES,hots,T
from Deadlywaves import PAGES

img_width = 300
img_height = 'auto'
img_src= 'https://cdn.discordapp.com/attachments/1075182862598414377/1215771024243691712/image.png?ex=65fdf600&is=65eb8100&hm=67d065ae66a2a94f6cfddd2b59f6c93f3864b6b1f2da10176485a693026ca7f0&'
pz31 = "https://cdn.discordapp.com/attachments/1075182862598414377/1219393658747617473/image.png?ex=660b23d7&is=65f8aed7&hm=43c6a75b77ece20007d6f5820aa43f95dde1537e70e87fa395986b71122436c0&"
pz32 = "https://cdn.discordapp.com/attachments/1075182862598414377/1219393658290307133/image.png?ex=660b23d7&is=65f8aed7&hm=409672d2de03082343be474372dfa56b744c5335b66dbdc81da8bce2c776beea&"
pz33 = "https://cdn.discordapp.com/attachments/1075182862598414377/1219393414953566380/image.png?ex=660b239d&is=65f8ae9d&hm=e7c6877850787f0c2b77d3a958a27f1ec7e2ea4d8edf5708f4cf2ff25042830e&"
pz34 = "https://cdn.discordapp.com/attachments/1075182862598414377/1219393414588665886/image.png?ex=660b239d&is=65f8ae9d&hm=58a775e51f17b3d910c4e55fb241f04f3a2c3e855bfa5d993913e54ec6175e4e&"   



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
            'margin-top':'200px'
        }),
            
    html.H1(id='Title3',
                    children=' Puzzle 3',
                    style={
                        'text-align' : 'center',
                        'color': 'Red',
                        'font-family':'monospace'
                    }),
    
    
    html.Img(id='pz31',
                        src=pz31,style={
                                            'width':str(img_width)+'px',
                                            'height':str(img_height)+'px',
                                            'padding-top': '0px',
                                            'padding-left' :'30px'
                                            
    }),
    
    html.Img(id='pz32',
                        src=pz32,style={
                                            'width':str(img_width)+'px',
                                            'height':str(img_height)+'px',
                                            'padding-top': '0px',
                                            'padding-left' :'30px'
                                            
    }),
    html.Img(id='pz33',
                        src=pz33,style={
                                            'width':str(img_width)+'px',
                                            'height':str(img_height)+'px',
                                            'padding-top': '0px',
                                            'padding-left' :'30px'
                                            
    }),
    html.Img(id='pz34',
                        src=pz34,style={
                                            'width':str(img_width)+'px',
                                            'height':str(img_height)+'px',
                                            'padding-top': '0px',
                                            'padding-left' :'30px'
                                            
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
        return 'Find the word to stop the bomb, the shockwaves would cause a disaster !'
        
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
    elif (n_clicks > 3 and value != victoire ) : return 'YOU DIED !'
    
    else : return " Welp, that's gg's (sike) !"
    
    
    