import dash
from dash import html, ctx
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import random
from dash import dcc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

PlayerBack_style = {'background-image': 'url(assets/PlayerBack.jpg',
                'background-repeat': 'no-repeat',
                'border-radius': '25px',
                'border': '2px solid black', 
                'margin-left': '90px',
                'margin-top': '12px',
                'height':'275px',
                'width': '200px'}


Shoot_style = {'background-image': 'url(assets/Shoot.jpg',
                'background-repeat': 'no-repeat',
                'border-radius': '25px',
                'border': '2px solid black', 
                'margin-left': '90px',
                'margin-top': '12px',
                'height':'275px',
                'width': '200px'}



Save_style = {'background-image': 'url(assets/Save.jpg',
                'background-repeat': 'no-repeat',
                'border-radius': '25px',
                'border': '2px solid black', 
                'margin-left': '90px',
                'margin-top': '12px',
                'height':'275px',
                'width': '200px'}


Player1_style = {'background-image': 'url(assets/Player1.jpg',
                 'background-repeat': 'no-repeat',
                 'border-radius': '25px',
                 'border': '2px solid black', 
                'margin-left': '90px',
                'margin-top': '12px',
                'height':'275px',
                'width': '200px'}


Player2_style = {'background-image': 'url(assets/Player2.jpg',
                 'background-repeat': 'no-repeat',
                 'border-radius': '25px',
                 'border': '2px solid black', 
                'margin-left': '90px',
                'margin-top': '12px',
                'height':'275px',
                'width': '200px'}


Player3_style = {'background-image': 'url(assets/Player3.jpg',
                 'background-repeat': 'no-repeat',
                 'border-radius': '25px',
                'border': '2px solid black', 
                'margin-left': '90px',
                'margin-top': '12px',
                'height':'275px',
                'width': '200px'}


Player4_style = {'background-image': 'url(assets/Player4.jpg',
                 'background-repeat': 'no-repeat',
                 'border-radius': '25px',
                 'border': '2px solid black', 
                'margin-left': '90px',
                'margin-top': '12px',
                'height':'275px',
                'width': '200px'}


Player5_style = {'background-image': 'url(assets/Player5.jpg',
                 'background-repeat': 'no-repeat',
                 'border-radius': '25px',
                 'border': '2px solid black', 
                'margin-left': '90px',
                'margin-top': '12px',
                'height':'275px',
                'width': '200px'}


Player6_style = {'background-image': 'url(assets/Player6.jpg',
                 'background-repeat': 'no-repeat',
                 'border-radius': '25px',
                 'border': '2px solid black', 
                'margin-left': '90px',
                'margin-top': '12px',
                'height':'275px',
                'width': '200px'}



rightGreen_style = {'background-image': 'url(assets/rightGreen.jpg',
                 'background-repeat': 'no-repeat',
                 'border-radius': '25px',
                 'border': '2px solid black', 
                'margin-left': '90px',
                'margin-top': '12px',
                'height':'275px',
                'width': '200px'}


rightYellow_style = {'background-image': 'url(assets/rightYellow.jpg',
                 'background-repeat': 'no-repeat',
                 'border-radius': '25px',
                 'border': '2px solid black', 
                'margin-left': '90px',
                'margin-top': '12px',
                'height':'275px',
                'width': '200px'}




Player7_style = {'background-image': 'url(assets/Player7.jpg',
                 'background-repeat': 'no-repeat',
                 'border': '2px solid black', 
                 'border-radius': '25px',
                'margin-left': '90px',
                'margin-top': '12px',
                'height':'275px',
                'width': '200px'}


leftGreen_style = {'background-image': 'url(assets/leftGreen.jpg',
                 'background-repeat': 'no-repeat',
                 'border': '2px solid black', 
                 'border-radius': '25px',
                'margin-left': '90px',
                'margin-top': '12px',
                'height':'275px',
                'width': '200px'}


leftYellow_style = {'background-image': 'url(assets/leftYellow.jpg',
                 'background-repeat': 'no-repeat',
                 'border': '2px solid black', 
                 'border-radius': '25px',
                'margin-left': '90px',
                'margin-top': '12px',
                'height':'275px',
                'width': '200px'}


Player8_style = {'background-image': 'url(assets/Player8.jpg',
                 'background-repeat': 'no-repeat',
                 'border-radius': '25px',
                 'border': '2px solid black', 
                'margin-left': '90px',
                'margin-top': '12px',
                'height':'275px',
                'width': '200px'}


middleGreen_style = {'background-image': 'url(assets/middleGreen.jpg',
                 'background-repeat': 'no-repeat',
                 'border-radius': '25px',
                 'border': '2px solid black', 
                'margin-left': '90px',
                'margin-top': '12px',
                'height':'275px',
                'width': '200px'}


middleYellow_style = {'background-image': 'url(assets/middleYellow.jpg',
                 'background-repeat': 'no-repeat',
                 'border-radius': '25px',
                 'border': '2px solid black', 
                'margin-left': '90px',
                'margin-top': '12px',
                'height':'275px',
                'width': '200px'}


Player9_style = {'background-image': 'url(assets/Player9.jpg',
                 'background-repeat': 'no-repeat',
                 'border-radius': '25px',
                 'border': '2px solid black', 
                'margin-left': '90px',
                'margin-top': '12px',
                'height':'275px',
                'width': '200px'}


Player10_style = {'background-image': 'url(assets/Player10.jpg',
                 'background-repeat': 'no-repeat',
                 'border-radius': '25px',
                 'border': '2px solid black', 
                'margin-left': '90px',
                'margin-top': '12px',
                'height':'275px',
                'width': '200px'}


Player11_style = {'background-image': 'url(assets/Player11.jpg',
                 'background-repeat': 'no-repeat',
                 'border-radius': '25px',
                 'border': '2px solid black', 
                'margin-left': '90px',
                'margin-top': '12px',
                'height':'275px',
                'width': '200px'}


PlayerBack_styleBlue = {'background-image': 'url(assets/PlayerBackBlue.jpg',
                'background-repeat': 'no-repeat',
                'border-radius': '25px',
                'border': '2px solid black', 
                'margin-left': '125px',
                'margin-top': '12px',
                'height':'275px',
                'width': '200px'}


Player1_styleBlue = {'background-image': 'url(assets/Player1Blue.jpg',
                'background-repeat': 'no-repeat',
                'border-radius': '25px',
                'border': '2px solid black', 
                'margin-left': '125px',
                'margin-top': '12px',
                'height':'275px',
                'width': '200px'}


Player2_styleBlue = {'background-image': 'url(assets/Player2Blue.jpg',
                'background-repeat': 'no-repeat',
                'border-radius': '25px',
                'border': '2px solid black', 
                'margin-left': '125px',
                'margin-top': '12px',
                'height':'275px',
                'width': '200px'}


Player3_styleBlue = {'background-image': 'url(assets/Player3Blue.jpg',
                'background-repeat': 'no-repeat',
                'border-radius': '25px',
                'border': '2px solid black', 
                'margin-left': '125px',
                'margin-top': '12px',
                'height':'275px',
                'width': '200px'}


Player4_styleBlue = {'background-image': 'url(assets/Player4Blue.jpg',
                'background-repeat': 'no-repeat',
                'border-radius': '25px',
                'border': '2px solid black', 
                'margin-left': '125px',
                'margin-top': '12px',
                'height':'275px',
                'width': '200px'}


Player5_styleBlue = {'background-image': 'url(assets/Player5Blue.jpg',
                'background-repeat': 'no-repeat',
                'border-radius': '25px',
                'margin-left': '125px',
                'border': '2px solid black', 
                'margin-top': '12px',
                'height':'275px',
                'width': '200px'}


Player6_styleBlue = {'background-image': 'url(assets/Player6Blue.jpg',
                'background-repeat': 'no-repeat',
                'border-radius': '25px',
                'border': '2px solid black', 
                'margin-left': '125px',
                'margin-top': '12px',
                'height':'275px',
                'width': '200px'}


Player7_styleBlue = {'background-image': 'url(assets/Player7Blue.jpg',
                'background-repeat': 'no-repeat',
                'border-radius': '25px',
                'border': '2px solid black', 
                'margin-left': '125px',
                'margin-top': '12px',
                'height':'275px',
                'width': '200px'}


Player8_styleBlue = {'background-image': 'url(assets/Player8Blue.jpg',
                'background-repeat': 'no-repeat',
                'border-radius': '25px',
                'border': '2px solid black', 
                'margin-left': '125px',
                'margin-top': '12px',
                'height':'275px',
                'width': '200px'}


Player9_styleBlue = {'background-image': 'url(assets/Player9Blue.jpg',
                'background-repeat': 'no-repeat',
                'border-radius': '25px',
                'border': '2px solid black', 
                'margin-left': '125px',
                'margin-top': '12px',
                'height':'275px',
                'width': '200px'}


Player10_styleBlue = {'background-image': 'url(assets/Player10Blue.jpg',
                'background-repeat': 'no-repeat',
                'border-radius': '25px',
                'border': '2px solid black', 
                'margin-left': '125px',
                'margin-top': '12px',
                'height':'275px',
                'width': '200px'}


Player11_styleBlue = {'background-image': 'url(assets/Player11Blue.jpg',
                'background-repeat': 'no-repeat',
                'border-radius': '25px',
                'border': '2px solid black', 
                'margin-left': '125px',
                'margin-top': '12px',
                'height':'275px',
                'width': '200px'}


green_button_style1 = {'background-color': 'lightgreen',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'grey',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '35px',
                      'margin-left': '185px'}


green_button_style1High = {'background-color': 'purple',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '35px',
                      'margin-left': '185px'}


red_button_style2 = {'background-color': 'red',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '45px',
                      'margin-left': '35px'}


red_button_style2High = {'background-color': 'orange',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '45px',
                      'margin-left': '35px'}



red_button_style3 = {'background-color': 'red',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '45px',
                      'margin-left': '35px'}


red_button_style3High = {'background-color': 'orange',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '45px',
                      'margin-left': '35px'}




red_button_style4 = {'background-color': 'red',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '45px',
                      'margin-left': '35px'}

red_button_style4High = {'background-color': 'orange',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '45px',
                      'margin-left': '35px'}

red_button_style5 = {'background-color': 'red',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '45px',
                      'margin-left': '35px'}

red_button_style5High = {'background-color': 'orange',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '45px',
                      'margin-left': '35px'}


red_button_style6 = {'background-color': 'red',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '75px',
                      'margin-left': '35px'}


red_button_style6High = {'background-color': 'orange',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '75px',
                      'margin-left': '35px'}

shoot_button_style6 = {'background-color': 'green',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '75px',
                      'margin-left': '35px'}


shoot_button_style6High = {'background-color': 'yellow',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '75px',
                      'margin-left': '35px'}

red_button_style7 = {'background-color': 'red',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '75px',
                      'margin-left': '90px'}


red_button_style7High = {'background-color': 'orange',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '75px',
                      'margin-left': '90px'}

shoot_button_style7 = {'background-color': 'green',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '75px',
                      'margin-left': '90px'}


shoot_button_style7High = {'background-color': 'yellow',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '75px',
                      'margin-left': '90px'}

red_button_style8 = {'background-color': 'red',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '75px',
                      'margin-left': '30px'}


