from soccersimulator import Strategy, SoccerTeam
from toolbox import MyState, Action
from soccersimulator import Vector2D
from soccersimulator.settings import *
from toolbox import Shootameliorer

from soccersimulator import SimuGUI,show_state,show_simu, Simulation
from strat import ElDefenseur, ElStrategySolo, fonceurballdef, fonceurball, ElLooser

class ElStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"ElMatadorSolo")
        self.mydic = dict()
        self.mydic["c"] = 0
    def compute_strategy(self,state,id_team,id_player):
        mystate= MyState(state,id_team,id_player)
        action= Action(mystate)
        x=mystate.ball_position.distance(mystate.position_but_adv)
        self.mydic["c"]+=1
        if self.mydic["c"]<0:
            return donothing()
            
        if mystate.my_position.distance(mystate.ball_position)<1.65:
            if(mystate.ball_position.distance(Vector2D(mystate.position_but_adv.x,mystate.ball_position.y))<=(2./7)*GAME_WIDTH/2) or ((mystate.ball_position.distance(Vector2D(mystate.position_but_adv.x,mystate.ball_position.y))<=(3./7)*GAME_WIDTH/2) and mystate.ball_position.distance(Vector2D(mystate.ball_position.x,GAME_HEIGHT/2))<=(1./4)*GAME_HEIGHT):
                return Shootameliorer(mystate,x).shoot
            return(action.petit_shoot_but_adv)

        if mystate.my_position.distance(mystate.ball_position)<10:
            return fonceurballdef(mystate)

        if(mystate.position_mon_but.x==GAME_WIDTH):
            if (mystate.position_mon_but.distance(mystate.ball_position)<GAME_WIDTH*0.25):
                return action.sprint(Vector2D(0.65*GAME_WIDTH,mystate.ball_position.y))
            if (mystate.position_mon_but.distance(mystate.ball_position)<=GAME_WIDTH/2):
                return action.sprint(Vector2D(0.5*GAME_WIDTH,mystate.ball_position.y))

        if(mystate.position_mon_but.x==0):
            if (mystate.position_mon_but.distance(mystate.ball_position)<GAME_WIDTH*0.45):
                return action.sprint(Vector2D(0.4*GAME_WIDTH,mystate.ball_position.y))
            if (mystate.position_mon_but.distance(mystate.ball_position)<=GAME_WIDTH/2):
                return action.sprint(Vector2D(0.5*GAME_WIDTH,mystate.ball_position.y))
        
        return fonceurball(mystate)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
## Creation d'une equipe
team1 = SoccerTeam(name="team1",login="etu1")
team2 = SoccerTeam(name="team2",login="etu2")
team1.add("Hassan",ElDefenseur())
team1.add("Booba",ElStrategySolo())
team2.add("Paul",ElStrategy())
team2.add("Pogba",ElDefenseur())




#Creation d'une partie
simu = Simulation(team1,team2)
#Jouer et afficher la partie
show_simu(simu)