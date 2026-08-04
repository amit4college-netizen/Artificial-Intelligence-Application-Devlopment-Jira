import heapq

#display puzzle state
def print_state(state):
    for i in range (0,9,3):
        print(state[i],state[i+1],state[i+2])
    print()