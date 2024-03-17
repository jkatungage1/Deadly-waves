from dash import html, dash, dash_table, dcc, callback, Output, Input,State,ctx
import json, logging, time, os, pandas as pd, plotly.graph_objects as go, dash as d, dash_bootstrap_components as dbc
from PIL import Image


from Deadlywaves import PAGES, hots
from flask import request


#variables setup
img_width = 100
img_height = img_width*2
img_src= 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmZlerAavnOiz98igv9owprofau87uNoWPxrLL3OwJUQ&s' 

VALIDATED = [[1,False],[2,False],[3,False]]  
pz1 = 'https://cdn.discordapp.com/attachments/1075182862598414377/1217097738521542726/image.png?ex=6602c999&is=65f05499&hm=34b20bd2f64de163445318b975c2baa5bb34c9b7246122c071ee66ca6f188d5a&'
pz1a = 'traitor'

pz2 = 'https://cdn.discordapp.com/attachments/1075182862598414377/1217097714689380403/image.png?ex=6602c993&is=65f05493&hm=b0eb85a03b7a69fc28defb5253e322a481485dcd2c08597dacfeae094acfdc8a&'
pz2a='DE'

pz3 = 'https://cdn.discordapp.com/attachments/1075182862598414377/1217097660037730505/image.png?ex=6602c986&is=65f05486&hm=4c39a678bcc395615d60fa6b21dbf88a9c9693db10956885ef2f923cabc7eb3c&'
pz3a='CACHAN'
pz4 = 'https://cdn.discordapp.com/attachments/1075182862598414377/1217109501824466964/image.png?ex=6602d48e&is=65f05f8e&hm=21ddd5cf5d4c8ebd05b3528b3a2018a01b1c40f9be407e8073dad5cc821fef17&' 


#Layout setup
d.register_page(__name__) #'/' means it's the maine page

layout = html.Div([
    
    html.H1(id='Title',
                    children='',
                    style={
                        # 'font-size':'4em',
                        # 'text-align' : 'center',
                        # 'color': 'red',
                        # 'font-family':'monospace',
                        # 'margin-bottom' : '2px'
    }),
     
    html.Div(style={
                        'margin-top' : '200px',
                        'margin-left' : '0px',
                        'margin-right':'auto',
                        'display':'block'
    },children = [
        
            html.Img(id='pz4',
                        src=pz4,style={
                                            'width':str(img_width*3)+'px',
                                            'height':'auto',
                                            'padding-top': '0px',
                                            'padding-left' :'0 px'}),
               
            html.Img(id='pz1',
                        src=pz1,style={
                                            'width':str(img_width)+'px',
                                            'height':str(img_height)+'px',
                                            'padding-top': '0px',
                                            'padding-left' :str(img_width+100)+'px'
                                            
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
            
   
 
    html.Div(id='',children=''),
    #Image 1 input
        dcc.Input(id='pz1a', type='text',
            style={
                
                'margin-left':'600px',
                'width':'180px',
                'height':'23px',
                'verticalAlign':'middle'
            },value=" Guess "),
    html.Button(style ={
            
            'width':'100px',
            'height':'30px',
            'line-height': '15px',
            'verticalAlign':'middle'
                        },
                children = 'Submit', id='page1complete', n_clicks=0),

    
    html.Div(children=[
        
        html.H4(id ='pz1av',children ="?") #,html.H3(dbc.Textarea())
        
    ]),
    
    
    
    html.Button(style ={
            'text-align' : 'center',
            'display': 'block',
            'margin-left' :'auto',
            'margin-right' :'auto', 
            'margin-top' :'20px'
        },
                children = dbc.Button(id='Start1',children = "Step 2",href='http://'+hots+':8050/puzzle2',disabled=True)) 
    
    ])


@callback(
            [Output(component_id='pz1av', component_property='children'),Output(component_id='Start1', component_property='disabled')],
            [Input("page1complete", "n_clicks")],
            State('pz1a', 'value'),           
            prevent_initial_call=True  
        )

def check_pz (n_clicks,value) :
    if ( value == pz1a ) :
        print("c'ests bon")
        return ["Correct !",False]
    else : return ["Enter the word corresponding to the clues you've gathered !",True]
    
    

    











