'''
Created on May 12, 2013

@author: Tudor
'''
from evdev import uinput, ecodes as e
from subprocess import Popen, PIPE

ui = uinput.UInput()
class KBInterface(object):
    ui = uinput.UInput()
    def keypress(self,sequence):
        p = Popen(['xte'], stdin=PIPE)
        p.communicate(input=sequence)
    #all keyup/down sequences need to be ended with \n !!!
    def KeyUp_Down(self):
        self.keypress('''keydown Up\n''')
        pass
    def KeyUp_Up(self):
        self.keypress('''keyup Up\n''')
        pass
    def KeyDown_Down(self):
        self.keypress('''keydown Down\n''')
        pass
    def KeyDown_Up(self):
        self.keypress('''keyup Down\n''')
        pass
    def KeyLeft_Down(self):
        self.keypress('''keydown Left\n''')
        pass
    def KeyLeft_Up(self):
        self.keypress('''keyup Left\n''')
        pass
    def KeyRight_Down(self):
        self.keypress('''keydown Right\n''')
        pass
    def KeyRight_Up(self):
        self.keypress('''keyup Right\n''')
        pass
    pass
