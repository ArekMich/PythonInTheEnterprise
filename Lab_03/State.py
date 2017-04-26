__author__ = 'Arkadiusz'

class State():

    def __init__(self, state, mainState, copyState):
        self.state = state
        self.mainState = mainState
        self.copyState = copyState

    def displayMainState(self):
        print "HOW TO PLAY"
        print "Number of places:"

        print("_" * 10)
        print " ", self.mainState[0], self.mainState[1], self.mainState[2]
        print " ", self.mainState[3], self.mainState[4], self.mainState[5]
        print " ", self.mainState[6], self.mainState[7], self.mainState[8]
        print("_" * 10)
        print "START"

    def displayState(self):
        for i in range(9):
            if self.state[i]==0:
                self.copyState[i] = '_'
            if self.state[i]==1:
                self.copyState[i] = 'X'
            if self.state[i]==2:
                self.copyState[i] = 'O'

        print self.copyState[0], self.copyState[1], self.copyState[2]
        print self.copyState[3], self.copyState[4], self.copyState[5]
        print self.copyState[6], self.copyState[7], self.copyState[8]