# Cannibals and Missionary Problem 

# Describes state which includes the cannibals, missionaries, if the transition is valid. 
class State():
    
    def __init__(self, cannibalLeft, missionaryLeft, side, cannibalRight, missionaryRight):
        self.cannibalLeft = cannibalLeft
        self.missionaryLeft = missionaryLeft
        self.side = side
        self.cannibalRight = cannibalRight
        self.missionaryRight = missionaryRight
        self.parent = None
        
    def isGoal(self):
        return self.cannibalLeft == 0 and self.missionaryLeft == 0
    
    def isValid(self):
        if self.missionaryLeft < 0 and self.missionaryRight < 0:
            return False
        if self.cannibalLeft < 0 or self.cannibalRight < 0:
            return False
        if self.missionaryLeft < self.cannibalLeft and self.missionaryLeft != 0:
            return False
        if self.missionaryRight < self.cannibalRight and self.missionaryRight != 0:
            return False
        return True
 
# New States returns a list of predecessors of a certain state, checking its validity and adding it to a list, which is returned in the end.
# Referenced: https://github.com/marianafranco/missionaries-and-cannibals/blob/master/python/missionaries_and_cannibals.py

def newStates(state):
    children = []
    cannibalLeft = [0, -2, -1, 0, -1]
    missionaryLeft = [-2, 0, -1, -1, 1]
    cannibalRight = [0, 2, 1, 0, 1]
    missionaryRight = [2, 0, 1, 1, 0]    
    # if you're on the left
    if state.side == -1:
        newState = State(state.cannibalLeft, state.missionaryLeft - 2, 1, state.cannibalRight, state.missionaryRight + 2)
        for x in range(4):
            if newState.isValid():
                newState.parent = state
                children.append(newState)
            newState = State(state.cannibalLeft + cannibalLeft[x], state.missionaryLeft + missionaryLeft[x], 1, state.cannibalRight + cannibalRight[x], state.missionaryRight + missionaryRight[x])
        if newState.isValid():
            newState.parent = state
            children.append(newState)
    # if you're on the right
    if state.side == 1:
        newState = State(state.cannibalLeft, state.missionaryLeft + 2, -1, state.cannibalRight, state.missionaryRight - 2)
        if newState.isValid():
            newState.parent = state
            children.append(newState)
        newState = State(state.cannibalLeft + 1, state.missionaryLeft + 1, -1, state.cannibalRight - 1, state.missionaryRight - 1)
        # One missionary and one cannibal cross right to left.
        if newState.isValid():
            newState.parent = state
            children.append(newState)
        newState = State(state.cannibalLeft, state.missionaryLeft + 1, -1, state.cannibalRight, state.missionaryRight - 1)
        # One missionary crosses right to left.
        if newState.isValid():
            newState.parent = state
            children.append(newState)
        newState = State(state.cannibalLeft + 1, state.missionaryLeft, -1, state.cannibalRight - 1, state.missionaryRight)
        # One cannibal crosses right to left.
        if newState.isValid():
            newState.parent = state
            children.append(newState)
            
    return children

def bfs():
    # starting off with initial state that there's 3 missionaries and 3 cannibals and the boats on the left with no one else on the other side.
    initial = State(3, 3, -1, 0, 0)
    if initial.isGoal() == True:
        return initial
    else:
        river = []
        seen = []
        # adding the initial state to the list
        river.append(initial)
        while river:
            # pops because it returns the item on the list with that index, which in the beginning is initial state
            state = river.pop(0)           
            # if that state is the goal, so 0, 0, right, 3, 3, then return that state
            if state.isGoal() == True:
                printStates(state)
                return state
            #if it isn't the goal, add it to the list
            seen.append(state)
            # basing off of what was the initial, newStates will return a list of new valid states.
            childStates = newStates(state)           
            # based off of the list of valid childPaths that stem from the initial state, we will append that child to the river (overall list)
            for childState in childStates:
                if childState not in seen or childState not in river:
                    river.append(childState)

def printStates(solution):
    traversal = []
    traversal.append(solution)
    crossing = solution.parent
    print("CL ML BOAT CR MR")
    print("----------------")
    # goes through each parent appending it to the path, so now the path will have all the valid traversals
    while crossing:
        traversal.append(crossing)
        crossing = crossing.parent
    # going backwards in list since the parents were added in reverse order
    for x in range(len(traversal), 0, -1):
        state = traversal[x - 1] # have to -1 so you start at the left side
        sideStr = ''
        if state.side == -1:
            sideStr = '|----'
        else:
            sideStr = '----|'
        print("{0}, {1} {2} {3},{4} ".format(state.cannibalLeft, state.missionaryLeft, sideStr, state.cannibalRight, state.missionaryRight))

def main():
    winner = bfs()

main()

