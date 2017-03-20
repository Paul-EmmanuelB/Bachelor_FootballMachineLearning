from soccersimulator import settings,SoccerTeam, Simulation, show_simu, KeyboardStrategy, SoccerAction
from soccersimulator import Strategy, SoccerAction, Vector2D, load_jsonz,dump_jsonz,Vector2D
import logging
from arbre_utils import build_apprentissage,affiche_arbre,DTreeStrategy,apprend_arbre,genere_dot
from sklearn.tree 	import export_graphviz
from sklearn.tree import DecisionTreeClassifier
import os.path



from strat import ElStrategy, ElDefenseur, ElLooser
from toolbox import MyState, Action, Shootameliorer
from soccersimulator import Strategy
from soccersimulator import SoccerAction
from soccersimulator import Vector2D
from soccersimulator.settings import *


class GenStrat(Strategy):
    def __init__(self,fun):
        self.fun = fun
        self.name = fun.__name__
    def compute_strategy(self,state,id_team,id_player):
        return self.fun(MyState(state,id_team,id_player))
    

def apprentissage(fn):
    ### chargement d'un fichier sauvegarder
    states_tuple = load_jsonz(fn)
    ## Apprentissage de l'arbre
    data_train, data_labels = build_apprentissage(states_tuple,my_get_features)
    dt = apprend_arbre(data_train,data_labels,depth=10)
    # Visualisation de l'arbre
    affiche_arbre(dt)
    genere_dot(dt,"test_arbre.dot")
    return dt


