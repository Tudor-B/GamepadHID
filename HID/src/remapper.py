class remapper():
    buttons = {}
    actions = {}
    
    def __init__(self, name):
        self.name = name
        self.layout = 'default'
        self.buttons = self.readButtons(name)
        self.actions = self.readActions('default')
        pass
    
    def readButtons(self, filename):
        f = open(filename + '.txt')
        buttons = {}
        for line in f:
            line = line.split()
            buttons[line[0]] = int(line[1])
        return buttons
    
    def writeButtons(self, filename):
        f = open(filename + '.txt','w')
        buttons = self.buttons
        for button in buttons:
            f.write(button + ' ' + str(buttons.get(button)) + '\n')
    
    def readActions(self, filename):
        f = open(filename + '.txt')
        actions = {}
        for line in f:
            line = line.split(None,1)
            actions[line[0]] = line[1]
        return actions
    
    def writeActions(self, filename):
        f = open(filename + '.txt','w')
        actions = self.actions
        for button in actions:
            f.write(button + ' ' + actions.get(button))
    
    def mapButton(self,button,ID):
        self.buttons[button] = ID
        pass
    
    def mapAction(self,button,action):
        self.actions[button] = action
        pass