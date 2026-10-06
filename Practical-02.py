from collections import deque

def print_state(state):
    for i in range(0,9,3):
        print(state[i],state[i+1],state[i+2])
    print()

def get_neighbors(state):
    neighbors=[]

    blank_index=state.index(0)

    moves = {
        "UP":-3,
        "Down":3,
        "Left":-1,
        "Right":1
    }

    for move,position_change in moves.items():
        new_index = blank_index+position_change
        if move == "UP" and blank_index<3:
            continue
        if move == "Down" and blank_index>5:
            continue
        if move == "Left" and blank_index % 3 == 0:
            continue
        if move == "Right" and blank_index % 3 == 2:
            continue

        new_state = list(state)
        new_state[blank_index],new_state[new_index] = new_state[new_index],new_state[blank_index]

        neighbors.append((tuple(new_state),move))
    return neighbors         

def bfs(initial_state,goal_state):
    queue=deque()

    queue.append((initial_state,[]))

    visited = set()
    visited.add(initial_state)

    while queue:
        current_state, path = queue.popleft()

        if current_state ==goal_state:
            return path
        
        for neighbor, move in get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [(move, neighbor)]))

    return None

initial_state = (1,2,3,
                 4,0,6,
                 7,5,8)

goal_state = (1,2,3,
              4,5,6,
              7,8,0)

print("Initial state")
print_state(initial_state)

print("Goal State")
print_state(goal_state)

solution = bfs(initial_state,goal_state)

if solution:
    print("Shortest sequence of moves:")
    current_step=1

    for move, state in solution:
        print("Step", current_step, "Move:",move)
        print_state(state)
        current_step += 1

        print("Goal reached successfully")
        print("Total number of moves:", len(solution))
else:
    print("No solution found")
