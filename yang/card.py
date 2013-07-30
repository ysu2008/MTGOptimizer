from cost import Cost

class Card:
    def __init__(self, name, cost, isLand):
        self.cost = cost;
        self.isLand = isLand;
        self.name = name;

    def printCard(self):
        print self.name + " " + self.cost.toString();
