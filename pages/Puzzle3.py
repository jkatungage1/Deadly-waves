from dash import html, dash, dash_table, dcc, callback, Output, Input,State,ctx
import json, logging, time, os, pandas as pd, plotly.graph_objects as go, dash as d
from PIL import Image

img_src= 'https://cdn.discordapp.com/attachments/1075182862598414377/1215771024243691712/image.png?ex=65fdf600&is=65eb8100&hm=67d065ae66a2a94f6cfddd2b59f6c93f3864b6b1f2da10176485a693026ca7f0&'    
d.register_page(__name__) #'/' means it's the maine page

layout = html.Div([
    
    html.Div(html.Img(id='cachan_image',
                              src=img_src,style={
                                  
                                'width':'500px',
                                'display':'block',
                                'height':'auto',
                                'margin-right': 'auto',
                                'margin-left' :'auto'
                                                  
            })),
            
    html.H1(id='Title',
                    children=' Puzzle 3',
                    style={
                        'text-align' : 'center',
                        'color': 'Red',
                        'font-family':'monospace'
                    })
    
    
])