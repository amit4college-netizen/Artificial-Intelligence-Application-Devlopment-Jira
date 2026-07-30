#Water jug problem using dfs

j1=int(input("Enter capacity of jug 1 : "))
j2=int(input("Enter capacity of jug 2 : "))
goal=int(input("Enter target amount : "))

visited = set()

def dfs(x, y, path):
    if x==goal or y==goal:
        path.append((x,y))
        print("\nGoal achived sucessfully")
        print("Solution path : ")
        for state in path:
            print(state)
        return True
    
    if(x,y) in visited:
        return False
    visited.add((x,y))
    path.append((x,y))

    next_states = [
        (j1, y), #fill jug1
        (x, j2), #fill jug2
        (0, y), #empty jug1
        (x, 0), #empty jug2

        #pour Jug1 -> Jug2
        (x-min(x,j2-y),
        y+min(x,j2-y)),

        #pour Jug2 -> Jug1
        (x+min(y,j1-x),
        y-min(y,j1-x))
    ]

    for state in next_states:
        if dfs(state[0],state[1],path.copy()):
            return True
    return False

if not dfs(0,0,[]):
    print("No Solution found")