red_button_style8High = {'background-color': 'orange',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '75px',
                      'margin-left': '30px'}

shoot_button_style8 = {'background-color': 'green',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '75px',
                      'margin-left': '30px'}


shoot_button_style8High = {'background-color': 'yellow',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '75px',
                      'margin-left': '30px'}

red_button_style9 = {'background-color': 'red',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '25px',
                      'margin-left': '90px'}


red_button_style9High = {'background-color': 'orange',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '25px',
                      'margin-left': '90px'}


red_button_style10 = {'background-color': 'red',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '55px',
                      'margin-left': '190px'}

red_button_style10High = {'background-color': 'orange',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '55px',
                      'margin-left': '190px'}


red_button_style11 = {'background-color': 'red',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '25px',
                      'margin-left': '135px'}

red_button_style11High = {'background-color': 'orange',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '25px',
                      'margin-left': '135px'}




hide_button_style1 = {'background-color': 'lightgreen',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'grey',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '45px',
                      'margin-left': '210px',
                      'opacity': '0',
                      }

hide_button_style2 = {'background-color': 'red',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '45px',
                      'margin-left': '50px',
                      'opacity': '0',
                      }



hide_button_style3 = {'background-color': 'red',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '45px',
                      'margin-left': '35px',
                      'opacity': '0',
                      }

hide_button_style4 = {'background-color': 'red',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '45px',
                      'margin-left': '35px',
                      'opacity': '0',
                      }

hide_button_style5 = {'background-color': 'red',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '45px',
                      'margin-left': '35px',
                      'opacity': '0',
                      }


hide_button_style6 = {'background-color': 'red',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '75px',
                      'margin-left': '35px',
                      'opacity': '0',
                      }


hide_button_style7 = {'background-color': 'red',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '75px',
                      'margin-left': '100px',
                      'opacity': '0',
                      }


hide_button_style8 = {'background-color': 'red',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '75px',
                      'margin-left': '40px',
                      'opacity': '0',
                      }


hide_button_style9 = {'background-color': 'red',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '25px',
                      'margin-left': '100px',
                      'opacity': '0',
                      }


hide_button_style10 = {'background-color': 'red',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '65px',
                      'margin-left': '210px',
                      'opacity': '0',
                      }


hide_button_style11 = {'background-color': 'red',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '25px',
                      'margin-left': '150px',
                      'opacity': '0',
                      }



yellow_button_style1 = {'background-color': 'yellow',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'grey',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '35px',
                      'margin-left': '185px'}

yellow_button_style1High = {'background-color': 'teal',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '35px',
                      'margin-left': '185px'}


blue_button_style2 = {'background-color': 'lightblue',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '45px',
                      'margin-left': '35px'}



blue_button_style2High = {'background-color': 'pink',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '45px',
                      'margin-left': '35px'}



blue_button_style3 = {'background-color': 'lightblue',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '45px',
                      'margin-left': '35px'}


blue_button_style3High = {'background-color': 'pink',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '45px',
                      'margin-left': '35px'}



blue_button_style4 = {'background-color': 'lightblue',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '45px',
                      'margin-left': '35px'}



blue_button_style4High = {'background-color': 'pink',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '45px',
                      'margin-left': '35px'}

blue_button_style5 = {'background-color': 'lightblue',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '45px',
                      'margin-left': '35px'}


blue_button_style5High = {'background-color': 'pink',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '45px',
                      'margin-left': '35px'}


blue_button_style6 = {'background-color': 'lightblue',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '75px',
                      'margin-left': '35px'}


blue_button_style6High = {'background-color': 'pink',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '75px',
                      'margin-left': '35px'}

save_button_style6 = {'background-color': 'yellow',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '75px',
                      'margin-left': '35px'}


save_button_style6High = {'background-color': 'green',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '75px',
                      'margin-left': '35px'}

blue_button_style7 = {'background-color': 'lightblue',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '75px',
                      'margin-left': '90px'}


blue_button_style7High = {'background-color': 'pink',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '75px',
                      'margin-left': '90px'}

save_button_style7 = {'background-color': 'yellow',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '75px',
                      'margin-left': '90px'}


save_button_style7High = {'background-color': 'green',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '75px',
                      'margin-left': '90px'}


blue_button_style8 = {'background-color': 'lightblue',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '75px',
                      'margin-left': '30px'}

blue_button_style8High = {'background-color': 'pink',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '75px',
                      'margin-left': '30px'}

save_button_style8 = {'background-color': 'yellow',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '75px',
                      'margin-left': '30px'}

save_button_style8High = {'background-color': 'green',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '75px',
                      'margin-left': '30px'}


blue_button_style9 = {'background-color': 'lightblue',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '25px',
                      'margin-left': '90px'}


blue_button_style9High = {'background-color': 'pink',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '25px',
                      'margin-left': '90px'}


blue_button_style10 = {'background-color': 'lightblue',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '55px',
                      'margin-left': '190px'}


blue_button_style10High = {'background-color': 'pink',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '55px',
                      'margin-left': '190px'}


blue_button_style11 = {'background-color': 'lightblue',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '25px',
                      'margin-left': '135px'}

blue_button_style11High = {'background-color': 'pink',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '25px',
                      'margin-left': '135px'}



hide_button_style1blue = {'background-color': 'yellow',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'grey',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '45px',
                      'margin-left': '210px',
                      'opacity': '0',
                      }

hide_button_style2blue = {'background-color': 'lightblue',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '45px',
                      'margin-left': '50px',
                      'opacity': '0',
                      }



hide_button_style3blue = {'background-color': 'lightblue',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '45px',
                      'margin-left': '35px',
                      'opacity': '0',
                      }

hide_button_style4blue = {'background-color': 'lightblue',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '45px',
                      'margin-left': '35px',
                      'opacity': '0',
                      }

hide_button_style5blue = {'background-color': 'lightblue',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '45px',
                      'margin-left': '35px',
                      'opacity': '0',
                      }


hide_button_style6blue = {'background-color': 'lightblue',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '75px',
                      'margin-left': '35px',
                      'opacity': '0',
                      }


hide_button_style7blue = {'background-color': 'lightblue',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '75px',
                      'margin-left': '100px',
                      'opacity': '0',
                      }


hide_button_style8blue = {'background-color': 'lightblue',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '75px',
                      'margin-left': '40px',
                      'opacity': '0',
                      }


hide_button_style9blue = {'background-color': 'lightblue',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '25px',
                      'margin-left': '100px',
                      'opacity': '0',
                      }


hide_button_style10blue = {'background-color': 'lightblue',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '65px',
                      'margin-left': '210px',
                      'opacity': '0',
                      }


hide_button_style11blue = {'background-color': 'lightblue',
                      'border-radius': '50px',
                      'fontSize': '30px',
                      'color': 'white',
                      'height': '65px',
                      'width': '65px',
                      'margin-top': '25px',
                      'margin-left': '150px',
                      'opacity': '0',
                      }



hide_button_display = {'display': 'none'}




rebelPhaseDefense = {'background-image': 'url(assets/Defense.jpg)',
                          'background-repeat': 'no-repeat',
                          'background-size':'250px 310px',
                          'border': '2px solid black', 
                          'border-radius': '50px',
                          'background-color': 'GhostWhite',
                          'margin-right': '0px', 'margin-left': '0px',
                          'margin-top': '30px', 'height': '310px', 'width': '500px'}



rebelPhaseAttack = {'background-image': 'url(assets/Attack.jpg)',
                          'background-repeat': 'no-repeat',
                          'background-size':'250px 310px',
                          'border': '2px solid black', 
                          'border-radius': '50px',
                          'background-color': 'GhostWhite',
                          'margin-right': '0px', 'margin-left': '0px',
                          'margin-top': '30px', 'height': '310px', 'width': '500px'}


dragonPhaseAttack = style={'background-image': 'url(assets/Attack.jpg)',
                          'background-repeat': 'no-repeat',
                          'background-size':'250px 310px',
                          'border': '2px solid black', 
                          'border-radius': '50px',
                          'background-color': 'GhostWhite',
                          'margin-right': '20px', 'margin-left': '50px',
                          'margin-top': '30px', 'height': '310px', 'width': '500px'}


dragonPhaseDefense = style={'background-image': 'url(assets/Defense.jpg)',
                          'background-repeat': 'no-repeat',
                          'background-size':'250px 310px',
                          'border': '2px solid black', 
                          'border-radius': '50px',
                          'background-color': 'GhostWhite',
                          'margin-right': '20px', 'margin-left': '50px',
                          'margin-top': '30px', 'height': '310px', 'width': '500px'}



match_style = {'border': '2px solid black', 
               'border-radius': '20px',
               'background-color': 'Crimson',
               'margin-right': '0px', 
               'margin-left': '25px',
               'margin-top': '20px', 
               'height': '60px', 
               'width': '500px'}

shoot_style = {'border': '2px solid black', 
               'border-radius': '20px',
               'background-color': 'DarkOrange',
               'margin-right': '0px', 
               'margin-left': '25px',
               'margin-top': '20px', 
               'height': '60px', 
               'width': '500px'}

save_style = {'border': '2px solid black', 
               'border-radius': '20px',
               'background-color': 'DarkSlateBlue',
               'margin-right': '0px', 
               'margin-left': '25px',
               'margin-top': '20px', 
               'height': '60px', 
               'width': '500px'}

safe_style = {'border': '2px solid black', 
               'border-radius': '20px',
               'background-color': 'DarkCyan',
               'margin-right': '0px', 
               'margin-left': '25px',
               'margin-top': '20px', 
               'height': '60px', 
               'width': '500px'}

saved_style = {'border': '2px solid black', 
               'border-radius': '20px',
               'background-color': 'DarkMagenta',
               'margin-right': '0px', 
               'margin-left': '25px',
               'margin-top': '20px', 
               'height': '60px', 
               'width': '500px'}

scored_style = {'border': '2px solid black', 
               'border-radius': '20px',
               'background-color': 'MediumSeaGreen',
               'margin-right': '0px', 
               'margin-left': '25px',
               'margin-top': '20px', 
               'height': '60px', 
               'width': '500px'}




phase = 1  ## -> attack
## phase = 0 -> defend
## phase = 3 -> shoot
## phase = 4 -> save
FullListBlue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


score1 = 0
pass1 = 0
score2 = 0
pass2 = 0


