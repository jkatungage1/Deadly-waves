from dash import Dash as d, html, dash, dash_table, dcc, callback, Output, Input,State,ctx
import dash,json, logging, time, os, pandas as pd, plotly.graph_objects as go
from PIL import Image


img_src= 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmZlerAavnOiz98igv9owprofau87uNoWPxrLL3OwJUQ&s'  
game_src= ''  
pil_img = Image.open("webimg.png")

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
external_stylesheet = ['https://codepen.io/chiriddyp/pen/bWLwgP.css']

# ANG_DIST_TABLE = get_table()


def Deadly_waves():

    app = d(__name__,use_pages=False)

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
    
        children=[
        


            html.Div([html.Img(id='cachan_image',
                              src=img_src,style={
                                                  'width':'100px',
                                                  'height':'auto',
                                                  'padding-top': '0px',
                                                  'padding-left' :'0px'
                                                  
            }),
                     html.Img(id='GAME IMAGE',
                              src=img_src,style={
                                                  'width':'100px',
                                                  'height':'auto',
                                                  'padding-top': '0px',
                                                  'padding-right' :'120px'
                                                  
            })
                     
        ]),
            
            html.H1(id='Title',
                    children=' Deadly waves Main page :',
                    style={
                        'textAlign' : 'center',
                        'color': 'blue',
                        'font-family':'monospace'
                    }),
            
            html.Div([
                
                dcc.Link(page['name']+"  |  ",href=page['path'])
                for page in dash.page_registry.values()
            ]),
            
            html.Hr(),
            
            dash.page_container,
            
            dcc.Interval(id="refresh-interval", disabled=False, interval=100)
            
            
    ])


    # @callback(
    #         Output(component_id='container-button-basic', component_property='children'),
    #         # Input("refresh-interval", "n_intervals"),
    #         Input("submit-val","n_clicks"),
    #         State('input-on-submit', 'value'),
    #         prevent_initial_call=True  
    #     )
    # def rien (n_clicks,value) :
        
    #     essais = 3 - n_clicks
    #     txt = "T'as cliqué 😉"+str(n_clicks)+" fois Il te reste : "+str(essais)+" essais !" 
    #     print(n_clicks,value) 
    #     if ( essais == 0) :
    #         if (value == 'Jacques') : 
    #             txt = " Gagné !!"
    #         else :
    #             txt = "PERDU !!"
        
    #     return txt
      


    return app


if __name__ == '__main__':
  Deadly_waves().run_server(host="0.0.0.0", debug=True)


