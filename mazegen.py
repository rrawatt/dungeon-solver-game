import random

def incdec(currenta, x):       #to change position as per x
    current = list(currenta)
    if x == 'u':
        current[1] -= 1
    elif x == 'd':
        current[1] += 1
    elif x == 'r':
        current[0] += 1
    elif x == 'l':
        current[0] -= 1
    return current

def news(tempcurrent, current, board):  # check the four directions
    news = [incdec(tempcurrent, x) for x in ['u', 'd', 'r', 'l']]

    states = [board[i[0]][i[1]][2] for i in news if i != current and (0<i[0]<49) and (0<i[1]<49)]
    return states

def rando(board,n):
    path = set()
    choices = ['u', 'd', 'r', 'l'] 

    start = random.choice([(random.randint(1, 48-n), random.choice([0+n, 49-n])),
                           (random.choice([0+n, 49-n]), random.randint(1+n, 48-n))])
    current = [start[0], start[1]]  # tail of generator
    board[start[0]][start[1]] = 1  # setting state of start 1

    if current[0] == 0+n:  # x coord will always be incremented, MOVES RIGHT
        current[0] += 1  # x away from 1
        board[current[0]][current[1]][2] = 1
        firs=current[::]

        while current[0] != 49-n:  # boundary is not reached

            weights = [current[1] / 49 * 0.20, 0.20 * (49 - current[1]) / 49, 0.49, 0.00]  # weight according to the loc of the player
            choice = random.choices(choices, weights=weights)[0]  # choice of one of the four directions
            tempcurrent = incdec(current, choice)

            if board[tempcurrent[0]][tempcurrent[1]][2] != 1 and 1 not in news(tempcurrent, current, board):
                board[tempcurrent[0]][tempcurrent[1]][2] == 1
                current = tuple(tempcurrent)
                path.add(current)
     

    elif current[0] == 49-n:  # x coord will mostly be decremnted, MOVES LEFT
        current[0] -= 1
        board[current[0]][current[1]][2] = 1
        firs=current[::]

        while current[0] != 0+n:  # boundary is not reached

            weights = [current[1] / 49 * 0.20, 0.20 * (49 - current[1]) / 49, 0.00, 0.49]  # weight according to the loc of the player
            choice = random.choices(choices, weights=weights)[0]
            tempcurrent = incdec(current, choice)

            if board[tempcurrent[0]][tempcurrent[1]][2] != 1 and 1 not in news(tempcurrent, current, board):
                board[tempcurrent[0]][tempcurrent[1]][2] == 1
                current = tuple(tempcurrent)
                path.add(current)


    elif current[1] == 0+n:  # y coord will mostly be incremented, MOVES DOWN
        current[1] += 1
        board[current[0]][current[1]][2] = 1
        firs=current[::]

        while current[1] != 49-n:  # boundary is not reached
            weights = [0.00, 0.49, 0.20 * (49 - current[0]) / 49, current[0] / 49 * 0.20]
            choice = random.choices(choices, weights=weights)[0]
            tempcurrent = incdec(current, choice)

            if board[tempcurrent[0]][tempcurrent[1]][2] != 1 and 1 not in news(tempcurrent, current, board):
                board[tempcurrent[0]][tempcurrent[1]][2] == 1
                current = tuple(tempcurrent)
                path.add(current)


    elif current[1] == 49-n:  # y coord will mostly be decremnted, MOVES UP
        current[1] -= 1
        board[current[0]][current[1]][2] = 1
        firs=current[::]

        while current[1] != 0+n:  # boundary is not reached
            weights = [0.49, 0.00, 0.20 * (49 - current[0]) / 49, current[0] / 49 * 0.20]
            choice = random.choices(choices, weights=weights)[0]
            tempcurrent = incdec(current, choice)

            if board[tempcurrent[0]][tempcurrent[1]][2] != 1 and 1 not in news(tempcurrent, current, board):
                board[tempcurrent[0]][tempcurrent[1]][2] == 1
                current = tuple(tempcurrent)
                path.add(current)
    return (path,firs,current)

def mazetree():
    choices = ['u', 'd', 'r', 'l']  # [-1,1,1,-1]
    
    board = []
    for i in range(50):
        row = []
        for j in range(50):
            cell = [i, j, 0]
            row.append(cell)
        board.append(row)

    path = rando(board,0)  #main path
    travellable=path[0].copy() #main path + branching paths

    for i in range(13):
        travellable=travellable.union(rando(board,1)[0])

    return (travellable,path)
