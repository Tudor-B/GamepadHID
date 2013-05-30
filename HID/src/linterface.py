from subprocess import Popen, PIPE

class Interface(object):
    def keypress(self,sequence):
        p = Popen(['xte'], stdin=PIPE)
        p.communicate(input=sequence)
    #all keyup/down sequences need to be ended with \n !!!
    def genEvent(self,action,updown):
        if action.find('None') == 0:
            pass
        elif action.find('mouse') == -1:
            self.keypress('key' + updown + " " + action + "\n")
            pass
        pass
