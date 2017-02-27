from soccersimulator import SoccerTeam, Simulation, Vector2D, SoccerAction, Strategy
from soccersimulator import show_simu
import random, math
from soccersimulator.settings import *
from toolbox import MyState
import numpy as np

def superf(a,b,c,d,e,x):
    return min(a*x**2+b*sin(x)**c+d*cos(x)**e,15)

def expf(a,b,x):
    return min(b*(1-math.exp(-a*x)),15)

def xexpalpha(a,b,x):
    return min(b*x**a,15)

def shootf(fct,mystate):
    return SoccerAction(Vector2D(),(mystate.position_but_adv-mystate.my_position).normalize()*fct)

class shoot(Strategy):
    def __init__(self):
        Strategy.__init__(self,"ElMatador")
        self.a = 0
        self.b = 0
    def compute_strategy(self,state,id_team,id_player):
        mystate= MyState(state,id_team,id_player)
        x=mystate.my_position.distance(mystate.position_but_adv)
        return shootf(expf(self.a,self.b,x),mystate)

team1 = SoccerTeam(name="France",login="Paul")
team2 = SoccerTeam(name="Liban",login="Hassan")
team1.add("Paul",shoot())
team2.add("Hassan",shoot())



# Class Obeserver
class Observer(object):
    MAX_STEP=40
    def __init__(self,visu = False):  # Visu permet la visualisation de la simu. Si on en veut pas, on met false. Cela est permis par la fonction start en bas.
        team1 = SoccerTeam("expe1")
        team2 = SoccerTeam("expe2")
        self.strat = shoot()         # On donne la strat qu'on va utiliser.
        team1.add("jexp1", self.strat )
        team2.add("jplot",Strategy())  # Si besoin d'un joueur de team adverse
        self.simu = Simulation(team1,team2,max_steps=10000000) # On def la simu avec un enorme max_steps car on veut test x round et on veut pas devoir recommencer un match
        self.visu = visu
        self.simu.listeners+=self #ajout de l observer
        list_a = np.linspace(0.1,20,30)    # Creation de la matrice pour la parametre a. De param1 a param2 avec param2 valeurs
        list_b = np.linspace(0.1,20,30)
        self.list_params = [(a,b) for a in list_a for b in list_b]   # Creation de tout les couples possible
        self.cpt_params = 0     # Va permettre de tester toute la liste de couple de params
        self.nb_expe = 20       # Nb de round que l on fera par postion 
        self.res = dict()       # Ini de notre dico
        self.pos = dict()
    def begin_match(self,team1,team2,state):
    #initialisation des parametres ...
        self.last, self.but, self.expe = 0, 0, 0
    def begin_round(self,team1,team2,state):
        self.x,self.y = 4*GAME_WIDTH/7+random.uniform(0,1)*GAME_WIDTH/7,GAME_HEIGHT/4+random.uniform(0,1)*GAME_HEIGHT/4  # Ini des postions qu on voudra en depart, dans un secteur donne
        self.simu.state.states[(1,0)].position = Vector2D(self.x,self.y)
        self.simu.state.ball.position = Vector2D(self.x,self.y)
    #ou self.simu.set_state(state)
        self.strat.a,self.strat.b = self.list_params[self.cpt_params]  # On met les vals de a et b dans shoot que l on veut pour les couples dans list_params
        self.last = self.simu.step   # Pas a la fin du round precedant
    def update_round(self,team1,team2,state):
        if state.step>self.last+self.MAX_STEP: 
            self.simu.end_round()
    def end_round(self,team1,team2,state):
        if state.goal>0:    # Si but marque, on incremente but
            self.but+=1
        self.expe+=1        # On increment pour chaque round
        if self.expe > self.nb_expe:
            if self.cpt_params <len(self.list_params)-1:   # Si on a pas traite tout les couples 
                if self.but*1./self.expe > 0.5 :
                    self.res[self.list_params[self.cpt_params]]= self.but*1./self.expe  # On met dans res la proba
                    self.pos[self.list_params[self.cpt_params]]= self.x,self.y
                self.cpt_params+=1  # On change les params qu on va tester
                self.last, self.but, self.expe = 0, 0, 0    # On reinitialise
            else:
                self.simu.end_match()       # Sinon on end
    def start(self):
        if self.visu :
            show_simu(self.simu)
        else:
            self.simu.start()
                    
    
    
# Trouver parametre