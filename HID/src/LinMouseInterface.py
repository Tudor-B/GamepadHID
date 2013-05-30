'''
Created on May 12, 2013

@author: Tudor
'''
#from pymouse import PyMouse
#m=pyMouse
from subprocess import Popen, PIPE
class MouseInterface(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def keypress(self,sequence):
        p = Popen(['xte'], stdin=PIPE)
        p.communicate(input=sequence)
    
    def SetPosition(self, x, y):
        #m.move((x, y))
        self.keypress("mousemove " + x + " " + y + "\n")
        
    #def GetPosition(self):
        #return m.position()
    
    def ClickLeft(self):
        #     def Lclick(x, y):
        #x, y = self.GetPosition()
        #m.click(x,y,1)
        self.keypress("mouseclick " + str(1) + "\n")
         
    def ClickRight(self):
        #x, y = self.GetPosition()
        #m.click(x,y,2)
        self.keypress("mouseclick " + str(3) + "\n")
    
    def middleDown(self):
        self.keypress("mousedown " + str(2) + "\n")
        
    def middleUp(self):
        self.keypress("mouseup " + str(2) + "\n")
        
    def SetRelPos(self, dx, dy ):
        #x, y = self.GetPosition()
        #y = y+6*dy
        #x = x+6*dx
        #self.SetPosition(x, y)
        print "arguments recieved: " + str(dx) + " " + str(dy)
        self.keypress("mousermove " + str(dx) + " " + str(dy) + "\n")