import random
class RPSai:
    def __init__(self):
        self.history = []
        self.bestMove = ""

    def opponentMove(self,move):
        self.move = move
        if self.move == "R" or self.move == "P" or self.move == "S":
            self.history.append(self.move)
        else:
            print("ERROR")

    def beatMove(self,beat):
        self.beat = beat
        if self.beat == "R":
            return "P"
        if self.beat == "P":
            return "S"
        if self.beat == "S":
            return "R"

    def predictMove(self):
        freq = {}
        val = []
        key = []
        maxVal = -1
        maxMove = ""
        for i in range(len(self.history)):
            if self.history[i] in freq:
                freq[self.history[i]] += 1
            else:
                freq[self.history[i]] = 1
        for i in freq.values():
            val.append(i)
        for i in freq.keys():
            key.append(i)
        for i in range(len(val)):
            if val[i] > maxVal:
                maxVal = val[i]
                maxMove = key[i]
        self.bestMove = maxMove
        return maxMove

    def playMove(self):
        self.predictMove()
        if self.bestMove == "R":
            return "P"
        if self.bestMove == "P":
            return "S"
        if self.bestMove == "S":
            return "R"
        
            
    def playMovePro(self):
        moves = ""
        output = ""
        count = 0
        for i in range(len(self.history)):
            if self.move == "":
                output = random.choice(["R","P","S"])
            elif self.history[-3:] == ["R","R","R"]:
                output = "P"
            elif self.history[-3:] == ["S","S","S"]:
                output = "R"
            elif self.history[-3:] == ["P","P","P"]:
                output = "S"
            elif self.history[-3:] == ["R","S","P"]:
                if count%3 == 2:
                    output = "S"
                if count%3 == 1:
                    output = "R"
                if count%3 == 0:
                    output = "P"
            elif self.history[-3:] == ["S","P","R"]:
                if count%3 == 2:
                    output = "R"
                if count%3 == 1:
                    output = "P"
                if count%3 == 0:
                    output = "S"
            elif self.history[-3:] == ["P","R","S"]:
                if count%3 == 2:
                    output = "P"
                if count%3 == 1:
                    output = "S"
                if count%3 == 0:
                    output = "R"
            else:
                if self.move == "R":
                    output = random.choice(["R","P"])
                elif self.move == "P":
                    output = random.choice(["P","S"])
                elif self.move == "S":
                    output = random.choice(["R","S"])
                else:
                    output = random.choice(["R","P","S"])
            count += 1
        return output
            
    def __repr__(self):
        return "%s"%(self.history,self.bestMove,self.move)