app.layout = html.Div([
    
    dbc.Row([
        
        dbc.Col([
            dbc.Row([
                
                
                html.Div([
                html.H1('Dragons', style={'text-align': 'center', 'color': 'white', 'fontSize': 40, 'marginBottom': 20, 'marginTop': 0}),
                ], style={'border': '2px solid black',
                          'border-radius': '20px',
                          'background-color': 'darkred',
                          'margin-right': '20px', 'margin-left': '50px',
                          'margin-top': '20px', 'height': '60px', 'width': '500px'}),

                html.Div([
                html.H1(id="outputold"),
                html.H3('Score', style={'text-align': 'right', 'color': 'purple', 'fontSize': 55, 
                                                'marginRight': 60, 
                                                'marginTop': 1}),
                
                html.H3(id='player1Score', style={'text-align': 'right', 'color': 'orange', 'fontSize': 55, 
                                                'marginRight': 120, 
                                                'marginTop': 1}),
                
                html.H3('Pass', style={'text-align': 'right', 'color': 'purple', 'fontSize': 55, 
                                                'marginRight': 70, 
                                                'marginTop': 1}),
                

                html.H3(id='player1Pass', style={'text-align': 'right', 'color': 'orange', 'fontSize': 55, 
                                                'marginRight': 120, 
                                                'marginTop': 1}),

                
                ], id='dragonPhase', style=dragonPhaseAttack),
 
                html.Div([
                html.H1(id="output", style=PlayerBack_style),
                ], style={'border': '2px solid black', 
                          'border-radius': '50px',
                          'background-color': 'GhostWhite',
                          'margin-right': '20px', 'margin-left': '50px',
                          'margin-top': '20px', 'height': '310px', 'width': '500px'}),
                
                
                html.Div([
                html.H1(id="PlayerSelection", style={'text-align': 'left', 'color': 'white', 'fontSize': 40, 
                                                'marginLeft': 180, 
                                                'margin-bottom': '100px'}), 
                ], style={'border': '2px solid black', 
                          'border-radius': '20px',
                          'background-color': 'darkred',
                          'margin-right': '0px', 'margin-left': '50px',
                          'margin-top': '20px', 'height': '60px', 'width': '500px'}),
        ]),
        ], width=4),

        dbc.Col([
            dbc.Row([
                
                html.Div([
                html.H1('Soccer-Go!', style={'text-align': 'center', 'color': 'White', 'fontSize': 40, 'marginLeft': 20, 'marginBottom': 20, 'marginTop': 0}),
                ], style={'border': '2px solid black', 
                          'border-radius': '20px',
                          'background-color': 'GoldenRod',
                          'margin-right': '0px', 'margin-left': '25px',
                          'margin-top': '20px', 'height': '60px', 'width': '500px'}),

                html.Div(
                [

                    html.Div(
                    [
                        dbc.Button(id='button1',
                            children=['1'],
                            n_clicks=0,
                            style=green_button_style1,
                    ), 
                        dbc.Popover(target="button1", trigger="hover", id="popover1", className="d-none"),
                        
                        
                        dbc.Button(id='button1blue',
                            children=['1'],
                            n_clicks=0,
                            style=yellow_button_style1,
                    ), 
                        dbc.Popover(target="button1blue", trigger="hover", id="popover1blue", className="d-none")
                        
                    ]),
                    
                    html.Div([
                        dbc.Button(id='button2',
                            children=['2'],
                            n_clicks=0,
                            style=red_button_style2,
                    ),
                        
                        dbc.Popover(target="button2", trigger="hover", id="popover2", className="d-none"),
                    
                        dbc.Button(id='button4',
                            children=['4'],
                            n_clicks=0,
                            style=red_button_style4,
                    ),
                        dbc.Popover(target="button4", trigger="hover", id="popover4", className="d-none"),
                    
                        dbc.Button(id='button5',
                            children=['5'],
                            n_clicks=0,
                            style=red_button_style5,
                    ),
                        
                        dbc.Popover(target="button5", trigger="hover", id="popover5", className="d-none"),
                            
                        dbc.Button(id='button3',
                            children=['3'],
                            n_clicks=0,
                            style=red_button_style3,
                    ),
                        
                        dbc.Popover(target="button3", trigger="hover", id="popover3", className="d-none"),
                        
                        
                        dbc.Button(id='button2blue',
                            children=['2'],
                            n_clicks=0,
                            style=blue_button_style2,
                    ),
                        
                        dbc.Popover(target="button2blue", trigger="hover", id="popover2blue", className="d-none"),
                    
                        dbc.Button(id='button4blue',
                            children=['4'],
                            n_clicks=0,
                            style=blue_button_style4,
                    ),
                        dbc.Popover(target="button4blue", trigger="hover", id="popover4blue", className="d-none"),
                    
                        dbc.Button(id='button5blue',
                            children=['5'],
                            n_clicks=0,
                            style=blue_button_style5,
                    ),
                        
                        dbc.Popover(target="button5blue", trigger="hover", id="popover5blue", className="d-none"),
                            
                        dbc.Button(id='button3blue',
                            children=['3'],
                            n_clicks=0,
                            style=blue_button_style3,
                    ),
                        
                        dbc.Popover(target="button3blue", trigger="hover", id="popover3blue", className="d-none"),
                        
                        ]),
                    
                    
                    html.Div([
                        dbc.Button(id='button7',
                            children=['7'],
                            n_clicks=0,
                            style=red_button_style7,
                    ),
                    
                        dbc.Popover(target="button7", trigger="hover", id="popover7", className="d-none"),
                        
                        dbc.Button(id='button8',
                            children=['8'],
                            n_clicks=0,
                            style=red_button_style8,
                    ),
                        
                        dbc.Popover(target="button8", trigger="hover", id="popover8", className="d-none"),
                    
                        dbc.Button(id='button6',
                            children=['6'],
                            n_clicks=0,
                            style=red_button_style6,
                    ),
                        
                        dbc.Popover(target="button6", trigger="hover", id="popover6", className="d-none"),
                        
                        
                        dbc.Button(id='button7blue',
                            children=['7'],
                            n_clicks=0,
                            style=blue_button_style7,
                    ),
                    
                        dbc.Popover(target="button7blue", trigger="hover", id="popover7blue", className="d-none"),
                        
                        dbc.Button(id='button8blue',
                            children=['8'],
                            n_clicks=0,
                            style=blue_button_style8,
                    ),
                        
                        dbc.Popover(target="button8blue", trigger="hover", id="popover8blue", className="d-none"),
                    
                        dbc.Button(id='button6blue',
                            children=['6'],
                            n_clicks=0,
                            style=blue_button_style6,
                    ),
                        
                        dbc.Popover(target="button6blue", trigger="hover", id="popover6blue", className="d-none"),    

                        ]),
                      

                    html.Div([
                        dbc.Button(id='button10',
                            children=['10'],
                            n_clicks=0,
                            style=red_button_style10,
                    ),
                        
                        dbc.Popover(target="button10", trigger="hover", id="popover10", className="d-none"),
                        

                        dbc.Button(id='button10blue',
                            children=['10'],
                            n_clicks=0,
                            style=blue_button_style10,
                    ),
                        
                        dbc.Popover(target="button10blue", trigger="hover", id="popover10blue", className="d-none"),
                        
                    ]),
                    
                    
                    html.Div([
                        dbc.Button(id='button9',
                            children=['9'],
                            n_clicks=0,
                            style=red_button_style9,
                    ),
                        
                        dbc.Popover(target="button9", trigger="hover", id="popover9", className="d-none"),
                    
                        dbc.Button(id='button11',
                            children=['11'],
                            n_clicks=0,
                            style=red_button_style11,
                    ),
                        dbc.Popover(target="button11", trigger="hover", id="popover11", className="d-none"),
                        
                        
                        
                        dbc.Button(id='button9blue',
                            children=['9'],
                            n_clicks=0,
                            style=blue_button_style9,
                    ),
                        
                        dbc.Popover(target="button9blue", trigger="hover", id="popover9blue", className="d-none"),
                    
                        dbc.Button(id='button11blue',
                            children=['11'],
                            n_clicks=0,
                            style=blue_button_style11,
                    ),
                        dbc.Popover(target="button11blue", trigger="hover", id="popover11blue", className="d-none"),
                        
                        ]),

                    dcc.Store(id='intermediate-value'),

                    dcc.Store(id='test'),
                    
                    dcc.Store(id='elementPhase')
                                        
                ], style={'background-image': 'url(assets/verticalPitch90.png)',
                        'background-repeat': 'no-repeat',
                        'height':'650px',
                        'width': '470px',
                        'margin-left': '50px',
                        'margin-right': '0px',
                        'margin-top': '20px'
                        }),
                
                
                html.Div([
                html.H1('Match', id='GameCheck', style={'text-align': 'center', 'color': 'White', 'fontSize': 40, 'marginBottom': 5, 'marginTop': 0}),
                ], id='barStyle', style=match_style),   
            ])
        ], width=4),
        
        
        dbc.Col([
            dbc.Row([

                html.Div([
                html.H1('Rebels', style={'text-align': 'center', 'color': 'white', 'fontSize': 40, 'marginBottom': 30, 'marginTop': 0}),
                ], style={'border': '2px solid black', 
                          'border-radius': '20px',
                          'background-color': 'darkblue',
                          'margin-right': '0px', 'margin-left': '0px',
                          'margin-top': '20px', 'height': '60px', 'width': '500px'}),

                html.Div([
                
                html.H1(id="output3"),
                
                html.H3('Score', style={'text-align': 'right', 'color': 'purple', 'fontSize': 55, 
                                                  'marginRight': 60,
                                                'marginTop': 1}),
                html.H3(id='player2Score', style={'text-align': 'right', 'color': 'orange', 'fontSize': 55,
                                                'marginRight': 120,
                                                'marginTop': 1}),
                
                html.H3('Pass', style={'text-align': 'right', 'color': 'purple', 'fontSize': 55,
                                                'marginRight': 70, 
                                                'marginTop': 1}),
                
                html.H3(id='player2Pass', style={'text-align': 'right', 'color': 'orange', 'fontSize': 55,
                                                 'marginRight': 120,
                                                'marginTop': 1}),

                
                ], id='rebelPhase', style=rebelPhaseDefense),

                html.Div([
                html.H1(id="output1", style=PlayerBack_styleBlue),
                html.Div(id="SelectionBlue", style={'text-align': 'left', 'color': 'purple', 'fontSize': 20, 
                                                'marginLeft': 120, 
                                                'marginTop': 10}),
                ], style={'border': '2px solid black', 
                         'border-radius': '50px',
                          'background-color': 'GhostWhite',
                          'margin-right': '0px', 'margin-left': '0px',
                          'margin-top': '20px', 'height': '310px', 'width': '500px'}),
                
                
                
                
                html.Div([
                html.H1(id="ComputerSelection", style={'text-align': 'left', 'color': 'white', 'fontSize': 40, 
                                                'marginLeft': 200, 
                                                'marginBottom': 100}),
                ], style={'border': '2px solid black', 
                          'border-radius': '20px',
                          'background-color': 'darkblue',
                          'margin-right': '0px', 'margin-left': '0px',
                          'margin-top': '20px', 'height': '60px', 'width': '500px'}),
        ]),
        ], width=4),

    ], id='refresh')

])



@app.callback(Output('rebelPhase', 'style'), [Input('elementPhase', 'data')])
def rebelLayout(data):
    
    global phase
    
    if((phase==1) or (phase==3)):
        return rebelPhaseDefense
    elif((phase==0) or (phase==4)):
        return rebelPhaseAttack
    else:
        return rebelPhaseDefense
    
    
@app.callback(Output('dragonPhase', 'style'), [Input('elementPhase', 'data')])
def dragonLayout(data):
    
    global phase
    
    if((phase==1) or (phase==3)):
        return dragonPhaseAttack
    elif((phase==0) or (phase==4)):
        return dragonPhaseDefense
    else:
        return dragonPhaseAttack



