from dash import html, dash, dash_table, dcc, callback, Output, Input,State,ctx
import json, logging, time, os, pandas as pd, plotly.graph_objects as go, dash as d
from PIL import Image

img_src= 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmZlerAavnOiz98igv9owprofau87uNoWPxrLL3OwJUQ&s'    
d.register_page(__name__,path='/') #'/' means it's the maine page

layout = html.Div([
    
    html.Div(html.Img(id='cachan_image',
                              src=img_src,style={
                                                  'width':'100px',
                                                  'height':'auto',
                                                  'padding-top': '0px',
                                                  'padding-left' :'0px'
                                                  
    })),
            
    html.H1(id='Title',
                    children=' Puzzle 1',
                    style={
                        'text-align' : 'center',
                        'color': 'Red',
                        'font-family':'monospace'
    })
])