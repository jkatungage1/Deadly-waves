from dash import html, dash, dash_table, dcc, callback, Output, Input,State,ctx
import json, logging, time, os, pandas as pd, plotly.graph_objects as go, dash as d, dash_bootstrap_components as dbc
from PIL import Image
from flask import request
from Deadlywaves import EQUIPES,hots
from Deadlywaves import PAGES


#variables setup
img_width = 300
img_height = 'auto'
img_src= 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmZlerAavnOiz98igv9owprofau87uNoWPxrLL3OwJUQ&s' 

VALIDATED = [[1,False],[2,False],[3,False]]  
pz1 = 'https://cdn.discordapp.com/attachments/1075182862598414377/1217112234006679612/image.png?ex=6602d719&is=65f06219&hm=06e63e957822b21885fe190e3d32a39daa5e653f03b560bfb1b9d89c70b42afb&'
pz1a = 'traitor'
pz2 = 'https://cdn.discordapp.com/attachments/1075182862598414377/1217116878112165999/image.png?ex=6602db6c&is=65f0666c&hm=9710866d7c14cb2a675a3def2a1456d20b4ddeb95603c2820e6366b22ab84230&'
pz3 = 'https://cdn.discordapp.com/attachments/1075182862598414377/1217112657484578866/image.png?ex=6602d77e&is=65f0627e&hm=ad9e2a9983105321ef5bcf17f849eeec6b22b0d4b5dbe196c93175c23c9270eb&'
pz4 = 'https://cdn.discordapp.com/attachments/1075182862598414377/1217117062447763597/image.png?ex=6602db98&is=65f06698&hm=c8d5877b4e980fe32dd0e1bc7bf751594859fa25a4ec047e3cbea628a3da4c4c&'
# pz1 = None 

img_src1= 'https://cdn.discordapp.com/attachments/1075182862598414377/1215948704855359548/image.png?ex=65fe9b7a&is=65ec267a&hm=35ff185788bb96ed8b93cdfa851cf763d9e0eb982ae4c4cf54fc02c7ef8728e2&'    
img_src2 = 'https://cdn.discordapp.com/attachments/1075182862598414377/1215771024243691712/image.png?ex=65fdf600&is=65eb8100&hm=67d065ae66a2a94f6cfddd2b59f6c93f3864b6b1f2da10176485a693026ca7f0&S'


d.register_page(__name__) #'/' means it's the maine page

layout = html.Div([
    
     
    html.Div(style={
                        'margin-top' : '270px',
                        'margin-left' : '100px',
                        'margin-right':'auto',
                        'display':'block'
    },children = [
        

               
            html.Img(id='pz1',
                        src=pz1,style={
                                            'width':str(img_width)+'px',
                                            'height':str(img_height)+'px',
                                            'padding-top': '0px',
                                            'padding-left' :'30px'
                                            
    }),
            
            
            html.Img(id='pz2',
                        src=pz2,style={
                                            'width':str(img_width)+'px',
                                            'height':str(img_height)+'px',
                                            'padding-top': '0px',
                                            'padding-left' :str(img_width/2)+'px'
                                            
    }),
                        
            html.Img(id='pz3',
                        src=pz3,style={
                                            'width':str(img_width)+'px',
                                            'height':str(img_height)+'px',
                                            'padding-top': '0px',
                                            'padding-left' :str(img_width/2)+'px'
                                            
    }),
            html.Div([dcc.Dropdown(options=["cos * sin","vert = (e^ix+e^−ix) / 2 et rouge = e^ix-e^−ix / 2i","cos(x)","rouge = (e^ix+e^−ix) / 2  et vert = e^ix-e^−ix / 2i "]
                                   ,id='functions1',style={
                
                'margin-left' : '25px',                                                             
                'width':'200px',
                
                                                   
            },disabled=False,),
                      dcc.Dropdown(options=["cos * sin","vert = (e^ix+e^−ix) / 2 et rouge = e^ix-e^−ix / 2i","cos(x)","rouge = (e^ix+e^−ix) / 2  et vert = e^ix-e^−ix / 2i "]
                                   ,id='functions2',style={
                
                'margin-left' : '160px',                                                             
                'width':'200px',
                'height':'30px'
                
            },disabled=False,),
                      
                      dcc.Dropdown(options=["cos * sin","vert = (e^ix+e^−ix) / 2 et rouge = e^ix-e^−ix / 2i","cos(x)","rouge = (e^ix+e^−ix) / 2  et vert = e^ix-e^−ix / 2i "]
                                   ,id='functions3',style={
               
                'margin-left' : '220px',                                                             
                'width':'200px',
                'height':'auto'
                                                    
            },disabled=False,)
                      
                      ],style={
                'display':'-webkit-inline-box'
            }),

    ]),
            
   
 
    html.Div([
        
        #Image 1 input
        html.Img(id='pz4',
                        src=pz4,style={
                                            'width':str(img_width)+'px',
                                            'height':str(img_height)+'px',
                                            'padding-top': '0px',
                                            'padding-left' :'600px'}),
        
        html.Button(style ={
                
                'width':'100px',
                'height':'30px',
                'line-height': '15px',
                'verticalAlign':'middle'
                            },
                    children = 'Submit', id='submit-val', n_clicks=0)
        ]),
    
    
    html.Div(children=[
        
        html.Div(id ='pz1av',children ="?") 
        #,html.H3(dbc.Textarea())
        
    ]),
    
            
    
    dcc.Dropdown(options=[300,500,1000,10000],id='frequences',style={
                # 'width':'60%',
                'padding-left' : '50%',                                                             
                'width':'100px',
                'height':'auto',
                'padding-top': '0px',
                'padding-left' :'0px'                                     
            },disabled=True,),
    

    
    
    
    html.Button(style ={
            'text-align' : 'center',
            'display': 'block',
            'margin-left' :'auto',
            'margin-right' :'auto', 
            'margin-top' :'20px'
        },
                children = dbc.Button(id='Start2',children = "Step 3",href='http://'+hots+':8050/puzzle3',disabled=True)) 
])

@callback(
    Output("Start2","disabled"),
    [State(),State(),State()],
    prevent_
    
    
)