@app.callback(
    Output('intermediate-value', 'data'),
    [Input('button1', 'n_clicks'), Input('button2', 'n_clicks'), Input('button3', 'n_clicks'), Input('button4', 'n_clicks'), Input('button5', 'n_clicks'), Input('button6', 'n_clicks'),
     Input('button7', 'n_clicks'), Input('button8', 'n_clicks'), Input('button9', 'n_clicks'),Input('button10', 'n_clicks'),Input('button11', 'n_clicks'),
     
     Input('button1blue', 'n_clicks'), Input('button2blue', 'n_clicks'), Input('button3blue', 'n_clicks'), Input('button4blue', 'n_clicks'), Input('button5blue', 'n_clicks'), Input('button6blue', 'n_clicks'),
     Input('button7blue', 'n_clicks'), Input('button8blue', 'n_clicks'), Input('button9blue', 'n_clicks'),Input('button10blue', 'n_clicks'),Input('button11blue', 'n_clicks'),
     
     Input('test', 'data')
     
     ]
)
def set_output222(n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11,
                n_clicks12, n_clicks22, n_clicks32, n_clicks42, n_clicks52, n_clicks62, n_clicks72, n_clicks82, n_clicks92, n_clicks102, n_clicks112,
                test):
    
    global phase

    button_id = ctx.triggered_id
    
    if((phase==1) or (phase==0)):
        
        if((test=='R') or (test=='L') or (test=='M')):
            
            if((button_id == 'button6') or (button_id == 'button6blue')):
                return 'R'
            elif((button_id == 'button7') or (button_id == 'button7blue')):
                return 'L'
            elif((button_id == 'button8') or (button_id == 'button8blue')):
                return 'M'

        else:    
            if((button_id == 'button1') or (button_id == 'button1blue')):
                return 1
            elif((button_id == 'button2') or (button_id == 'button2blue')):
                return 2
            elif((button_id == 'button3') or (button_id == 'button3blue')):
                return 3
            elif((button_id == 'button4') or (button_id == 'button4blue')):
                return 4
            elif((button_id == 'button5') or (button_id == 'button5blue')):
                return 5
            elif((button_id == 'button6') or (button_id == 'button6blue')):
                return 6
            elif((button_id == 'button7') or (button_id == 'button7blue')):
                return 7
            elif((button_id == 'button8') or (button_id == 'button8blue')):
                return 8
            elif((button_id == 'button9') or (button_id == 'button9blue')):
                return 9
            elif((button_id == 'button10') or (button_id == 'button10blue')):
                return 10
            elif((button_id == 'button11') or (button_id == 'button11blue')):
                return 11
            else:
                return ' '
            
    elif((phase==3) or (phase==4)):
            if((button_id == 'button6') or (button_id == 'button6blue')):
                return 'R'
            elif((button_id == 'button7') or (button_id == 'button7blue')):
                return 'L'
            elif((button_id == 'button8') or (button_id == 'button8blue')):
                return 'M'
            else:
                return ' '
        
        
    else:
        return ' '


@app.callback(
    Output('output', 'style'),
    [Input("popover1", "is_open"), Input('button1', 'n_clicks'),
     Input("popover2", "is_open"), Input('button2', 'n_clicks'),
     Input("popover3", "is_open"), Input('button3', 'n_clicks'),
     Input("popover4", "is_open"), Input('button4', 'n_clicks'),
     Input("popover5", "is_open"), Input('button5', 'n_clicks'),
     Input("popover6", "is_open"), Input('button6', 'n_clicks'),
     Input("popover7", "is_open"), Input('button7', 'n_clicks'),
     Input("popover8", "is_open"), Input('button8', 'n_clicks'),
     Input("popover9", "is_open"), Input('button9', 'n_clicks'),
     Input("popover10", "is_open"), Input('button10', 'n_clicks'),
     Input("popover11", "is_open"), Input('button11', 'n_clicks'),     
     Input("popover1blue", "is_open"), Input('button1blue', 'n_clicks'),
     Input("popover2blue", "is_open"), Input('button2blue', 'n_clicks'),
     Input("popover3blue", "is_open"), Input('button3blue', 'n_clicks'),
     Input("popover4blue", "is_open"), Input('button4blue', 'n_clicks'),
     Input("popover5blue", "is_open"), Input('button5blue', 'n_clicks'),
     Input("popover6blue", "is_open"), Input('button6blue', 'n_clicks'),
     Input("popover7blue", "is_open"), Input('button7blue', 'n_clicks'),
     Input("popover8blue", "is_open"), Input('button8blue', 'n_clicks'),
     Input("popover9blue", "is_open"), Input('button9blue', 'n_clicks'),
     Input("popover10blue", "is_open"), Input('button10blue', 'n_clicks'),
     Input("popover11blue", "is_open"), Input('button11blue', 'n_clicks')])
def set_output(is_open1, n_clicks1,
               is_open2, n_clicks2,
               is_open3, n_clicks3,
               is_open4, n_clicks4,
               is_open5, n_clicks5,
               is_open6, n_clicks6,
               is_open7, n_clicks7,
               is_open8, n_clicks8,
               is_open9, n_clicks9,
               is_open10, n_clicks10,
               is_open11, n_clicks11,
               is_open12, n_clicks12,
               is_open22, n_clicks22,
               is_open32, n_clicks32,
               is_open42, n_clicks42,
               is_open52, n_clicks52,
               is_open62, n_clicks62,
               is_open72, n_clicks72,
               is_open82, n_clicks82,
               is_open92, n_clicks92,
               is_open102, n_clicks102,
               is_open112, n_clicks112):
    
    if(phase==1 or phase==0):   
    
        if ((is_open1==True and (n_clicks1==0)) or (is_open12==True and (n_clicks12==0))):
            return Player1_style
        elif((is_open2==True and (n_clicks2==0)) or (is_open22==True and (n_clicks22==0))):
            return Player2_style
        elif((is_open3==True and (n_clicks3==0)) or (is_open32==True and (n_clicks32==0))):
            return Player3_style
        elif((is_open4==True and (n_clicks4==0)) or (is_open42==True and (n_clicks42==0))):
            return Player4_style
        elif((is_open5==True and (n_clicks5==0)) or (is_open52==True and (n_clicks52==0))):
            return Player5_style
        elif((is_open6==True and (n_clicks6==0)) or (is_open62==True and (n_clicks62==0))):
            return Player6_style
        elif((is_open7==True and (n_clicks7==0)) or (is_open72==True and (n_clicks72==0))):
            return Player7_style
        elif((is_open8==True and (n_clicks8==0)) or (is_open82==True and (n_clicks82==0))):
            return Player8_style
        elif((is_open9==True and (n_clicks9==0)) or (is_open92==True and (n_clicks92==0))):
            return Player9_style
        elif((is_open10==True and (n_clicks10==0)) or (is_open102==True and (n_clicks102==0))):
            return Player10_style
        elif((is_open11==True and (n_clicks11==0)) or (is_open112==True and (n_clicks112==0))):
            return Player11_style
        else:
            return PlayerBack_style     

    elif(phase==3):
    
        if((is_open6==True and (n_clicks6==0)) or (is_open62==True and (n_clicks62==0))):
            return rightGreen_style
        elif((is_open7==True and (n_clicks7==0)) or (is_open72==True and (n_clicks72==0))):
            return leftGreen_style
        elif((is_open8==True and (n_clicks8==0)) or (is_open82==True and (n_clicks82==0))):
            return middleGreen_style
        else:
            return Shoot_style
    
    
    elif(phase==4):
        
        if((is_open6==True and (n_clicks6==0)) or (is_open62==True and (n_clicks62==0))):
            return rightYellow_style
        elif((is_open7==True and (n_clicks7==0)) or (is_open72==True and (n_clicks72==0))):
            return leftYellow_style
        elif((is_open8==True and (n_clicks8==0)) or (is_open82==True and (n_clicks82==0))):
            return middleYellow_style
        else:
            return Save_style


    else:
        return PlayerBack_style 


@app.callback(
    Output('output1', 'style'),
    [Input("test", "data")])  
def computerPlayer(num):
    
    if(phase==0):
        if ((num == 1)):
            return Player1_styleBlue
        elif(num == 2):
            return Player2_styleBlue
        elif(num == 3):
            return Player3_styleBlue
        elif(num == 4):
            return Player4_styleBlue
        elif(num == 5):
            return Player5_styleBlue
        elif(num == 6):
            return Player6_styleBlue
        elif(num == 7):
            return Player7_styleBlue
        elif( num == 8):
            return Player8_styleBlue
        elif(num == 9):
            return Player9_styleBlue
        elif(num ==10):
            return Player10_styleBlue
        elif(num == 11):
            return Player11_styleBlue
        elif(num == 'R'):
            return rightYellow_style    
        elif(num == 'L'):
            return leftYellow_style
        elif(num == 'M'):
            return middleYellow_style
        else:
            return PlayerBack_styleBlue
        
        
    elif(phase==1):
        if ((num == 1)):
            return Player1_styleBlue
        elif(num == 2):
            return Player2_styleBlue
        elif(num == 3):
            return Player3_styleBlue
        elif(num == 4):
            return Player4_styleBlue
        elif(num == 5):
            return Player5_styleBlue
        elif(num == 6):
            return Player6_styleBlue
        elif(num == 7):
            return Player7_styleBlue
        elif( num == 8):
            return Player8_styleBlue
        elif(num == 9):
            return Player9_styleBlue
        elif(num ==10):
            return Player10_styleBlue
        elif(num == 11):
            return Player11_styleBlue
        elif(num == 'R'):
            return rightGreen_style    
        elif(num == 'L'):
            return leftGreen_style
        elif(num == 'M'):
            return middleGreen_style
        else:
            return PlayerBack_styleBlue
        
        
        
    elif(phase==3):
        return Save_style
        
        
    elif(phase==4):  
        return Shoot_style
    

    else:
        return PlayerBack_styleBlue


