from soccersimulator import  SoccerAction
from soccersimulator import Vector2D
from soccersimulator.settings import *
import math


class MyState(object):
    def __init__(self,state,idteam,idplayer):
        self.state = state
        self.key = (idteam,idplayer)
        self.middle= Vector2D()
    
    @property
    def my_position(self):
        return self.state.player_state(self.key[0],self.key[1]).position
        #equivalent a self.player_state(self.key[0],self.key[1])
    @property    
    def ball_position(self):
        return self.state.ball.position
    
    @property
    def my_team(self):
        return self.key[0]
    @property
    def position_but_adv(self):
        if self.key[0]==1:
            return Vector2D(GAME_WIDTH,GAME_HEIGHT//2)
        else:
            return Vector2D(0,GAME_HEIGHT//2)


class Action(object):
    def __init__(self,mystate):
        self.state = mystate

    def petit_shoot_zone(self,p):
        return SoccerAction(Vector2D(0,0),(p-self.state.my_position).norm_max(1.9))
            
    @property
    def shoot_but_adv(self):
        return SoccerAction(Vector2D(0,0),self.state.position_but_adv-self.state.my_position)
        
        




def shootf(fct,mystate):
    return SoccerAction(Vector2D(),(mystate.position_but_adv-mystate.my_position).normalize()*fct)



def expf(a,b,x):
    return min(b*(1-math.exp(-a*x)),15)



class Shootameliorer(object):
    def __init__(self,mystate,dist_ball_but):
        self.state = mystate
        self.x=dist_ball_but
        
    @property
    def shoot(self):
        if(self.state.ball_position.distance(Vector2D(self.state.position_but_adv.x,self.state.ball_position.y))<=(1./7)*GAME_WIDTH/2):
            if self.state.ball_position.distance(Vector2D(self.state.ball_position.x,GAME_HEIGHT/2))<=(1./4)*GAME_HEIGHT:
                return shootf(expf(20,2.84,self.x),self.state)
            return shootf(expf(7.3,4.2,self.x),self.state)
        if(self.state.ball_position.distance(Vector2D(self.state.position_but_adv.x,self.state.ball_position.y))<=(2./7)*GAME_WIDTH/2):
            if self.state.ball_position.distance(Vector2D(self.state.ball_position.x,GAME_HEIGHT/2))<=(1/4)*GAME_HEIGHT:
                return shootf(expf(20,4.2,self.x),self.state)
            return shootf(expf(19.3,4.2,self.x),self.state)
        if(self.state.ball_position.distance(Vector2D(self.state.position_but_adv.x,self.state.ball_position.y))<=(3./7)*GAME_WIDTH/2) and self.state.ball_position.distance(Vector2D(self.state.ball_position.x,GAME_HEIGHT/2))<=(1./4)*GAME_HEIGHT:
            return shootf(expf(18.6,11.1,self.x),self.state)