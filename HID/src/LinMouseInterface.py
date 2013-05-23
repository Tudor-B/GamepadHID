'''
Created on May 12, 2013

@author: Tudor
'''
from pymouse import PyMouse
m=pyMouse
class MouseInterface(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def SetPosition(self, x, y):
        m.move((x, y))
        
    def GetPosition(self):
        return m.position()
    
    def Click_Up(self,argument):
        #     def Lclick(x, y):
        x, y = self.GetPosition()
        if argument == "left":
        
        elif argument =="right":
         
    def Click_Down(self,argument):
        x, y = self.GetPosition()
        if argument == "left":
        
        elif argument =="right":
        
    def SetRelPos(self, dx, dy ):
        x, y = self.GetPosition()
        y = y+6*dy
        x = x+6*dx
        self.SetPosition(x, y)