@app.callback(
    [Output("test", "data"),
     Output("popover1", "is_open"),
     Output("popover2", "is_open"),
     Output("popover3", "is_open"),
     Output("popover4", "is_open"),
     Output("popover5", "is_open"),
     Output("popover6", "is_open"),
     Output("popover7", "is_open"),
     Output("popover8", "is_open"),
     Output("popover9", "is_open"),
     Output("popover10", "is_open"),
     Output("popover11", "is_open"),   
     Output("popover1blue", "is_open"),
     Output("popover2blue", "is_open"),
     Output("popover3blue", "is_open"),
     Output("popover4blue", "is_open"),
     Output("popover5blue", "is_open"),
     Output("popover6blue", "is_open"),
     Output("popover7blue", "is_open"),
     Output("popover8blue", "is_open"),
     Output("popover9blue", "is_open"),
     Output("popover10blue", "is_open"),
     Output("popover11blue", "is_open"),
     Output('button1', 'n_clicks'),
     Output('button2', 'n_clicks'),
     Output('button3', 'n_clicks'),
     Output('button4', 'n_clicks'),
     Output('button5', 'n_clicks'),
     Output('button6', 'n_clicks'),
     Output('button7', 'n_clicks'),
     Output('button8', 'n_clicks'),
     Output('button9', 'n_clicks'),
     Output('button10', 'n_clicks'),
     Output('button11', 'n_clicks'),
     Output('button1blue', 'n_clicks'),
     Output('button2blue', 'n_clicks'),
     Output('button3blue', 'n_clicks'),
     Output('button4blue', 'n_clicks'),
     Output('button5blue', 'n_clicks'),
     Output('button6blue', 'n_clicks'),
     Output('button7blue', 'n_clicks'),
     Output('button8blue', 'n_clicks'),
     Output('button9blue', 'n_clicks'),
     Output('button10blue', 'n_clicks'),
     Output('button11blue', 'n_clicks'),
     Output('elementPhase', 'data'), 
     Output('player1Score', 'children'),
     Output('player1Pass', 'children'),   
     Output('player2Score', 'children'),
     Output('player2Pass', 'children'),
     ],
     
    [Input('button1', 'n_clicks'), Input('button2', 'n_clicks'), Input('button3', 'n_clicks'), Input('button4', 'n_clicks'), Input('button5', 'n_clicks'), Input('button6', 'n_clicks'),
     Input('button7', 'n_clicks'), Input('button8', 'n_clicks'), Input('button9', 'n_clicks'),Input('button10', 'n_clicks'),Input('button11', 'n_clicks'),
     
     Input('button1blue', 'n_clicks'), Input('button2blue', 'n_clicks'), Input('button3blue', 'n_clicks'), Input('button4blue', 'n_clicks'), Input('button5blue', 'n_clicks'), Input('button6blue', 'n_clicks'),
     Input('button7blue', 'n_clicks'), Input('button8blue', 'n_clicks'), Input('button9blue', 'n_clicks'),Input('button10blue', 'n_clicks'),Input('button11blue', 'n_clicks')]


)
def set_output232(n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11,
               n_clicks12, n_clicks22, n_clicks32, n_clicks42, n_clicks52, n_clicks62, n_clicks72, n_clicks82, n_clicks92, n_clicks102,
               n_clicks112):
    
    global FullListBlue
    global phase
    
    global score1
    global pass1
    global score2
    global pass2

    if(phase==1):

        playerNum = []
         
        if(n_clicks1 == 0):
            playerNum.append(1)            
        if(n_clicks2 == 0):
            playerNum.append(2)
        if(n_clicks3 == 0):
            playerNum.append(3)
        if(n_clicks4 == 0):
            playerNum.append(4)
        if(n_clicks5 == 0):
            playerNum.append(5)
        if(n_clicks6 == 0):
            playerNum.append(6)
        if(n_clicks7 == 0):
            playerNum.append(7)
        if(n_clicks8 == 0):
            playerNum.append(8)
        if(n_clicks9 == 0):
            playerNum.append(9)
        if(n_clicks10 == 0):
            playerNum.append(10)
        if(n_clicks11 == 0):
            playerNum.append(11)
            
            
        pass1 = min((11-len(playerNum)),7)
            
        if(len(playerNum) <= 4):
            phase=3
            FullListBlue = [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            return " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,FullListBlue[0], FullListBlue[1], FullListBlue[2], FullListBlue[3], FullListBlue[4], FullListBlue[5], FullListBlue[6],FullListBlue[7], FullListBlue[8], FullListBlue[9], FullListBlue[10], FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 3, score1, pass1, score2, pass2
        
        
        elif ((n_clicks1 == 1)):
            playerNum.append(1)
            random_num = random.choice(playerNum)
            
            if (random_num == 1):
                phase=0
                pass1=0
                FullListBlue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                return " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,FullListBlue[0], FullListBlue[1], FullListBlue[2], FullListBlue[3], FullListBlue[4], FullListBlue[5], FullListBlue[6],FullListBlue[7], FullListBlue[8], FullListBlue[9], FullListBlue[10], FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            else:
                phase=1
                
                if(len(playerNum) <= 6):
                    n_clicks1 = 1
                return random_num, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 1, score1, pass1, score2, pass2


        elif((n_clicks2 == 1)):
            playerNum.append(2)
            random_num = random.choice(playerNum)
            
            if (random_num == 2):
                phase=0
                pass1=0
                FullListBlue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                return " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,FullListBlue[0], FullListBlue[1], FullListBlue[2], FullListBlue[3], FullListBlue[4], FullListBlue[5], FullListBlue[6],FullListBlue[7], FullListBlue[8], FullListBlue[9], FullListBlue[10], FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            else:
                phase=1
                
                if(len(playerNum) <= 6):
                    n_clicks1 = 1
                return random_num, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 1, score1, pass1, score2, pass2
            
        elif((n_clicks3 == 1)):
            playerNum.append(3)
            random_num = random.choice(playerNum)
            
            if (random_num == 3):
                phase=0
                pass1=0
                FullListBlue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                return " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,FullListBlue[0], FullListBlue[1], FullListBlue[2], FullListBlue[3], FullListBlue[4], FullListBlue[5], FullListBlue[6],FullListBlue[7], FullListBlue[8], FullListBlue[9], FullListBlue[10], FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            else:
                phase=1
                
                if(len(playerNum) <= 6):
                    n_clicks1 = 1
                return random_num, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 1, score1, pass1, score2, pass2
            
        elif((n_clicks4 == 1)):
            playerNum.append(4)
            random_num = random.choice(playerNum)
            
            if (random_num == 4):
                phase=0
                pass1=0
                FullListBlue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                return " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,FullListBlue[0], FullListBlue[1], FullListBlue[2], FullListBlue[3], FullListBlue[4], FullListBlue[5], FullListBlue[6],FullListBlue[7], FullListBlue[8], FullListBlue[9], FullListBlue[10], FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            else:
                phase=1
                
                if(len(playerNum) <= 6):
                    n_clicks1 = 1
    
                return random_num, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 1, score1, pass1, score2, pass2
            
        elif((n_clicks5 == 1)):
            playerNum.append(5)
            random_num = random.choice(playerNum)
            
            if (random_num == 5):
                phase=0
                pass1=0
                FullListBlue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                return " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,FullListBlue[0], FullListBlue[1], FullListBlue[2], FullListBlue[3], FullListBlue[4], FullListBlue[5], FullListBlue[6],FullListBlue[7], FullListBlue[8], FullListBlue[9], FullListBlue[10], FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            else:
                phase=1
                
                if(len(playerNum) <= 6):
                    n_clicks1 = 1
                return random_num, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 1, score1, pass1, score2, pass2
            
        elif((n_clicks6 == 1)):
            playerNum.append(6)
            random_num = random.choice(playerNum)
            
            if (random_num == 6):
                phase=0
                pass1=0
                FullListBlue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                return " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,FullListBlue[0], FullListBlue[1], FullListBlue[2], FullListBlue[3], FullListBlue[4], FullListBlue[5], FullListBlue[6],FullListBlue[7], FullListBlue[8], FullListBlue[9], FullListBlue[10], FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            else:
                phase=1
                
                if(len(playerNum) <= 6):
                    n_clicks1 = 1
                return random_num, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 1, score1, pass1, score2, pass2
            
        elif((n_clicks7 == 1)):
            playerNum.append(7)
            random_num = random.choice(playerNum)
            
            if (random_num == 7):
                phase=0
                pass1=0
                FullListBlue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                return " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,FullListBlue[0], FullListBlue[1], FullListBlue[2], FullListBlue[3], FullListBlue[4], FullListBlue[5], FullListBlue[6],FullListBlue[7], FullListBlue[8], FullListBlue[9], FullListBlue[10], FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            else:
                phase=1
                
                if(len(playerNum) <= 6):
                    n_clicks1 = 1
                return random_num, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 1, score1, pass1, score2, pass2
            
        elif((n_clicks8 == 1)):
            playerNum.append(8)
            random_num = random.choice(playerNum)
            
            if (random_num == 8):
                phase=0
                pass1=0
                FullListBlue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                return " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,FullListBlue[0], FullListBlue[1], FullListBlue[2], FullListBlue[3], FullListBlue[4], FullListBlue[5], FullListBlue[6],FullListBlue[7], FullListBlue[8], FullListBlue[9], FullListBlue[10], FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            else:
                phase=1
                
                if(len(playerNum) <=6):
                    n_clicks1 = 1
                return random_num, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 1, score1, pass1, score2, pass2
            
        elif((n_clicks9 == 1)):
            playerNum.append(9)
            random_num = random.choice(playerNum)
            
            if (random_num == 9):
                phase=0
                pass1=0
                FullListBlue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                return " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,FullListBlue[0], FullListBlue[1], FullListBlue[2], FullListBlue[3], FullListBlue[4], FullListBlue[5], FullListBlue[6],FullListBlue[7], FullListBlue[8], FullListBlue[9], FullListBlue[10], FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            else:
                phase=1
                
                if(len(playerNum) <=6):
                    n_clicks1 = 1
                return random_num, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 1, score1, pass1, score2, pass2
            
        elif((n_clicks10 == 1)):
            playerNum.append(10)
            random_num = random.choice(playerNum)
            
            if (random_num == 10):
                phase=0
                pass1=0
                FullListBlue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                return " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,FullListBlue[0], FullListBlue[1], FullListBlue[2], FullListBlue[3], FullListBlue[4], FullListBlue[5], FullListBlue[6],FullListBlue[7], FullListBlue[8], FullListBlue[9], FullListBlue[10], FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            else:
                phase=1
                
                if(len(playerNum) <=6):
                    n_clicks1 = 1
                return random_num, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 1, score1, pass1, score2, pass2
            
        elif((n_clicks11 == 1)):
            playerNum.append(11)
            random_num = random.choice(playerNum)
            
            if (random_num == 11):
                phase=0
                pass1=0
                FullListBlue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                return " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,FullListBlue[0], FullListBlue[1], FullListBlue[2], FullListBlue[3], FullListBlue[4], FullListBlue[5], FullListBlue[6],FullListBlue[7], FullListBlue[8], FullListBlue[9], FullListBlue[10], FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            else:
                phase=1
                
                if(len(playerNum) <=6):
                    n_clicks1 = 1
                return random_num, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 1, score1, pass1, score2, pass2
            
        else:
            FullListBlue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            return " ",0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, score1, pass1, score2, pass2
        
    elif(phase==0):
        playerNumBlue = []

        if(n_clicks12 == 0):
            playerNumBlue.append(1)

            
        if(n_clicks22 == 0):
            playerNumBlue.append(2)

        
        if(n_clicks32 == 0):
            playerNumBlue.append(3)

        
        if(n_clicks42 == 0):
            playerNumBlue.append(4)
 
        
        if(n_clicks52 == 0):
            playerNumBlue.append(5)
 
        
        if(n_clicks62 == 0):
            playerNumBlue.append(6)
  
        
        if(n_clicks72 == 0):
            playerNumBlue.append(7)
 
        
        if(n_clicks82 == 0):
            playerNumBlue.append(8)
 
        
        if(n_clicks92 == 0):
            playerNumBlue.append(9)

        
        if(n_clicks102 == 0):
            playerNumBlue.append(10)
 
        
        if(n_clicks112 == 0):
            playerNumBlue.append(11)
            
            
        pass2 = min((11-len(playerNumBlue)), 7)

        
        if(len(playerNumBlue) <= 4):
            phase = 4
            FullListBlue = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1]
            return " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,FullListBlue[0], FullListBlue[1], FullListBlue[2], FullListBlue[3], FullListBlue[4], FullListBlue[5], FullListBlue[6],FullListBlue[7], FullListBlue[8], FullListBlue[9], FullListBlue[10], FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 4, score1, pass1, score2, pass2
        
        elif ((n_clicks12 == 1)):
            playerNumBlue.append(1)
            random_numBlue = random.choice(playerNumBlue)
            
            if(random_numBlue == 1):
                phase = 1
                pass2=0
                FullListBlue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]      
                return " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,FullListBlue[0], FullListBlue[1], FullListBlue[2], FullListBlue[3], FullListBlue[4], FullListBlue[5], FullListBlue[6],FullListBlue[7], FullListBlue[8], FullListBlue[9], FullListBlue[10], FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 1, score1, pass1, score2, pass2
            
            if(random_numBlue == 2):
                FullListBlue[11] += 1 
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1 

                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            if(random_numBlue == 3):
                FullListBlue[13] += 1
                
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1 
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            
            if(random_numBlue == 4):
                FullListBlue[14] += 1
                
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1 
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            if(random_numBlue == 5):
                FullListBlue[15] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1 
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            
            if(random_numBlue == 6):
                FullListBlue[16] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            if(random_numBlue == 7):
                FullListBlue[17] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            
            if(random_numBlue == 8):
                FullListBlue[18] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            
            if(random_numBlue == 9):
                FullListBlue[19] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            
            if(random_numBlue == 10):
                FullListBlue[20] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            
            if(random_numBlue == 11):
                FullListBlue[21] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2   
                

        elif((n_clicks22 == 1)):
            playerNumBlue.append(2)
            random_numBlue = random.choice(playerNumBlue)
            
            if(random_numBlue == 1):
                FullListBlue[11] += 1 
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            if(random_numBlue == 2):
                phase = 1
                pass2=0
                FullListBlue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0]       
                return " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,FullListBlue[0], FullListBlue[1], FullListBlue[2], FullListBlue[3], FullListBlue[4], FullListBlue[5], FullListBlue[6],FullListBlue[7], FullListBlue[8], FullListBlue[9], FullListBlue[10], FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 1, score1, pass1, score2, pass2
                
            
            
            if(random_numBlue == 3):
                FullListBlue[13] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            
            if(random_numBlue == 4):
                FullListBlue[14] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1 
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            if(random_numBlue == 5):
                FullListBlue[15] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            
            if(random_numBlue == 6):
                FullListBlue[16] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            if(random_numBlue == 7):
                FullListBlue[17] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            
            if(random_numBlue == 8):
                FullListBlue[18] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            
            if(random_numBlue == 9):
                FullListBlue[19] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            
            if(random_numBlue == 10):
                FullListBlue[20] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            
            if(random_numBlue == 11):
                FullListBlue[21] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2   
            
            
        elif((n_clicks32 == 1)):
            playerNumBlue.append(3)
            random_numBlue = random.choice(playerNumBlue)
            
            if(random_numBlue == 1):
                FullListBlue[11] += 1 
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            if(random_numBlue == 2):
                FullListBlue[12] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
                
            if(random_numBlue == 3):
                phase = 1
                pass2=0
                FullListBlue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0]           
                return " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,FullListBlue[0], FullListBlue[1], FullListBlue[2], FullListBlue[3], FullListBlue[4], FullListBlue[5], FullListBlue[6],FullListBlue[7], FullListBlue[8], FullListBlue[9], FullListBlue[10], FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 1, score1, pass1, score2, pass2
                
            if(random_numBlue == 4):
                FullListBlue[14] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            if(random_numBlue == 5):
                FullListBlue[15] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            
            if(random_numBlue == 6):
                FullListBlue[16] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            if(random_numBlue == 7):
                FullListBlue[17] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            
            if(random_numBlue == 8):
                FullListBlue[18] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            
            if(random_numBlue == 9):
                FullListBlue[19] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            
            if(random_numBlue == 10):
                FullListBlue[20] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            
            if(random_numBlue == 11):
                FullListBlue[21] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2  
            
            
        elif((n_clicks42 == 1)):
            playerNumBlue.append(4)
            random_numBlue = random.choice(playerNumBlue)
            
            if(random_numBlue == 1):
                FullListBlue[11] += 1 
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            if(random_numBlue == 2):
                FullListBlue[12] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
                
            if(random_numBlue == 3):
                FullListBlue[13] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2

            if(random_numBlue == 4):
                phase = 1
                pass2=0
                FullListBlue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0]          
                return " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,FullListBlue[0], FullListBlue[1], FullListBlue[2], FullListBlue[3], FullListBlue[4], FullListBlue[5], FullListBlue[6],FullListBlue[7], FullListBlue[8], FullListBlue[9], FullListBlue[10], FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 1, score1, pass1, score2, pass2
            
            if(random_numBlue == 5):
                FullListBlue[15] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            
            if(random_numBlue == 6):
                FullListBlue[16] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            if(random_numBlue == 7):
                FullListBlue[17] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            
            if(random_numBlue == 8):
                FullListBlue[18] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1 
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            
            if(random_numBlue == 9):
                FullListBlue[19] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            
            if(random_numBlue == 10):
                FullListBlue[20] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1 
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            
            if(random_numBlue == 11):
                FullListBlue[21] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1 
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2  
            

        elif((n_clicks52 == 1)):
            playerNumBlue.append(5)
            random_numBlue = random.choice(playerNumBlue)
           
            if(random_numBlue == 1):
                FullListBlue[11] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1  
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            if(random_numBlue == 2):
                FullListBlue[12] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1   
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
                
            if(random_numBlue == 3):
                FullListBlue[13] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2

            if(random_numBlue == 4):
                FullListBlue[14] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
                
            if(random_numBlue == 5):
                phase = 1
                pass2=0
                FullListBlue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0]           
                return " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,FullListBlue[0], FullListBlue[1], FullListBlue[2], FullListBlue[3], FullListBlue[4], FullListBlue[5], FullListBlue[6],FullListBlue[7], FullListBlue[8], FullListBlue[9], FullListBlue[10], FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 1, score1, pass1, score2, pass2

            if(random_numBlue == 6):
                FullListBlue[16] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            if(random_numBlue == 7):
                FullListBlue[17] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            
            if(random_numBlue == 8):
                FullListBlue[18] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            
            if(random_numBlue == 9):
                FullListBlue[19] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            
            if(random_numBlue == 10):
                FullListBlue[20] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            
            if(random_numBlue == 11):
                FullListBlue[21] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1 
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2  
           

        elif((n_clicks62 == 1)):
            playerNumBlue.append(6)
            random_numBlue = random.choice(playerNumBlue)
            
            if(random_numBlue == 1):
                FullListBlue[11] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            if(random_numBlue == 2):
                FullListBlue[12] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
                
            if(random_numBlue == 3):
                FullListBlue[13] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2

            if(random_numBlue == 4):
                FullListBlue[14] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
                
            if(random_numBlue == 5):
                FullListBlue[15] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2

            if(random_numBlue == 6):  
                phase = 1
                pass2=0
                FullListBlue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0]           
                return " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,FullListBlue[0], FullListBlue[1], FullListBlue[2], FullListBlue[3], FullListBlue[4], FullListBlue[5], FullListBlue[6],FullListBlue[7], FullListBlue[8], FullListBlue[9], FullListBlue[10], FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 1, score1, pass1, score2, pass2

            if(random_numBlue == 7):
                FullListBlue[17] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2

            if(random_numBlue == 8):
                FullListBlue[18] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2

            if(random_numBlue == 9):
                FullListBlue[19] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2

            if(random_numBlue == 10):
                FullListBlue[20] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2

            if(random_numBlue == 11):
                FullListBlue[21] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2  

        elif((n_clicks72 == 1)):
            playerNumBlue.append(7)
            random_numBlue = random.choice(playerNumBlue)
            
            if(random_numBlue == 1):
                FullListBlue[11] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1 
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            if(random_numBlue == 2):
                FullListBlue[12] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
                
            if(random_numBlue == 3):
                FullListBlue[13] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2

            if(random_numBlue == 4):
                FullListBlue[14] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
                
            if(random_numBlue == 5):
                FullListBlue[15] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2

            if(random_numBlue == 6):
                FullListBlue[16] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2  
                
            if(random_numBlue == 7):
                phase = 1
                pass2=0
                FullListBlue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0]           
                return " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,FullListBlue[0], FullListBlue[1], FullListBlue[2], FullListBlue[3], FullListBlue[4], FullListBlue[5], FullListBlue[6],FullListBlue[7], FullListBlue[8], FullListBlue[9], FullListBlue[10], FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 1, score1, pass1, score2, pass2

            if(random_numBlue == 8):
                FullListBlue[18] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2

            if(random_numBlue == 9):
                FullListBlue[19] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2

            if(random_numBlue == 10):
                FullListBlue[20] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2

            if(random_numBlue == 11):
                FullListBlue[21] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2  
            
        elif((n_clicks82 == 1)):
            playerNumBlue.append(8)
            random_numBlue = random.choice(playerNumBlue)
            if(random_numBlue == 1):
                FullListBlue[11] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            if(random_numBlue == 2):
                FullListBlue[12] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1 
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
                
            if(random_numBlue == 3):
                FullListBlue[13] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1  
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2

            if(random_numBlue == 4):
                FullListBlue[14] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1 
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
                
            if(random_numBlue == 5):
                FullListBlue[15] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2

            if(random_numBlue == 6):
                FullListBlue[16] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1 
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2  
                
            if(random_numBlue == 7):
                FullListBlue[17] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1  
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2

            if(random_numBlue == 8):
                phase = 1
                pass2=0
                FullListBlue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0]            
                return " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,FullListBlue[0], FullListBlue[1], FullListBlue[2], FullListBlue[3], FullListBlue[4], FullListBlue[5], FullListBlue[6],FullListBlue[7], FullListBlue[8], FullListBlue[9], FullListBlue[10], FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 1, score1, pass1, score2, pass2
                
            if(random_numBlue == 9):
                FullListBlue[19] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2

            if(random_numBlue == 10):
                FullListBlue[20] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2

            if(random_numBlue == 11):
                FullListBlue[21] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1 
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2  
            

        elif((n_clicks92 == 1)):
            playerNumBlue.append(9)
            random_numBlue = random.choice(playerNumBlue)
            
            if(random_numBlue == 1):
                FullListBlue[11] += 1 
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            if(random_numBlue == 2):
                FullListBlue[12] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_num, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
                
            if(random_numBlue == 3):
                FullListBlue[13] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2

            if(random_numBlue == 4):
                FullListBlue[14] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
                
            if(random_numBlue == 5):
                FullListBlue[15] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2

            if(random_numBlue == 6):
                FullListBlue[16] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2  
                
            if(random_numBlue == 7):
                FullListBlue[17] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2

            if(random_numBlue == 8):
                FullListBlue[18] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
                
                
            if(random_numBlue == 9):
                phase = 1
                pass2=0
                FullListBlue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0]             
                return " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,FullListBlue[0], FullListBlue[1], FullListBlue[2], FullListBlue[3], FullListBlue[4], FullListBlue[5], FullListBlue[6],FullListBlue[7], FullListBlue[8], FullListBlue[9], FullListBlue[10], FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 1, score1, pass1, score2, pass2
                
            if(random_numBlue == 10):
                FullListBlue[20] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2

            if(random_numBlue == 11):
                FullListBlue[21] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2  
            

        elif((n_clicks102 == 1)):
            playerNumBlue.append(10)
            random_numBlue = random.choice(playerNumBlue)
            
            if(random_numBlue == 1):
                FullListBlue[11] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            if(random_numBlue == 2):
                FullListBlue[12] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
                
            if(random_numBlue == 3):
                FullListBlue[13] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_num, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2

            if(random_numBlue == 4):
                FullListBlue[14] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
                
            if(random_numBlue == 5):
                FullListBlue[15] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2

            if(random_numBlue == 6):
                FullListBlue[16] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2  
                
            if(random_numBlue == 7):
                FullListBlue[17] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2

            if(random_numBlue == 8):
                FullListBlue[18] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
                
                
            if(random_numBlue == 9):
                FullListBlue[19] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2

            if(random_numBlue == 10):
                phase = 1
                pass2=0
                FullListBlue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0]               
                return " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,FullListBlue[0], FullListBlue[1], FullListBlue[2], FullListBlue[3], FullListBlue[4], FullListBlue[5], FullListBlue[6],FullListBlue[7], FullListBlue[8], FullListBlue[9], FullListBlue[10], FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 1, score1, pass1, score2, pass2
            
            if(random_numBlue == 11):
                FullListBlue[21] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2  
            
            
        elif((n_clicks112 == 1)):
            playerNumBlue.append(11)
            random_numBlue = random.choice(playerNumBlue)
            
            if(random_numBlue == 1):
                FullListBlue[11] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
            
            if(random_numBlue == 2):
                FullListBlue[12] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
                
            if(random_numBlue == 3):
                FullListBlue[13] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2

            if(random_numBlue == 4):
                FullListBlue[14] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
                
            if(random_numBlue == 5):
                FullListBlue[15] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2

            if(random_numBlue == 6):
                FullListBlue[16] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2  
                
            if(random_numBlue == 7):
                FullListBlue[17] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2

            if(random_numBlue == 8):
                FullListBlue[18] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
  
            if(random_numBlue == 9):
                FullListBlue[19] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2

            if(random_numBlue == 10):
                FullListBlue[20] += 1
                if(len(playerNumBlue) <=6):
                    FullListBlue[11] += 1
                return random_numBlue, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9, n_clicks10, n_clicks11, FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2  
                
            if(random_numBlue == 11):
                phase = 1
                pass2=0
                FullListBlue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0]            
                return " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,FullListBlue[0], FullListBlue[1], FullListBlue[2], FullListBlue[3], FullListBlue[4], FullListBlue[5], FullListBlue[6],FullListBlue[7], FullListBlue[8], FullListBlue[9], FullListBlue[10], FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 1, score1, pass1, score2, pass2
                
        else:
            return " ",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, score1, pass1, score2, pass2  
    
    elif(phase==3):
    
        Shot = ['L','M','R']
        
        random_Shot = random.choice(Shot)
    
        if((n_clicks6 == 1)):
    
            if (random_Shot == 'R'):
                phase=0
                pass1=0
                FullListBlue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                return random_Shot, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,FullListBlue[0], FullListBlue[1], FullListBlue[2], FullListBlue[3], FullListBlue[4], FullListBlue[5], FullListBlue[6],FullListBlue[7], FullListBlue[8], FullListBlue[9], FullListBlue[10], FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2

            else:
                phase=0
                pass1=0
                score1 +=1
                FullListBlue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                return random_Shot, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,FullListBlue[0], FullListBlue[1], FullListBlue[2], FullListBlue[3], FullListBlue[4], FullListBlue[5], FullListBlue[6],FullListBlue[7], FullListBlue[8], FullListBlue[9], FullListBlue[10], FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
        
        elif((n_clicks7 == 1)):
        
            if (random_Shot == 'L'):
                phase=0
                pass1=0
                FullListBlue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                return random_Shot, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,FullListBlue[0], FullListBlue[1], FullListBlue[2], FullListBlue[3], FullListBlue[4], FullListBlue[5], FullListBlue[6],FullListBlue[7], FullListBlue[8], FullListBlue[9], FullListBlue[10], FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2

            else:
                phase=0
                pass1=0
                score1 +=1
                FullListBlue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                return random_Shot, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,FullListBlue[0], FullListBlue[1], FullListBlue[2], FullListBlue[3], FullListBlue[4], FullListBlue[5], FullListBlue[6],FullListBlue[7], FullListBlue[8], FullListBlue[9], FullListBlue[10], FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2
        
        
        if((n_clicks8 == 1)):
        
            if (random_Shot == 'M'):
                phase=0
                pass1=0
                FullListBlue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                return random_Shot, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,FullListBlue[0], FullListBlue[1], FullListBlue[2], FullListBlue[3], FullListBlue[4], FullListBlue[5], FullListBlue[6],FullListBlue[7], FullListBlue[8], FullListBlue[9], FullListBlue[10], FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2

            else:
                phase=0
                pass1=0
                score1 +=1
                FullListBlue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                return random_Shot, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,FullListBlue[0], FullListBlue[1], FullListBlue[2], FullListBlue[3], FullListBlue[4], FullListBlue[5], FullListBlue[6],FullListBlue[7], FullListBlue[8], FullListBlue[9], FullListBlue[10], FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 0, score1, pass1, score2, pass2  
        

        
    elif(phase==4):
        
        Shot = ['L','M','R']
        
        random_Shot = random.choice(Shot)
    
        if((n_clicks6 == 1)):
    
            if (random_Shot == 'R'):
                phase=1
                pass2=0
                FullListBlue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                return random_Shot, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,FullListBlue[0], FullListBlue[1], FullListBlue[2], FullListBlue[3], FullListBlue[4], FullListBlue[5], FullListBlue[6],FullListBlue[7], FullListBlue[8], FullListBlue[9], FullListBlue[10], FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 1, score1, pass1, score2, pass2

            else:
                phase=1
                pass2=0
                score2 += 1
                FullListBlue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                return random_Shot, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,FullListBlue[0], FullListBlue[1], FullListBlue[2], FullListBlue[3], FullListBlue[4], FullListBlue[5], FullListBlue[6],FullListBlue[7], FullListBlue[8], FullListBlue[9], FullListBlue[10], FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 1, score1, pass1, score2, pass2
        
        elif((n_clicks7 == 1)):
        
            if (random_Shot == 'L'):
                phase=1
                pass2=0
                FullListBlue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                return random_Shot, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,FullListBlue[0], FullListBlue[1], FullListBlue[2], FullListBlue[3], FullListBlue[4], FullListBlue[5], FullListBlue[6],FullListBlue[7], FullListBlue[8], FullListBlue[9], FullListBlue[10], FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 1, score1, pass1, score2, pass2

            else:
                phase=1
                pass2=0
                score2 += 1
                FullListBlue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                return random_Shot, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,FullListBlue[0], FullListBlue[1], FullListBlue[2], FullListBlue[3], FullListBlue[4], FullListBlue[5], FullListBlue[6],FullListBlue[7], FullListBlue[8], FullListBlue[9], FullListBlue[10], FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 1, score1, pass1, score2, pass2
        
        
        if((n_clicks8 == 1)):
        
            if (random_Shot == 'M'):
                phase=1
                pass2=0
                FullListBlue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                return random_Shot, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,FullListBlue[0], FullListBlue[1], FullListBlue[2], FullListBlue[3], FullListBlue[4], FullListBlue[5], FullListBlue[6],FullListBlue[7], FullListBlue[8], FullListBlue[9], FullListBlue[10], FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 1, score1, pass1, score2, pass2

            else:
                phase=1
                pass2=0
                score2 += 1
                FullListBlue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                return random_Shot, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,FullListBlue[0], FullListBlue[1], FullListBlue[2], FullListBlue[3], FullListBlue[4], FullListBlue[5], FullListBlue[6],FullListBlue[7], FullListBlue[8], FullListBlue[9], FullListBlue[10], FullListBlue[11], FullListBlue[12], FullListBlue[13], FullListBlue[14], FullListBlue[15], FullListBlue[16], FullListBlue[17], FullListBlue[18], FullListBlue[19], FullListBlue[20], FullListBlue[21], 1, score1, pass1, score2, pass2          
        
  
    else:
        return " ",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, score1, pass1, score2, pass2


