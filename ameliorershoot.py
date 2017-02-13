from soccersimulator import SoccerTeam, Simulation, SoccerState, Vector2D, SoccerAction, Strategy
from soccersimulator import SimuGUI,show_state, show_simu
import random, math
from soccersimulator.settings import *
from toolbox import MyState, Action


def exp(b,a,x):
    return(b*(1-math.exp(-a*x)))

def xexpalpha(b,a,x):
    return(b*x**a)

def shoot(fct,mystate):
    return SoccerAction(Vector2D(),(mystate.position_but_adv-mystate.my_position).normalize()*fct)


class shoot(Strategy):
    def __init__(self):
        Strategy.__init__(self,"ElMatador")
        self.mydic = dict()
        self.mydic["c"] = 0
    def compute_strategy(self,state,id_team,id_player):
        mystate= MyState(state,id_team,id_player)
        action= Action(mystate)
        if self.mydic["c"]==0:
            return SoccerAction((mystate.ball_position-mystate.my_position).norm_max(0.01),Vector2D())
        self.mydic["c"]+=1
        x=mystate.my_position.distance(mystate.position_but_adv)
        return shoot(exp(2,1,x),mystate)

team1 = SoccerTeam(name="France",login="Paul")
team2 = SoccerTeam(name="Liban",login="Hassan")
team1.add("Paul",shoot())
team2.add("Hassan",shoot())


def get_team(i):
    if i==1:
        return team1
    if i==2:
        return team2
    if i==4:
        return team4



state=SoccerState.create_initial_state(1,0)
state.player_state(1,0).position=Vector2D(GAME_WIDTH/2+random.uniform(0,1)*GAME_WIDTH/2,random.uniform(0,1)*GAME_WIDTH/2)
state.ball.position=state.player_state(1,0).position

simu = Simulation(team1,team2,50,state)
#Jouer et afficher la partie
show_simu(simu)

