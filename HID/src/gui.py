'''
Created on May 8, 2013

@author: mads
'''
import easygui as eg

class gui():
    def __init__(self,remapper='derp'):
        self.remapper = remapper
    
    def Menu(self):
        image   = "Gamepad.gif"
        msg     = "Gamepad Info"
        choices = ["Back","Change buttons","Info(Not implemented)"]
        reply   = eg.buttonbox(msg,image=image,choices=choices)
        
        print ("You wanted to:", reply) 
        
        if reply == choices[0]:
            pass
        if reply == choices[1]:
            but, act = self.changefunc()
            print but, act
            self.remapper.mapAction(but,act)
        if reply == choices[2]:
            pass
    
    def changefunc(self):
    
        image   = "Gamepad.gif"
        msg     = "Button Config?"
        choices = ["cross", "circle", "square", "triangle"]
        choiceBot   = eg.buttonbox(msg,image=image,choices=choices)
        
        image   = "Gamepad.gif"
        msg     = "Function Change"
        choices = ["Alt","Tab","Esc","Left mouse","Right mouse" , "Middle mouse"]
        choiceAct   = eg.buttonbox(msg,image=image,choices=choices)
        
        print ("You have now changed the button to:", choiceBot)
        print ("You have specified that function to be:", choiceAct)
        
        return choiceBot, choiceAct