'''
Created on May 1, 2013

@author: Tudor
'''

import win32api, win32con, pygame

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
        win32api.SetCursorPos((x, y))
        
    def GetPosition(self):
        return win32api.GetCursorPos()
    
    def Click_Up(self,argument):
        
        x, y = self.GetPosition()
        if argument == 'left':
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x, y)
        elif argument == 'right':
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x, y)
        
    def Click_Down(self,argument):
        x, y= self.GetPosition()
        if argument == 'left':
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x, y)
        elif argument == 'right':
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x, y)
        
    def SetRelPos(self, dx, dy ):
        x, y = self.GetPosition()
        y = y+6*dy
        x = x+6*dx
        self.SetPosition(x, y)