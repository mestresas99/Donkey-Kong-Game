

class Mario:

    
    def __init__(self,x,y,live):
        self.x = x
        self.y = y
        self.lives = live
        self.yspeed=0
    
        
        
    def move(self,d,px,py):
        
                 
        #setting limits for the movement of mario       
        if self.x == 210:
            self.x = 209
        elif self.x == 19:
            self.x = 20
        elif self.y == 161:
            self.y = 160
        elif self.y == 22:
            self.y = 23
        
        
        
        if d == 'right':
            
                        #setting the botton right
            if(self.x>=104 and self.x<=111 and self.y<=158 and self.y>133):
                self.x = self.x
            elif(self.x>=81 and self.x<=88 and self.y<=129 and self.y>105):
                self.x = self.x 
            elif(self.x>=144 and self.x<=151 and self.y<=103 and self.y>77):
                self.x = self.x
            elif(self.x>=14 and self.x<=21 and self.y<=103 and self.y>77):
                self.x = self.x 
            elif(self.x>=194 and self.x<=201 and self.y<=75 and self.y>51):
                self.x = self.x
            elif(self.x>=89 and self.x<=96 and self.y<=50 and self.y>25):
                self.x = self.x
            else:
                self.x = self.x + 1
               
        elif d == 'left':
                                    #setting the botton left
            if(self.x>=104 and self.x<=111 and self.y<=158 and self.y>133):
                self.x = self.x
            elif(self.x>=81 and self.x<=88 and self.y<=129 and self.y>105):
                self.x = self.x 
            elif(self.x>=144 and self.x<=151 and self.y<=103 and self.y>77):
                self.x = self.x
            elif(self.x>=14 and self.x<=21 and self.y<=103 and self.y>77):
                self.x = self.x 
            elif(self.x>=194 and self.x<=201 and self.y<=75 and self.y>51):
                self.x = self.x
            elif(self.x>=89 and self.x<=96 and self.y<=50 and self.y>25):
                self.x = self.x
            else:
                self.x = self.x - 1
            
        elif d == 'up':
            
            #setting the botton up, just in case there is a stair you can use this botton
            if(self.x>=104 and self.x<=111 and self.y<=162 and self.y>133):
                self.y = self.y - 1
            elif(self.x>=81 and self.x<=88 and self.y<=133 and self.y>105):
                self.y = self.y - 1
            elif(self.x>=144 and self.x<=151 and self.y<=105 and self.y>77):
                self.y = self.y - 1
            elif(self.x>=34 and self.x<=41 and self.y<=105 and self.y>77):
                self.y = self.y - 1
            elif(self.x>=194 and self.x<=201 and self.y<=77 and self.y>51):
                self.y = self.y - 1
            elif(self.x>=89 and self.x<=96 and self.y<=52 and self.y>25):
                self.y = self.y - 1
            else:
                self.y = self.y
     
               
                          
        elif d == 'down':
            #setting the botton down, just in case there is a stair you can use this botton
            if(self.x>=104 and self.x<=111 and self.y<=162 and self.y>130):
                self.y = self.y + 1
            elif(self.x>=81 and self.x<=88 and self.y<=130 and self.y>103):
                self.y = self.y + 1
            elif(self.x>=144 and self.x<=151 and self.y<=103 and self.y>75):
                self.y = self.y + 1
            elif(self.x>=34 and self.x<=41 and self.y<=103 and self.y>75):
                self.y = self.y + 1
            elif(self.x>=194 and self.x<=201 and self.y<=75 and self.y>49):
                self.y = self.y + 1
            elif(self.x>=89 and self.x<=96 and self.y<=49 and self.y>23):
                self.y = self.y + 1
            else:
                self.y = self.y
            
            
        
        elif d == 'jump' and self.colliding(px,py):
            self.yspeed= -5; #all the y´s moving in the jump
            

        if(not self.colliding(px,py)):
            self.yspeed+=1
        elif(self.colliding(px,py) and d!='jump'):
            self.y-=self.yspeed
            self.yspeed==0;
         #appliying the 'gravity' in all the places minus the ladders   
        if (self.x>=104 and self.x<=111 and self.y<=162 and self.y>133):
            self.y = self.y
        elif(self.x>=81 and self.x<=87 and self.y<=133 and self.y>105):
            self.y = self.y
        elif(self.x>=144 and self.x<=151 and self.y<=105 and self.y>77):
            self.y = self.y
        elif(self.x>=34 and self.x<=41 and self.y<=105 and self.y>77):
            self.y = self.y
        elif(self.x>=194 and self.x<=201 and self.y<=77 and self.y>50):
            self.y = self.y
        elif(self.x>=89 and self.x<=96 and self.y<=50 and self.y>25):
            self.y = self.y
        else:
            self.y+=self.yspeed 
         
     #this method is acting like gravity in the game          
    def colliding(self,px,py):
        if(abs(self.y-py)<18) :
            return True
        else:
            return False 
        
            
            
            
            
            
            
            
            
            
            
            
            