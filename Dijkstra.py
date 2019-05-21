import pq

class Node():
    def __init__(self, label):
        self.label = label
        self.cost = float('inf')
        self.prev = None


def dijkstra(graph, startNode, endNode):
    explored = pq.Stack()
    queue = pq.PriorityQueue()
    startNode = Node(startNode)
    startNode.cost=0
    queue.insert(startNode)

    x = 0
    while len(queue) > 0:
        #Test code
        #if x == 3:
        #    break
        #Test code
        # pop minimum cost from queue as current node
        currentNode = queue.removeMax()
        explored.push(currentNode)
        # if current node is goal node return path and cost
        if currentNode.label == endNode:
            #shows every node visited
            """
            print()
            print("explored list")
            for i in range(len(explored)):
                print("node:",explored[i].label, "prev:",explored[i].prev ,"Cost:",explored[i].cost)
            """
            path=[]
            path.append(explored.pop())
            previousPath = path[0].prev
            cost = path[0].cost
            #Iterate through explored nodes and piece together the path from  the goal node to start node
            for i in range(len(explored)):
                currentPath = explored.pop()
                if currentPath.label == previousPath:
                    path.append(currentPath)
                    previousPath = currentPath.prev
            #print path
            """
            print()
            print("path")
            for j in range(len(path)):
                print("node:",path[j].label, "prev:",path[j].prev ,"Cost:",path[j].cost)
            """

            return cost, path
        #print()
        #print("current node:",currentNode.label, "prev:",currentNode.prev ,"Cost:",currentNode.cost)
        # check if node connects to anything
        try:
            length = len(graph[currentNode.label][0])
        except:
            break
        # iterate through all children nodes
        for i in range(length):
            #  check if new Node is already in the queue
            ind = queue.lookUp(graph[currentNode.label][0][i])
            if ind != False:
                newWeight = currentNode.cost + graph[currentNode.label][1][i]
                previousWeight = queue.items[ind].cost
                # if the current cost is smaller than the cost of the node, update it
                if newWeight < previousWeight:
                    queue.items[ind].cost = newWeight
                    queue.items[ind].prev = currentNode.label
            # if the node isnt in the queue yet, add it in
            else:
                newNode = Node(graph[currentNode.label][0][i])
                newNode.cost = currentNode.cost + graph[currentNode.label][1][i]
                newNode.prev = currentNode.label
                queue.insert(newNode)
        #print("Nodes available:")
        #for i in range(1,len(queue)+1):
            #print("node:",queue.items[i].label, "prev:",queue.items[i].prev ,"Cost:",queue.items[i].cost)
        x+=1

    return "not found"
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
