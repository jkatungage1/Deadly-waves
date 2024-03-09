from dash import html, dash, dash_table, dcc, callback, Output, Input,State,ctx
import json, logging, time, os, pandas as pd, plotly.graph_objects as go, dash as d
from PIL import Image

img_src1= 'https://cdn.discordapp.com/attachments/1075182862598414377/1215948704855359548/image.png?ex=65fe9b7a&is=65ec267a&hm=35ff185788bb96ed8b93cdfa851cf763d9e0eb982ae4c4cf54fc02c7ef8728e2&'    
img_src2 = 'https://cdn.discordapp.com/attachments/1075182862598414377/1215771024243691712/image.png?ex=65fdf600&is=65eb8100&hm=67d065ae66a2a94f6cfddd2b59f6c93f3864b6b1f2da10176485a693026ca7f0&S'


d.register_page(__name__) #'/' means it's the maine page

layout = html.Div([
    
    html.Div(html.Img(id='cachan_image',
                              src=img_src1,style={
                                                  'width':'500px',
                                                  'height':'auto',
                                                  'padding-top': '0px',
                                                  'padding-left' :'0px'
                                                  
            })
            #  html.Img(id='cachan_image',
            #                   src=img_src2,style={
            #                                       'width':'500px',
            #                                       'height':'auto',
            #                                       'padding-top': '0px',
            #                                       'padding-left' :'0px'
                                                  
            # })
             
             ),
    
            
    html.H1(id='Title',
                    children=' Puzzle 2',
                    style={
                        'text-align' : 'center',
                        'color': 'Red',
                        'font-family':'monospace'
                    }),
])