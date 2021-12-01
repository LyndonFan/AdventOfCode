from copy import *

f = open("2020/22.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n\n")]

decks = []
for p in arr:
    p = p.split("\n")[1:]
    decks.append([int(x) for x in p])

# while len(decks[0])*len(decks[1])>0:
#     a,b = decks[0].pop(0), decks[1].pop(0)
#     if a>b:
#         decks[0] += [a,b]
#     else:
#         decks[1] += [b,a]

# score = 0
# winner = int(len(decks[0])==0)
# n = len(decks[winner])
# for i in range(n):
#     score += (i+1)*decks[winner][n-1-i]
# print(score)

class Game:

    def __init__(self,decks,depth=0):
        self.decks = decks
        self.seen = []
        self.hasSeen = False
        self.winner = None
        self.depth = depth

    def playout(self):
        while self.winner==None:
            self.play()
        return self.winner

    def play(self):
        print(" "*self.depth+"Playing a round")
        if self.decks in self.seen:
            print(" "*self.depth+"Halting infinite loop")
            self.hasSeen = True
            self.winner = 0
        else:
            self.seen += [deepcopy(self.decks)]
            a,b = self.decks[0].pop(0), self.decks[1].pop(0)
            print(" "*self.depth+"Cards:",a,b)
            if len(self.decks[0])>=a and len(self.decks[1])>=b:
                print(" "*self.depth+"Going to a subgame")
                newDecks = [self.decks[0][:a], self.decks[1][:b]]
                g = Game(newDecks,self.depth+1)
                winner = g.playout()
            else:
                winner = int(b>a)
            if winner == 0:
                self.decks[0] += [a,b]
            else:
                self.decks[1] += [b,a]
            if len(self.decks[0])==0:
                self.winner = 1
            elif len(self.decks[1])==0:
                self.winner = 0

# decks = [[9, 2, 6, 3, 1],[5, 8, 4, 7, 10]]

g = Game(decks)
g.playout()
print(g.decks,g.winner)
decks = g.decks
score = 0
winner = g.winner
n = len(decks[winner])
for i in range(n):
    score += (i+1)*decks[winner][n-1-i]
print(score)