@app.callback(Output('PlayerSelection', 'children'), [Input('intermediate-value', 'data'), Input('test', 'data')])
def checkPlayerNum(data1, data2):
    
    if(data2 == " "):
        return " "
    else:
        return data1


@app.callback(Output('ComputerSelection', 'children'), [Input('test', 'data')])
def checkComputerNum(data):
    return data


@app.callback(Output('GameCheck', 'children'), [Input('intermediate-value', 'data'), Input('test', 'data'), Input('player1Pass', 'children'),
                                                Input('player2Pass', 'children')])
def checkMatch(data1, data2, pass1, pass2):
    
    global phase
    
    if((phase==1) or (phase==0)):
        
        if((data1=='L') and (data2=='L')):
            return 'Saved'
        elif((data1=='R') and (data2=='R')):
            return 'Saved'
        elif((data1=='M') and (data2=='M')):
            return 'Saved'
        elif((data2=='L') and (data1 != 'L')):
            return 'Scored'
        elif((data2=='R') and (data1 != 'R')):
            return 'Scored'
        elif((data2=='M') and (data1 != 'M')):
            return 'Scored'
        elif((data1 != data2) and (pass1 != 0)):
            return 'Safe'  
        elif((data1 != data2) and (pass2 != 0)):
            return 'Safe'     
        elif((pass1==0) and (pass2==0)):
            return 'Match'
        else:
            return 'Match'
        
    if((phase==3) or (phase==4)):    
        if((pass1 == 7)):
            return 'Shoot'  
        elif((pass2 == 7)):
            return 'Save'  
        else:
            return 'Match'
    else:
        return 'Match'


