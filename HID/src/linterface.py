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
        elif action.find('Left mouse') != -1:
            self.keypress('mouse' + updown + " " + str(1) + "\n")
        elif action.find('Right mouse') != -1:
            self.keypress('mouse' + updown + " " + str(3) + "\n")
        elif action.find('Middle mouse') != -1:
            self.keypress('mouse' + updown + " " + str(2) + "\n")
        pass
    def SetRelPos(self, dx, dy ):
        print "arguments recieved: " + str(dx) + " " + str(dy)
        self.keypress("mousermove " + str(dx) + " " + str(dy) + "\n")