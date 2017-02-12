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
        


def defonceur(mystate,action):
    if(mystate.my_position.distance(mystate.ball_position)<1.65):
        return(action.shoot_but_adv)
    if(mystate.position_mon_but.distance(mystate.ball_position)<GAME_WIDTH/2):
        return fonceurball(mystate)
    if(mystate.position_mon_but.x==GAME_WIDTH):
        return action.sprint(Vector2D(4*GAME_WIDTH/5,mystate.ball_position.y))
    else:
        return action.sprint(Vector2D(GAME_WIDTH/5,mystate.ball_position.y))