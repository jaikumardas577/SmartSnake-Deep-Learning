import random
import math



class Board:
    def __init__(self,length = 20,breadth = 20,originX = 0,originY = 0):
        self._length = length
        self._breadth = breadth
        self._originX = originX
        self._originY = originY
        self._level = 0
    
    @property
    def getLength(self):
        return self._length

    @property
    def getbreath(self):
        return self._breadth

    @property
    def getOriginX(self):
        return self._originX

    @property        
    def getOriginY(self):
        return self._originX


    def __repr__(self):
        return f"<Board ({self.getLength},{self.getbreath},{self.getOriginX},{self.getOriginY})>"



class Food:
    def __init__(self,board_obj):
        self._posX = random.randint(board_obj.getOriginX + 1,board_obj.getLength -2 )        
        self._posY = random.randint(board_obj.getOriginY + 1,board_obj.getbreath -2)

    @property
    def getPosx(self):
        return self._posX

    @property
    def getPosY(self):
        return self._posY

    def __repr__(self):
        return f"<Food ({self._posX},{self._posY})>"




# """ 
#            l3
#       ==================
#  l4   |                 |
#       |                 |  l2
#       |                 |
#        =================
#         l1
# """




class Snake:
    def __init__(self,board_obj):
        self._posX = random.randint(board_obj.getOriginX + 1 ,board_obj.getLength -2 )        
        self._posY = random.randint(board_obj.getOriginY + 1,board_obj.getbreath -2 )
        self._length = 1
    
    @property
    def getPosx(self):
        return self._posX

    @property
    def getPosY(self):
        return self._posY
    
    @property
    def moveLeft(self):
        self._posX = self._posX - 1
        return self._posX

    @property
    def moveRight(self):
        self._posX = self._posX + 1
        return self._posX

    @property
    def moveDown(self):
        self._posY = self._posY + 1
        return self._posY

    @property
    def moveUp(self):
        self._posY = self._posY - 1
        return self._posY

    def getL1(self,board_obj):
        return (self._posY - board_obj.getOriginY)/board_obj.getLength

    def getL2(self,board_obj):
        return (board_obj.getbreath - self._posX)/board_obj.getbreath

    def getL3(self,board_obj):
        return (board_obj.getLength - self._posY)/board_obj.getbreath

    def getL4(self,board_obj):
        return (self._posX - board_obj.getOriginX)/board_obj.getLength
    
    def getGradient1(self,foodObj):
        if foodObj.getPosx - self.getPosx == 0 :
            return 0
        return (foodObj.getPosY - self.getPosY)/(foodObj.getPosx - self.getPosx)
    def oreintation(self,foodObj):
        # returning 1 for UP and -1 for Down and 0 for coincide 
        if self.getPosY - foodObj.getPosY  > 0 :
            return 1
        elif self.getPosY - foodObj.getPosY  < 0:
            return -1
        else:
            return 0
    def getDistance(self,foodObj,board_obj):
        try:
            dist =  math.hypot((self.getPosx - foodObj.getPosx)/board_obj.getLength,(self.getPosY - foodObj.getPosY)/board_obj.getLength)
        except ZeroDivisionError:
            return 0
        return dist

    def __repr__(self):
        return f"<Snake ({self._posX},{self._posY},{self._length})>"



    








