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
    def milieu_terrain(self):
        return Vector2D(GAME_WIDTH/2,GAME_HEIGHT/2)
    @property    
    def ball_vitesse(self):
        return self.state.ball.vitesse
    @property
    def position_but_adv(self):
        if self.key[0]==1:
            return Vector2D(GAME_WIDTH,GAME_HEIGHT//2)
        else:
            return Vector2D(0,GAME_HEIGHT//2)
    @property
    def position_mon_but(self):
        if self.key[0]==1:
            return Vector2D(0,GAME_HEIGHT//2)
        else:
            return Vector2D(GAME_WIDTH,GAME_HEIGHT//2)

    def dist_player(self,p):
        return p.distance(self.my_position)
    
    @property
    def joueur_plus_proche(self):
        dmin=175
        for L in self.state.players :
            if L[0]==self.key[0] and L[1]!=self.key[1] and dmin>self.dist_player(state.player_state(L[0],L[1]).position) :
                dmin=self.dist_player(self.state.player_state(L[0],L[1]).position)
                player_proche=L
        return player_proche
    
    @property
    def joueurplusProche(self):
        dmin=0
        x=[(idt,idp) for idt,idp in self.state.players if idt == self.key[0] and idp != self.key[1]]
        dmin=x[0][1]
        # i=1
        # for i in x:
        # if(x[i]<dmin):
            # dmin=x[min]
        return self.state.player_state(x[0][0],x[0][1]).position

    @property
    def joueurAdv_plusProche(self):
        x=[(idp, self.my_position.distance(self.state.player_state(idt, idp).position)) for idt,idp in self.state.players if idt != self.key[0]]
        dmin = x[0][1]
        pmin = 0
        for idp, dist in x:
            if(dist<dmin):
                dmin=dist
                pmin = idp
        return self.state.player_state(3-self.key[0], pmin).position
    
    
class Action(object):
    def __init__(self,mystate):
        self.state = mystate
    def sprint(self,p):
        return SoccerAction(p-self.state.my_position,self.state.middle)
    
    def shoot(self,p):
        return SoccerAction(self.state.middle,p-self.state.my_position)

    @property
    def shoot_but_adv(self):
        return SoccerAction(Vector2D(0,0),self.state.position_but_adv-self.state.my_position)

    @property
    def petit_shoot_but_adv(self):
        return SoccerAction(Vector2D(0,0),(self.state.position_but_adv-self.state.my_position).norm_max(1.9))

    @property
    def petit_shoot_joueur_proche(self):
        return SoccerAction(Vector2D(0,0),(self.state.joueurplusProche-self.state.my_position).norm_max(5.5))

    @property
    def aller_vers_ball(self):
        return SoccerAction((self.state.ball_position-self.state.my_position,Vector2D(0,0)))

    @property
    def aller_vers_jApP(self):
        return SoccerAction(self.state.joueurplusProche-self.state.my_position,Vector2D(0,0))
        















def expf(a,b,x):
    return min(b*(1-math.exp(-a*x)),15)

def shootf(fct,mystate):
    return SoccerAction(Vector2D(),(mystate.position_but_adv-mystate.my_position).normalize()*fct)







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
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        