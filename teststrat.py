from soccersimulator import Strategy
from soccersimulator import SoccerTeam, Simulation, SoccerAction
from toolbox import MyState, Action
from soccersimulator import Vector2D
from soccersimulator.settings import *
from strat import fonceurball

class ElStrategy2(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
        self.mydic = dict()
        self.mydic["c"] = 0
    def compute_strategy(self,state,id_team,id_player):
        mystate= MyState(state,id_team,id_player)
        action= Action(mystate)
        self.mydic["c"]+=1
        if self.mydic["c"]<0:
            return donothing()
        if mystate.my_position.distance(mystate.ball_position)<1.65:
            return(action.shoot_but_adv)
        if mystate.my_position.distance(mystate.ball_position)<9.65:
            return ralentir(mystate,action)
        return fonceurball(mystate)
    
#Attente ok
        


def donothing():
    return(SoccerAction(Vector2D(0,0),Vector2D(0,0)))

def ralentir(mystate,action):
        return SoccerAction((mystate.ball_position-mystate.my_position).norm_max(0.09),Vector2D(0,0))

