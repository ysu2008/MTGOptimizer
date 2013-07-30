class Cost:
    def __init__(self, red, white, blue, green, black, colorless):
        self.red = red;
        self.white = white;
        self.blue = blue;
        self.green = green;
        self.black = black;
        self.colorless = colorless;

    def toString(self):
        string = "";
        for i in range(self.red):
            string += "R";
        for i in range(self.white):
            string += "W";
        for i in range(self.blue):
            string += "U";
        for i in range(self.green):
            string += "G";
        for i in range(self.black):
            string += "B";
        string += str(self.colorless)
        return string;
