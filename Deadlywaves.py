from dash import Dash as d, html, dash, dash_table, dcc, callback, Output, Input,State,ctx
import dash,json, logging, time, os, pandas as pd, plotly.graph_objects as go,random
from PIL import Image
from flask import request

EQUIPES = []
DEFAULT_LEVEL = 0
img_src= 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmZlerAavnOiz98igv9owprofau87uNoWPxrLL3OwJUQ&s'  
game_src= ''  
pil_img = Image.open("webimg.png")

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
external_stylesheet = ['https://codepen.io/chiriddyp/pen/bWLwgP.css']

colors = {'background': '#ffffff',
          'bg_home': '#666666',
          'text': '#ffa500',
          'background_plot': '#cccccc',
          'text_plot': '#000000'}



def Deadly_waves():

    app = d(__name__,use_pages=True,external_stylesheets = external_stylesheet)

    app.layout = html.Div(
        
        # style={
        # #         'background-image': 'url(img_src)',
        # #         'background-repeat': 'no-repeat',
        # #         'background-position': 'right top',
        # #         'background-size': '150px 100px'
        #     },
        
        # 'background-image': 'url("/assets/wallpaper.jpg")', 
        #                      'background-size': 'cover', 'background-repeat': 'no-repeat',
        #                      'background-position': 'center', 'height': '100vh'},
    
        [
        


            html.Div([html.Img(id='cachan_image',
                              src=img_src,style={
                                                  'width':'100px',
                                                  'height':'auto',
                                                  'padding-top': '0px',
                                                  'padding-left' :'0px'
                                                  
            })
    
            ]),
            
            html.H1(id='Title',
                    children=' BEWARE.. the Deadly waves are coming  :',
                    style={
                        'textAlign' : 'center',
                        'color': '#316171ad',
                        'font-family':"'Courier New', monospace"
                    }),
            
            html.Div([
                
                dcc.Link(page['name']+"  |  ",href=page['path'])
                for page in dash.page_registry.values()
            ]),
            
            html.Hr(),
            
            dash.page_container,
          
            
            dcc.Interval(id="refresh-interval", interval=500),# disabled=False),
            html.Div(id='Team Ip address',children='IP',style={
                
                'display':'block',
                'padding-top': '150px',
                'padding-left' :'0px'
                
            }),
            
            
    ])
    
    # @callback(        
    #         Output("refresh-interval","interval"),
    #         [Input("frequences","value")]    
    # )
    # def set_speed (value) :
    #     return value
    
    @callback(
            Output(component_id='Start Text', component_property='children'),
            # Input("refresh-interval", "n_intervals"),
            Input("submit-val","n_clicks"),
            State('input-on-submit', 'value'),
            prevent_initial_call=True  

        )
    def rien (n_clicks,value) :
        # global EQUIPES
        
        # EQUIPES.append([value,request.remote_addr,0])
        # print (EQUIPES)
        # txt = "Vous êtes enregistrés en tant qu'équipe {Teamname} : {ipaddress}!".format(Teamname=value,ipaddress=request.remote_addr)
        # return txt
        global EQUIPES
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
       
        
        if (len(EQUIPES)==0):
            return 'IP'
        else :
            for i in range(len(EQUIPES)) :
                time.sleep(random.randint(0,1))
                ipa = request.remote_addr
                if ( ipa == EQUIPES[i][1]): 
                    # print(EQUIPES[i])
                    return "TeamName : {teamname}  |  Level : {level}↗️ ".format(teamname=str(EQUIPES[i][0]),level=str(EQUIPES[i][2]))
                else : None
        
        



    return app


if __name__ == '__main__':
  Deadly_waves().run_server(host="192.168.137.1", debug=True)