@app.callback(Output('barStyle', 'style'), [Input('GameCheck', 'children')])
def barStyle(move):
    
    if(move == 'Match'):
        return match_style
    elif(move == 'Shoot'):
        return shoot_style
    elif(move == 'Save'):
        return save_style
    elif(move == 'Safe'):
        return safe_style
    elif(move == 'Saved'):
        return saved_style
    elif(move == 'Scored'):
        return scored_style
    else:
        return match_style


@app.callback([Output('button1', 'style'),Output('button1', 'disabled')], [Input('button1', 'n_clicks'), Input('elementPhase', 'data'),
                                                                           Input('popover1', 'is_open')])
def change_button_style1(n_clicks, data, is_open):

    if(data == 1):
    
        if is_open:
            
            return green_button_style1High, False
            
        elif n_clicks > 0:

            return hide_button_style1, True

        else:

            return green_button_style1, False
        
    else:
        return hide_button_display, True
    
    
@app.callback([Output('button2', 'style'),Output('button2', 'disabled')] , [Input('button2', 'n_clicks'), Input('elementPhase', 'data'),
                                                                            Input('popover2', 'is_open')])
def change_button_style2(n_clicks, data, is_open):

    if(data==1):
        
        if is_open:
                
            return red_button_style2High, False
        
        elif n_clicks > 0:

            return hide_button_style2, True

        else:

            return red_button_style2, False
    
    else:
        return hide_button_display, True
    
    
@app.callback([Output('button3', 'style'), Output('button3', 'disabled')], [Input('button3', 'n_clicks'), Input('elementPhase', 'data'),
                                                                            Input('popover3', 'is_open')])
def change_button_style3(n_clicks, data, is_open):

    if (data==1):
        
        if is_open:
            return red_button_style3High, False
        
        elif n_clicks > 0:
            return hide_button_style3, True

        else:
            return red_button_style3, False
    
    else:
        return hide_button_display, True
    
