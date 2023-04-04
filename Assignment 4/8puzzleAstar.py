import copy
from queue import PriorityQueue

def getBlankPosition(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return (i,j) 
            
def heuristic(initial, final):
    count = 0
    for i in range(3):
        for j in range(3):
            if initial[i][j] == final[i][j]:
                count = count + 1
    return count

def getNextStates(state):
    next_states = []
    blank = getBlankPosition(state)

    # left move
    if blank[1] > 0:
        new_state = copy.deepcopy(state)
        new_state[blank[0]][blank[1]] = new_state[blank[0]][blank[1]-1] 
        new_state[blank[0]][blank[1]-1] = 0
        next_states.append(new_state)

    # right move
    if blank[1] < 2:
        new_state = copy.deepcopy(state)
        new_state[blank[0]][blank[1]] = new_state[blank[0]][blank[1]+1] 
        new_state[blank[0]][blank[1]+1] = 0
        next_states.append(new_state)

    # up move
    if blank[0] > 0:
        new_state = copy.deepcopy(state)
        new_state[blank[0]][blank[1]] = new_state[blank[0]-1][blank[1]] 
        new_state[blank[0]-1][blank[1]] = 0
        next_states.append(new_state)

    # down move
    if blank[0] < 2:
        new_state = copy.deepcopy(state)
        new_state[blank[0]][blank[1]] = new_state[blank[0]+1][blank[1]] 
        new_state[blank[0]+1][blank[1]] = 0
        next_states.append(new_state)

    return next_states

def eightPuzzleAStar(initial, final):
    closed = []
    open = PriorityQueue()
    open.put((heuristic(initial, final), initial, []))

    while open:
        h, state, path = open.get()
        if state == final:
            return path
        if str(state) not in closed:
            closed.append(str(state))
            for next_state in getNextStates(state):
                if next_state is not None:
                    g = len(path) + 1
                    h = heuristic(next_state, final)
                    f = g + h
                    open.put((f, next_state, path + [next_state]))

    return None

if __name__ == '__main__':
    initial= [[2, 0, 3], [1, 8, 4], [7, 6, 5]]
    final = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

    result = eightPuzzleAStar(initial, final)

    for state in result:
        for i in state:
            print(i)
        print('\n\n')
