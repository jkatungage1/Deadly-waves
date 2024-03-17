from dash import Dash as d, html, dash, dash_table, dcc, callback, Output, Input,State,ctx
import dash,json, logging, time, os, pandas as pd, plotly.graph_objects as go,random,timer
from PIL import Image
from flask import request


# class TimerError(Exception):
#     """A custom exception used to report errors in use of Timer class"""

# class Timer:
#     def __init__(self):
#         self._start_time = None

#     def start(self):
#         """Start a new timer"""
#         if self._start_time is not None:
#             raise TimerError(f"Timer is running. Use .stop() to stop it")

#         self._start_time = time.perf_counter()

#     def stop(self):
#         """Stop the timer, and report the elapsed time"""
#         if self._start_time is None:
#             raise TimerError(f"Timer is not running. Use .start() to start it")

#         elapsed_time = time.perf_counter() - self._start_time
#         self._start_time = None
#         print(f"Elapsed time: {elapsed_time:0.4f} seconds")




T = 0
ST_TIMER = True
EQUIPES = []
PAGES = []
DEFAULT_LEVEL = 0
hots="192.168.137.1"
img_src= 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmZlerAavnOiz98igv9owprofau87uNoWPxrLL3OwJUQ&s'  
back_img = 'https://cdn.discordapp.com/attachments/1075182862598414377/1216992530122543134/Colorful_Fruits_Straightforward_Education_Landscape_Poster.png?ex=6602679d&is=65eff29d&hm=66fe8e0923d57d7d5e3938c97ecd47c7d2aeb44fef931d1704e75ecd1406e217&'
game_src= ''  
pil_img = Image.open("webimg.png")

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


external_stylesheet = ['https://codepen.io/chiriddyp/pen/bWLwgP.css']

colors = {'background': '#166fb7b0',
          'bg_home': '#666666',
          'text': '#ffa500',
          'background_plot': '#cccccc',
          'text_plot': '#000000'}



def Deadly_waves():
    global PAGES
    app = d(__name__,use_pages=True,external_stylesheets = external_stylesheet)

    app.layout = html.Div(
        
        style={
                
                'background-image': 'url('+str(back_img)+')',
                'background-repeat': 'no-repeat',
                'background-position-y': '10px',
                'background-size': 'contain',
                'background-clip':'border-box'
            },
        
        
    
        children = [
        


            html.Div(style = {}, children = [html.Img(id='cachan_image',
                              src=img_src,style={
                                                  'width':'100px',
                                                  'height':'auto',
                                                  'padding-top': '0px',
                                                  'padding-left' :'0px'                                                  
                                                  
            }), html.Div(id='timer',style={
                
                'display':'inline-block'
                
                },children=['TEMPS'])
    
            ]),
            
        
            
            html.Hr(),
            
            dash.page_container,
          
            
            dcc.Interval(id="refresh-interval", interval=500),# disabled=False),
            html.Div(id='Team Ip address',children='IP',style={
                'margin-top':'100px',
                'display':'block',
                'padding-right': 'auto',
                'padding-left' :'auto',
                'textAlign' : 'center'
                
            }),
            html.Div(id='',children='By Zohra and Jacques',style={
                'margin-top':'1000px'
                
                
            })
            
                    
    ])
    
    
   
  
    
    @callback(
            Output(component_id='Start Text', component_property='children'),
            Input("submit-val","n_clicks"),
            State('input-on-submit', 'value'),
            prevent_initial_call=True  

        )
    def equipes_ (n_clicks,value) :
        # global EQUIPES
        
        # EQUIPES.append([value,request.remote_addr,0])
        # print (EQUIPES)
        # txt = "Vous êtes enregistrés en tant qu'équipe {Teamname} : {ipaddress}!".format(Teamname=value,ipaddress=request.remote_addr)
        # return txt
        global EQUIPES, PAGES
        PAGES = [dcc.Link(page['name']+"  |  ",href=page['path'])
                for page in dash.page_registry.values()]
        
        ipa = request.remote_addr
        free = True
        for teams in EQUIPES:
            if ipa == teams[1] :
                free = False 
            else : 
                free = True
        if ( free == 1) :
            EQUIPES.append([value,ipa,DEFAULT_LEVEL])
            print (EQUIPES)
            txt = "Vous êtes enregistrés en tant qu'équipe {Teamname} : {ipaddress}!".format(Teamname=value,ipaddress=request.remote_addr)
        else : txt = "Vous avez déjà un nom d'équipe !"
                      
        return txt
    

    @callback(
            Output("Team Ip address","children"),
            Input("refresh-interval", "n_intervals")
        )
    def get_ip (n_intervals) :
        global ST_TIMER
        
        if (len(EQUIPES)==0):
            return 'IP'
        else :
            for i in range(len(EQUIPES)) :
                time.sleep(random.randint(0,1))
                ipa = request.remote_addr
                if ( ipa == EQUIPES[i][1]): 
                    # print(EQUIPES[i])
                    ST_TIMER = True
                    return "TeamName : {teamname}  |  Level : {level}↗️ ".format(teamname=str(EQUIPES[i][0]),level=str(EQUIPES[i][2]))
                else : None


    @callback(
            Output("timer","children"),
            Input("refresh-interval", "n_intervals")
        )
    def get_ip (n_intervals) :
        global T
        if (ST_TIMER == True ) :
            T = T+1
        else : 
            None 
        return T
        
                
    return app


if __name__ == '__main__':
  Deadly_waves().run_server(host=hots, debug=True)
    # Deadly_waves().run_server(debug=True)
