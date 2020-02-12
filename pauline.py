#from player import Mario


class Pauline:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.speed = 1
        
    def movepau(self): #add some movement for pauline not be be static
        #stop = False
        #while(stop!=True):
        #start in x = 140
        self.x = self.x + self.speed
        if(self.x<=100 or self.x>=140):
            self.speed = - self.speed  
            
            #if(Mario.x == self.Pauline.x and Mario.y == self.Pauline.y):
             #   stop = True
            #else:
             #   stop = False
    