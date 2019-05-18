import pq

def dijkstra(graph, startNode, endNode):
    queue = pq.PriorityQueue
    queue.insert((startNode, 0))
    print(graph[startNode])

#create a data structure that refelects previous node and cost
# change pq to reflect assignment 2
"""
function dijkstra(G, s):

for v in V:
    v.dist = infinity  // Initialize distance decorations
    v.prev = null      // Initialize previous pointers to null
s.dist = 0             // Set distance to start to 0

PQ = PriorityQueue(V)    // Use v.dist as priorities
while PQ not empty:
    u = PQ.removeMin()
    for all edges (u, v):  //each edge coming out of u
        if v.dist > u.dist + cost(u, v): // cost() is weight
        v.dist = u.dist + cost(u,v)   // Replace as necessary
        v.prev = u // Maintain pointers for path
        PQ.replaceKey(v, v.dist)
"""
