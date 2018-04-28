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
        
def newStates(state):
    children = [];
    if state.side == -1:
        newState = State(state.cannibalLeft, state.missionaryLeft - 2, 1, state.cannibalRight, state.missionaryRight + 2)
        ## Two missionaries cross left to right.
        if newState.isValid():
            newState.parent = state
            children.append(newState)
        newState = State(state.cannibalLeft - 2, state.missionaryLeft, 1, state.cannibalRight + 2, state.missionaryRight)
        ## Two cannibals cross left to right.
        if newState.isValid():
            newState.parent = state
            children.append(newState)
        newState = State(state.cannibalLeft - 1, state.missionaryLeft - 1, 1, state.cannibalRight + 1, state.missionaryRight + 1)
        ## One missionary and one cannibal cross left to right.
        if newState.isValid():
            newState.parent = state
            children.append(newState)
        newState = State(state.cannibalLeft, state.missionaryLeft - 1, 1, state.cannibalRight, state.missionaryRight + 1)
        ## One missionary crosses left to right.
        if newState.isValid():
            newState.parent = state
            children.append(newState)
        newState = State(state.cannibalLeft - 1, state.missionaryLeft, 1, state.cannibalRight + 1, state.missionaryRight)
        ## One cannibal crosses left to right.
        if newState.isValid():
            newState.parent = state
            children.append(newState)
    else:
        newState = State(state.cannibalLeft, state.missionaryLeft + 2, -1, state.cannibalRight, state.missionaryRight - 2)
        #Two missionaries cross right to left.
        if newState.isValid():
            newState.parent = state
            children.append(newState)
        newState = State(state.cannibalLeft + 2, state.missionaryLeft, -1, state.cannibalRight - 2, state.missionaryRight)
        # Two cannibals cross right to left.
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
        # for avoiding duplicates
        seen = set()
        # adding the initial state to the list
        river.append(initial)
        while river:
            # pops because it returns the item on the list with that index, which in the beginning is initial state
            state = river.pop(0)           
            # if that state is the goal, so 0, 0, right, 3, 3, then return that state
            if state.isGoal() == True:
                printStates(state)
                return state
            #if it isn't the goal, add it to the set, so that way there are no duplicate paths.
            seen.add(state)
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
    # goes through each parent appending it to the path, so now the path will have all the valid traversals
    while crossing:
        traversal.append(crossing)
        crossing = crossing.parent
    # going backwards in list since the parents were added in reverse order
    for x in range(len(traversal), 0, -1):
        state = traversal[x - 1] # have to do -1 so you start at the left side
        sideStr = ''
        if state.side == -1:
            sideStr = 'left'
        else:
            sideStr = 'right'
        print("({0}, {1}, {2}, {3}, {4})".format(state.cannibalLeft, state.missionaryLeft, sideStr, state.cannibalRight, state.missionaryRight))

def main():
    winner = bfs()

main()

