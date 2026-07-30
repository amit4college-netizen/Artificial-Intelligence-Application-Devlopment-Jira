import heapq

graph = {
    'Mumbai':[('Pune',150),('Hydrabad',710)],
    'Pune':[('Mumbai',150),('Banglore',840)],
    'Hydrabad':[('Mumbai',710),('Banglore',570)],
    'Banglore':[]
}

def ucs(start,goal):

    queue = [(0,start,[start])]
    visited = []

    while queue:
        cost,city,path = heapq.heappop(queue)

        if city==goal:
            return cost,path

        if city not in visited:
            visited.append(city)
            for neighbor, distance in graph[city]:
                heapq.heappush(
                    queue,
                    (cost + distance,
                    neighbor,
                    path + [neighbor])
                )

cost, path = ucs("Mumbai", "Banglore")

print("Least-cost path:")
print("Path:","->".join(path))
print("Total Distance:", cost, "km")