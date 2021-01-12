##type of units
###base
####able to see in a radius
####interact with other units

###todo learning system
###complex units will have misc. stats (hunger, energy, etc)
###they will interact with other units and learn which stat thoes units affect
###act accordingly to stats needed

###stats system
###stat
####value
####decrement rate
####increment rate
####minimal value
####minimal value danger threshold
####max value
####max value danger threshold

class Unit():
    def __init__(self, x = 0, y = 0, icon="*"):
        self.x = x
        self.y = y
        self.icon = icon
        self.board = None
        self.knowledge = [Unit] #list of units found in board

    def behavior(self):
        #sequence of action the unit makes by default
        self.action()

    def perception(self):
        #Read board gets information
        pass

    def action(self):
        #do something with any information that the unit has
        pass

    def interaction(self, other:Unit):
        #do something with the unit selected
        pass

    def moveByCoord(self, x, y):
        #move unit
        pass

    def moveByUnit(self, x, y):
        pass

    def moveByInformation(self, index):
        #move to the position closest to unit selected from knowledge
        pass

    def added(self, board):
        self.board = board

    #todo
    ##senses
    ##knowledge
    ##

    def __str__(self):
        return self.icon

class gameoflifeUnit(Unit):
    def __init__(self, x=0, y=0, icon='*'):
        super().__init__(x=x, y=y, icon=icon)
        self.alive = False #alive icon #, dead icon *

    def perception(self):
        
        #read all adjacent spaces
        #save in knowledge
        pass

    def action(self):
        #act according do GOL rules
        pass



def addUnit(board, unit:Unit):
    posx = unit.x
    posy = unit.y
    if board.get((posx, posy), "") == "":
        board[(posx, posy)] = unit

def initBoard(length:tuple):
    board["length"] = length

def printBoard(board):
    for x in range(board["length"][0]):
        print("| ", end="")
        for y in range(board["length"][1]):
            print(board.get((x,y), " "), end=" | ")
        print()

board = {}

if __name__ == "__main__":
    initBoard((5,5))
    u = Unit(0,0)
    addUnit(board, u)
    printBoard(board)