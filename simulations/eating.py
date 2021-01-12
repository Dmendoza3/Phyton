#Unit types: carnivore, herbivore, plant
#Unit actions: search for food, eat, sleep, reproduce
#Unit stats: Hunger(0-100), Sleep(0-100), Survivavility(based of population)
#Reduce stats by step, Reproduce world by step

class unit:
    def __init__(self, name = "nameless"):
        self.name = name
        self.x = 0.0
        self.y = 0.0
    
    def __str__(self):
        return "unit x = " + str(self.x) + " y = " + str(self.y)

class environment:
    def __init__(self, width = 10, height = 10):
        self.table = []

    def printTable(self):
        for u in table:
            pass
    
    def addUnit(self):
        self.table.append(unit("unit " + str(len(self.table))))

    def __str__(self):
        rstr = "["
        for x in self.table:
            rstr = rstr + str(x) + ", "
        rstr = rstr[:len(rstr) - 2] + "]"
        return rstr

env = environment()
x = unit()
env.table.append(unit())
env.table.append(unit())
env.table.append(unit())

env.table[0].x = 1.5
env.table[0].y = 1.5
env.table[1].x = 2.5
env.table[1].y = 2.5
env.table[2].x = 3.5
env.table[2].y = 3.5



