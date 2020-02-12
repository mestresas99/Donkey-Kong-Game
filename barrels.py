import random

class Barrels:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.active = False
        self.speed = 1
        
        
    def moveBarrel(self): #add some movement for pauline not be be static
         if self.active==True:
            #setting the movement on the x-axis of the barrel on the platforms
            if(self.y==51 or self.y ==77 or self.y ==105 or self.y == 133 or self.y==161):
                self.x = self.x + self.speed
                if(self.y == 51 or self.y== 105 or self.y == 161):
                    self.speed= self.speed 
                elif(self.y == 77 or self.y== 133):
                    self.speed= - 1                  
            
            
            #setting the decrease of the barrel on the y-axis 
            #25% of chanche to go down throught a ladderç
            
            if(self.x == 209 and (self.y>=51 and self.y<77)):
                self.speed = 2
                self.y = self.y + self.speed
                
            elif(self.x == 195 and (self.y>=51 and self.y<77)):
                a = random.randrange(1,5)
                if (a == 3):
                    self.speed = 1
                    self.y = self.y + self.speed
            
            elif(self.x == 148 and (self.y>=77 and self.y<105)):
                a = random.randrange(1,5)
                if (a == 3):
                    self.speed = 1
                    self.y = self.y + self.speed
                    
            elif(self.x == 38 and (self.y>=77 and self.y<105)):
                a = random.randrange(1,5)
                if (a == 3):
                    self.speed = 1
                    self.y = self.y + self.speed
            
            elif(self.x == 25 and (self.y>=77 and self.y<105)):
                self.speed = 1
                self.y = self.y + self.speed
                
            elif(self.x == 83 and (self.y>=105 and self.y<133)):
                a = random.randrange(1,5)
                if (a == 3):
                    self.speed = 1
                    self.y = self.y + self.speed
                
            elif(self.x == 209 and (self.y>=105 and self.y<133)):
                self.speed = 1
                self.y = self.y + self.speed
             
            elif(self.x == 108 and (self.y>=133 and self.y<161)):
                a = random.randrange(1,5)
                if (a == 3):
                    self.speed = 1
                    self.y = self.y + self.speed
                    
            elif(self.x == 25 and (self.y>=133 and self.y<161)):
                self.speed = 1
                self.y = self.y + self.speed
                
            #return to initial value 
            elif(self.x==231 and self.y==161):
                self.speed = 1
            
            elif(self.x==229 and self.y==161):
                self.x = 70
                self.y = 51
                self.active = False
                
                
            
          
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                