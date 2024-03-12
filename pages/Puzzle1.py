from dash import html, dash, dash_table, dcc, callback, Output, Input,State,ctx
import json, logging, time, os, pandas as pd, plotly.graph_objects as go, dash as d, dash_bootstrap_components as dbc
from PIL import Image
from Deadlywaves import EQUIPES,hots
from Deadlywaves import PAGES
from flask import request

img_src= 'https://cdn.discordapp.com/attachments/1075182862598414377/1216992530122543134/Colorful_Fruits_Straightforward_Education_Landscape_Poster.png?ex=6602679d&is=65eff29d&hm=66fe8e0923d57d7d5e3938c97ecd47c7d2aeb44fef931d1704e75ecd1406e217&'    
d.register_page(__name__) #'/' means it's the maine page

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
    }),
    
    # html.Div(className='flex-container',children=[1,2,3] ),
    html.Div(id='Start Text',children='What is the name of your team ? 😶‍🌫️'),
            html.Div(dcc.Input(id='input-on-submit', type='text',
                    style={
                        'width':'180px',
                        'height':'23px',
                        'padding-top': '5px',
                        'verticalAlign':'middle'
                    })),
            html.Button(children = 'Submit', id='submit-val', n_clicks=0),
    
    
    
    html.Button(dbc.Button(id='Start',children = "Start !",href='http://'+hots+':8050/puzzle1',disabled=True)),
])