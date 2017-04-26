__author__ = 'Arkadiusz'

player = 1

mainState = [0,1,2,
             3,4,5,
             6,7,8]
state = [0,0,0,
         0,0,0,
         0,0,0]
copyState = ['_','_','_',
         '_','_','_',
         '_','_','_']

def displayMainState():
    print "HOW TO PLAY"
    print "Number of places:"

    print("_" * 10)
    print " ", mainState[0], mainState[1], mainState[2]
    print " ", mainState[3], mainState[4], mainState[5]
    print " ", mainState[6], mainState[7], mainState[8]
    print("_" * 10)
    print "START"

def displayState(state):
    for i in range(9):
        if state[i]==0:
            copyState[i] = '_'
        if state[i]==1:
            copyState[i] = 'X'
        if state[i]==2:
            copyState[i] = 'O'

    print copyState[0], copyState[1], copyState[2]
    print copyState[3], copyState[4], copyState[5]
    print copyState[6], copyState[7], copyState[8]

def checkWin(state, player):
    if state[0]==player and state[1]==player and state[2]==player:
        return 'win'
    if state[3]==player and state[4]==player and state[5]==player:
        return 'win'
    if state[6]==player and state[7]==player and state[8]==player:
        return 'win'
    if state[0]==player and state[3]==player and state[6]==player:
        return 'win'
    if state[1]==player and state[4]==player and state[7]==player:
        return 'win'
    if state[3]==player and state[5]==player and state[8]==player:
        return 'win'
    if state[0]==player and state[4]==player and state[8]==player:
        return 'win'
    if state[2]==player and state[4]==player and state[6]==player:
        return 'win'

    # checking for empty places
    for i in range(9):
        if state[i]==0:
            return

    return 'stalemate'

def checkValid(state):
    validMoves=[]

    for i in range(9):
        if state[i]==0:
            validMoves.append(i)

    return validMoves

#----------------------------------
displayMainState()
displayState(state)

while True:
    print "Player ", player
    while True:
        move = input("What is your move? ")

        #check valid
        validMoves = checkValid(state)

        if move in validMoves:
            break
        else:
            print "Illegal move!"

    state[move] = player
    displayState(state)

    winStatus = checkWin(state, player)
    if winStatus == 'win':
        print "Player ", player, " wins!"
        break
    if winStatus == 'loses':
        print "Player ", player, " loses!"
        break
    if winStatus == 'stalemate':
        print "Stalemate!"
        break

    if player == 1:
        player = 2
    else:
        player = 1

print "Game Over"