@app.callback([Output('button4', 'style'), Output('button4', 'disabled')], [Input('button4', 'n_clicks'), Input('elementPhase', 'data'),
                                                                            Input('popover4', 'is_open')])
def change_button_style4(n_clicks, data, is_open):

    if (data==1):
        
        if is_open:
            return red_button_style4High, False
        
        elif n_clicks > 0:

            return hide_button_style4, True

        else:

            return red_button_style4, False
        
    else:
        return hide_button_display, True

@app.callback([Output('button5', 'style'), Output('button5', 'disabled')], [Input('button5', 'n_clicks'), Input('elementPhase', 'data'),
                                                                            Input('popover5', 'is_open')])
def change_button_style5(n_clicks, data, is_open):

    if (data==1):
        if is_open:
            return red_button_style5High, False

        elif n_clicks > 0:

            return hide_button_style5, True

        else:

            return red_button_style5, False
    
    else:
        return hide_button_display, True
    
    
@app.callback([Output('button6', 'style'), Output('button6', 'disabled'), Output('button6', 'children')], [Input('button6', 'n_clicks'), Input('elementPhase', 'data'),
                                                                            Input('popover6', 'is_open')])
def change_button_style6(n_clicks, data, is_open):

    if (data==1):
        
        if is_open:
            return red_button_style6High, False, 6
            
        elif n_clicks > 0:

            return hide_button_style6, True, 6

        else:

            return red_button_style6, False, 6
    
    elif (data == 3):
        if is_open:
            return shoot_button_style6High, False, 'R'
            
        elif n_clicks > 0:

            return hide_button_style6, True, 'R'

        else:

            return shoot_button_style6, False, 'R'

    else:
        return hide_button_display, True, 6
    
    
    
@app.callback([Output('button7', 'style'), Output('button7', 'disabled'), Output('button7', 'children')], [Input('button7', 'n_clicks'), Input('elementPhase', 'data'),
                                                                            Input('popover7', 'is_open')])
def change_button_style7(n_clicks, data, is_open):

    if (data==1):
        
        if is_open:
            return red_button_style7High, False, 7
        
        elif n_clicks > 0:

            return hide_button_style7, True, 7

        else:

            return red_button_style7, False, 7
        
        
    elif (data == 3):
        if is_open:
            return shoot_button_style7High, False, 'L'
            
        elif n_clicks > 0:

            return hide_button_style7, True, 'L'

        else:

            return shoot_button_style7, False, 'L'
        
    else:
        return hide_button_display, True, 7
    
    
@app.callback([Output('button8', 'style'), Output('button8', 'disabled'), Output('button8', 'children')], [Input('button8', 'n_clicks'), Input('elementPhase', 'data'),
                                                                            Input('popover8', 'is_open')])
def change_button_style8(n_clicks, data, is_open):

    if (data==1):
        
        if is_open:
            return red_button_style8High, False, 8
        
        elif n_clicks > 0:
            return hide_button_style8, True, 8

        else:
            return red_button_style8, False, 8
    
    
    elif (data == 3):
        if is_open:
            return shoot_button_style8High, False, 'M'
            
        elif n_clicks > 0:

            return hide_button_style8, True, 'M'

        else:

            return shoot_button_style8, False, 'M'
    
    
    
    else:
        return hide_button_display, True, 8
    
    
    
@app.callback([Output('button9', 'style'), Output('button9', 'disabled')], [Input('button9', 'n_clicks'), Input('elementPhase', 'data'),
                                                                            Input('popover9', 'is_open')])
def change_button_style9(n_clicks, data, is_open):

    if (data==1):
        
        if is_open:
            return red_button_style9High, False
            
        elif n_clicks > 0:

            return hide_button_style9, True

        else:

            return red_button_style9, False
    
    else:
        return hide_button_display, True
    
@app.callback([Output('button10', 'style'), Output('button10', 'disabled')], [Input('button10', 'n_clicks'), Input('elementPhase', 'data'),
                                                                              Input('popover10', 'is_open')])
def change_button_style10(n_clicks, data, is_open):

    if (data==1):
        
        if is_open:
            return red_button_style10High, False
        
        elif n_clicks > 0:
            return hide_button_style10, True

        else:
            return red_button_style10, False
    
    else:
        return hide_button_display, True
    
@app.callback([Output('button11', 'style'), Output('button11', 'disabled')], [Input('button11', 'n_clicks'), Input('elementPhase', 'data'),
                                                                              Input('popover11', 'is_open')])
def change_button_style11(n_clicks, data, is_open):

    if(data==1):
        if is_open:
            return red_button_style11High, False
        
        elif n_clicks > 0:

            return hide_button_style11, True

        else:

            return red_button_style11, False
        
    else:
        return hide_button_display, True
    

@app.callback([Output('button1blue', 'style'), Output('button1blue', 'disabled')], [Input('button1blue', 'n_clicks'), Input('elementPhase', 'data'),
                                                                                  Input('popover1blue', 'is_open')])
def change_button_style1blue(n_clicks, data, is_open):

    if (data==0):
        
        if is_open:
            return yellow_button_style1High, False 
        elif n_clicks > 0:
            return hide_button_style1blue, True
        else:
            return yellow_button_style1, False 
    else:
        return hide_button_display, True


@app.callback([Output('button2blue', 'style'), Output('button2blue', 'disabled')], [Input('button2blue', 'n_clicks'), Input('elementPhase', 'data'),
                                                                                    Input('popover2blue', 'is_open')])
def change_button_style2blue(n_clicks, data, is_open):

    if (data==0):
        
        if is_open:
            return blue_button_style2High, False 
        
        elif n_clicks > 0:

            return hide_button_style2, True

        else:

            return blue_button_style2, False
    
    else:
        return hide_button_display, True
    
    
@app.callback([Output('button3blue', 'style'), Output('button3blue', 'disabled')], [Input('button3blue', 'n_clicks'), Input('elementPhase', 'data'),
                                                                                    Input('popover3blue', 'is_open')])
def change_button_style3blue(n_clicks, data, is_open):

    if (data==0):
        
        if is_open:
            return blue_button_style3High, False 
        
        elif n_clicks > 0:

            return hide_button_style3, True

        else:

            return blue_button_style3, False
    
    else:
        return hide_button_display, True
    
@app.callback([Output('button4blue', 'style'), Output('button4blue', 'disabled')], [Input('button4blue', 'n_clicks'), Input('elementPhase', 'data'),
                                                                                    Input('popover4blue', 'is_open')])
def change_button_style4blue(n_clicks, data, is_open):

    if (data==0):
        
        if is_open:
            return blue_button_style4High, False 
        
        elif n_clicks > 0:

            return hide_button_style4, True

        else:

            return blue_button_style4, False
        
    else:
        return hide_button_display, True

@app.callback([Output('button5blue', 'style'), Output('button5blue', 'disabled')], [Input('button5blue', 'n_clicks'), Input('elementPhase', 'data'),
                                                                                    Input('popover5blue', 'is_open')])
def change_button_style5blue(n_clicks, data, is_open):

    if (data==0):
        
        if is_open:
            return blue_button_style5High, False 

        elif n_clicks > 0:

            return hide_button_style5, True

        else:

            return blue_button_style5, False
    
    else:
        return hide_button_display, True
    
    
@app.callback([Output('button6blue', 'style'), Output('button6blue', 'disabled'), Output('button6blue', 'children')], [Input('button6blue', 'n_clicks'), Input('elementPhase', 'data'),
                                                                                    Input('popover6blue', 'is_open')])
def change_button_style6blue(n_clicks, data, is_open):

    if (data==0):
        
        if is_open:
            return blue_button_style6High, False, 6
                  
        elif n_clicks > 0:

            return hide_button_style6, True, 6

        else:

            return blue_button_style6, False, 6
        
        
    elif (data == 4):
        if is_open:
            return save_button_style6High, False, 'R'
            
        elif n_clicks > 0:

            return hide_button_style6, True, 'R'

        else:

            return save_button_style6, False, 'R'
        
  
    else:
        return hide_button_display, True, 6
    
    
@app.callback([Output('button7blue', 'style'), Output('button7blue', 'disabled'), Output('button7blue', 'children')], [Input('button7blue', 'n_clicks'), Input('elementPhase', 'data'),
                                                                                    Input('popover7blue', 'is_open')])
def change_button_style7blue(n_clicks, data, is_open):

    if (data==0):
        
        if is_open:
            return blue_button_style7High, False, 7
        
        elif n_clicks > 0:

            return hide_button_style7, True, 7

        else:

            return blue_button_style7, False, 7
        
    elif (data == 4):
        if is_open:
            return save_button_style7High, False, 'L'
            
        elif n_clicks > 0:

            return hide_button_style7, True, 'L'

        else:

            return save_button_style7, False, 'L'
        
    else:
        return hide_button_display, True, 7
    
    
@app.callback([Output('button8blue', 'style'), Output('button8blue', 'disabled'),Output('button8blue', 'children')], [Input('button8blue', 'n_clicks'), Input('elementPhase', 'data'),
                                                                                    Input('popover8blue', 'is_open')])
def change_button_style8blue(n_clicks, data, is_open):

    if (data==0):
        
        if is_open:
            return blue_button_style8High, False, 8
        
        elif n_clicks > 0:

            return hide_button_style8, True, 8

        else:
            
            return blue_button_style8, False, 8
         
    elif (data == 4):
        if is_open:
            return save_button_style8High, False, 'M'
            
        elif n_clicks > 0:

            return hide_button_style8, True, 'M'

        else:

            return save_button_style8, False, 'M'
    
    else:
        return hide_button_display, True, 8
    
@app.callback([Output('button9blue', 'style'), Output('button9blue', 'disabled')], [Input('button9blue', 'n_clicks'), Input('elementPhase', 'data'),
                                                                                    Input('popover9blue', 'is_open')])
def change_button_style9blue(n_clicks, data, is_open):

    if (data==0):
        
        if is_open:
            return blue_button_style9High, False 
        
        elif n_clicks > 0:

            return hide_button_style9, True

        else:

            return blue_button_style9, False
    
    else:
        return hide_button_display, True
    
@app.callback([Output('button10blue', 'style'), Output('button10blue', 'disabled')], [Input('button10blue', 'n_clicks'), Input('elementPhase', 'data'),
                                                                                      Input('popover10blue', 'is_open')])
def change_button_style10blue(n_clicks, data, is_open):

    if (data==0):
        
        if is_open:
            return blue_button_style10High, False 
        
        elif n_clicks > 0:

            return hide_button_style10, True

        else:

            return blue_button_style10, False
    
    else:
        return hide_button_display, True
    
@app.callback([Output('button11blue', 'style'), Output('button11blue', 'disabled')], [Input('button11blue', 'n_clicks'), Input('elementPhase', 'data'),
                                                                                      Input('popover11blue', 'is_open')])
def change_button_style11blue(n_clicks, data, is_open):

    if (data==0):
        
        if is_open:
            return blue_button_style11High, False 
        
        elif n_clicks > 0:

            return hide_button_style11, True

        else:

            return blue_button_style11, False
        
    else:
        return hide_button_display, True
    

if __name__ == '__main__':
    app.run_server(debug=True)