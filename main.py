#Main
import pyxel
import constants
from player import Mario
from pauline import Pauline
from barrels import Barrels
class Game:

    def __init__(self):
        self.Mario = Mario(constants.MARIO_X, constants.MARIO_Y, constants.LIVES)
        self.Pauline = Pauline(constants.PAU_X, constants.PAU_Y)
        self.blist = []
        for i in range(7):
            self.Barrels = Barrels(constants.BAR_X, constants.BAR_Y)
            self.blist.append(self.Barrels)
        self.punt = 0
        self.counter = 0
        
    def run(self): 
        # The first thing to do is to create the screen, see API for more parameters
        pyxel.init(constants.WIDTH, constants.HEIGHT, caption=constants.CAPTION)
        # Loading the pyxres file, it has a 16x16 cat in (0,0) in bank 0
        pyxel.load("assets/gameboard.pyxres")
        # To start the game we invoke the run method with the update and draw functions
        pyxel.run(self.update, self.draw)

    # To use pyxel we need to define two functions, one will do all the
    # calculations needed each frame, the other will paint things on the screen
    # They can have any name, but the 'standard' ones are update and draw
    def update(self):
        ''' This function is executed every frame. Now it only checks if the user
        pressed E to finish'''
        if pyxel.btnp(pyxel.KEY_E) or self.Mario.lives==0 or self.Mario.y == self.Pauline.y:
            print('GAME OVER')
            pyxel.quit()
        else:
            self.counter = self.counter + 1
            self.moveMario()
            self.movePauline()
            self.moveBarrels()
            self.puntuations()

    def draw(self):
        ''' This function draws graphics from the image bank'''
        pyxel.cls(0)
        # Loading images from the image bank 0

        pyxel.blt(constants.DK_X, constants.DK_Y, 0, 50, 15, 40, 33)
        
        pyxel.blt(self.Pauline.x, self.Pauline.y, 0, 0, 48, 15, 30)
          
        #Barrels decoration
        pyxel.blt(constants.BAR1_X, constants.BAR1_Y,1, 0, 0, 23,50) 
        
        #putting two platforms PER LINE, total 5 lines of platforms
        pyxel.blt(constants.PLAT_X, constants.PLAT_Y, 1, 0, 49, 260, 20)
        pyxel.blt(constants.PLAT_X1, constants.PLAT_Y1, 1, 30, 49, 120, 20)
        
        pyxel.blt(constants.PLAT_X2, constants.PLAT_Y2, 1, 30, 49, 260, 20)
        pyxel.blt(constants.PLAT_X22, constants.PLAT_Y22, 1, 0, 49, 120, 20)
        
        pyxel.blt(constants.PLAT_X3, constants.PLAT_Y3, 1, 0, 49, 260, 20)
        pyxel.blt(constants.PLAT_X33, constants.PLAT_Y33, 1, 30, 49, 100, 20)
        
        pyxel.blt(constants.PLAT_X4, constants.PLAT_Y4, 1, 30, 49, 260, 20)
        pyxel.blt(constants.PLAT_X44, constants.PLAT_Y44, 1, 0, 49, 120, 20)
        
        pyxel.blt(constants.PLAT_X5, constants.PLAT_Y5, 1, 0, 49, 260, 20)
        pyxel.blt(constants.PLAT_X55, constants.PLAT_Y55, 1, 30, 49, 100, 20)
        
        pyxel.blt(constants.PLAT_X6, constants.PLAT_Y6, 1, 0, 49, 65, 20)
          
        #this for the barrels
        #for i in self.blist:
        self.blist[0].active = True                
        if self.blist[0].active == True:
            if pyxel.frame_count%4: #we change the image of the barrel in order to look like the barrel is rotating
                pyxel.blt(self.blist[0].x,self.blist[0].y,1, 23, 0, 16, 15)
            else:
                pyxel.blt(self.blist[0].x,self.blist[0].y,1, 39, 0, 16, 15)
                             
        self.blist[1].active = True                
        if self.blist[1].active == True:
            if pyxel.frame_count%4: #we change the image of the barrel in order to look like the barrel is rotating
                pyxel.blt(self.blist[1].x,self.blist[1].y,1, 23, 0, 16, 15)
            else:
                pyxel.blt(self.blist[1].x,self.blist[1].y,1, 39, 0, 16, 15) 
            
        self.blist[2].active = True                
        if self.blist[2].active == True:
            if pyxel.frame_count%4: #we change the image of the barrel in order to look like the barrel is rotating
                pyxel.blt(self.blist[2].x,self.blist[2].y,1, 23, 0, 16, 15)
            else:
                pyxel.blt(self.blist[2].x,self.blist[2].y,1, 39, 0, 16, 15) 
                
        self.blist[3].active = True                
        if self.blist[3].active == True:
            if pyxel.frame_count%4: #we change the image of the barrel in order to look like the barrel is rotating
                pyxel.blt(self.blist[3].x,self.blist[3].y,1, 23, 0, 16, 15)
            else:
                pyxel.blt(self.blist[3].x,self.blist[3].y,1, 39, 0, 16, 15) 
        
        self.blist[4].active = True                
        if self.blist[4].active == True:
            if pyxel.frame_count%4: #we change the image of the barrel in order to look like the barrel is rotating
                pyxel.blt(self.blist[4].x,self.blist[4].y,1, 23, 0, 16, 15)
            else:
                pyxel.blt(self.blist[4].x,self.blist[4].y,1, 39, 0, 16, 15) 
                
        self.blist[5].active = True                
        if self.blist[5].active == True:
            if pyxel.frame_count%4: #we change the image of the barrel in order to look like the barrel is rotating
                pyxel.blt(self.blist[5].x,self.blist[5].y,1, 23, 0, 16, 15)
            else:
                pyxel.blt(self.blist[5].x,self.blist[5].y,1, 39, 0, 16, 15) 
            
       # pyxel.blt(constants.BAR_X, constants.BAR_Y,1,23,0,16,15) #static barrel just for decoration     
            
        #Stairs
        pyxel.blt(constants.S1X, constants.S1Y, 1, 0, 30, 6, 30)
        pyxel.blt(constants.S2X, constants.S2Y, 1, 0, 30, 6, 30)
        pyxel.blt(constants.S3X, constants.S3Y, 1, 0, 30, 6, 30)
        pyxel.blt(constants.S4X, constants.S4Y, 1, 0, 30, 6, 30)
        pyxel.blt(constants.S5X, constants.S5Y, 1, 0, 30, 6, 30)
        pyxel.blt(constants.S6X, constants.S6Y, 1, 0, 30, 6, 30)
           
        #animation of mario while moving
        if  pyxel.btn(pyxel.KEY_RIGHT):
            pyxel.blt(self.Mario.x,self.Mario.y,0,53,0,12,15)
       
        elif pyxel.btn(pyxel.KEY_LEFT):
            pyxel.blt(self.Mario.x,self.Mario.y,0,32,0,12,15)
        
        elif pyxel.btn(pyxel.KEY_UP):
            pyxel.blt(self.Mario.x,self.Mario.y,0,32,0,12,15)
        
        elif pyxel.btn(pyxel.KEY_DOWN):
            pyxel.blt(self.Mario.x,self.Mario.y,0,32,0,12,15)
        else:
            pyxel.blt(self.Mario.x,self.Mario.y,0,0 ,0,12,15)        
    
        #PUNTUATIONS AND TITLE
        #high score
        pyxel.text(100, 0, "DONKEY KONG",4)
        #actual score
        pyxel.text(20, 0, "SC0RE:",8)
        pyxel.text(20, 10,str(self.punt),7)
        #level
        pyxel.text(205, 10, "LEVEL=01",1)
        #bonus with the rectangles cover the title
        pyxel.rectb(199, 36, 26, 8, 8)
        pyxel.text(202, 30, "LIVES",8)
        pyxel.rectb(197, 28, 30, 17, 7)
        pyxel.text(210, 37,str(self.Mario.lives),7)
        
    def moveMario(self):
        d = None
        if pyxel.btn(pyxel.KEY_RIGHT):
            d='right'
        elif pyxel.btn(pyxel.KEY_LEFT):
            d = 'left'
        elif pyxel.btn(pyxel.KEY_UP):
            d='up'
        elif pyxel.btn(pyxel.KEY_DOWN):
            d='down'
        elif pyxel.btn(pyxel.KEY_SPACE):
            d='jump'
        
       #setting the movements of mario for each platform 
        if self.Mario.y <= 165 and self.Mario.y>=140:
            self.Mario.move(d,constants.PLAT_X,constants.PLAT_Y)
       
        if self.Mario.y <= 140 and self.Mario.y>=115:
            self.Mario.move(d,constants.PLAT_X2,constants.PLAT_Y2)
       
        if self.Mario.y <= 115 and self.Mario.y>=90:
            self.Mario.move(d,constants.PLAT_X3,constants.PLAT_Y3)
        
        if self.Mario.y <= 90 and self.Mario.y>=60:
            self.Mario.move(d,constants.PLAT_X4,constants.PLAT_Y4)
        
        if self.Mario.y <= 60 and self.Mario.y>=35:
            self.Mario.move(d,constants.PLAT_X5,constants.PLAT_Y5)
        
        if self.Mario.y <= 35 and self.Mario.y>=5:
            self.Mario.move(d,constants.PLAT_X6,constants.PLAT_Y6)
        
    def movePauline(self):
        self.Pauline.movepau()   

    def moveBarrels(self):
      self.blist[0].moveBarrel()
      if (self.counter>=150):
           self.blist[1].moveBarrel()
      if(self.counter>=350):
           self.blist[2].moveBarrel()
      if(self.counter>=500):
           self.blist[3].moveBarrel()
      if(self.counter>=600):
           self.blist[4].moveBarrel()
      if(self.counter>=750):
           self.blist[5].moveBarrel()
    
    #puntuations system              
    def puntuations(self):
        #increasing puntuation:
        for i in self.blist:
            rest = i.y - self.Mario.y
            if(self.Mario.x == i.x and rest>5 and rest<=20):
                self.punt += 100
                print(self.punt)
                
            #modifiyng the lives of mario when the barrels and mario reach same positon
            elif(self.Mario.x == i.x and rest>=0 and rest<=5):
                self.Mario.lives =self.Mario.lives - 1
                print(self.Mario.lives)
                
################# main program ##################


game = Game()
game.run()






