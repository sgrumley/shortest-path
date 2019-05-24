import pq

class Node():
    def __init__(self, label):
        self.label = label
        self.cost = float('inf')
        self.prev = None


def dijkstra(graph, startNode, endNode):
    print("Dijkstra started")
    explored = pq.Stack()
    queue = pq.PriorityQueue()
    startNode = Node(startNode)
    startNode.cost=0
    queue.insert(startNode)
    updated=0
    count = 0
    actUp = 0
    while len(queue) > 0:
        # pop minimum cost from queue as current node
        currentNode = queue.removeMax()
        explored.push(currentNode)
        # if current node is goal node return path and cost
        if currentNode.label == endNode:
            print("end node found")
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
            print("Dijkstra ended w/ result")
            return cost, path
        #print()
        #print("current node:",currentNode.label, "prev:",currentNode.prev ,"Cost:",currentNode.cost)
        # check if node connects to anything
        try:
            length = len(graph[currentNode.label][0])
            print("length",length)
            print("lookup lenght",len(queue))
            print()
        except:
            break
        # iterate through all children nodes
        for i in range(length):
            #  check if new Node is already in the queue
            ind = queue.lookUp(graph[currentNode.label][0][i])
            # If node is in queue and the current path is shorter -> update
            if ind != False:
                print("updated count", updated)
                updated +=1
                newWeight = currentNode.cost + graph[currentNode.label][1][i]
                previousWeight = queue.items[ind].cost
                # if the current cost is smaller than the cost of the node, update it
                if newWeight < previousWeight:
                    print("actual updates:", actUp)
                    actUp += 1
                    queue.items[ind].cost = newWeight
                    queue.items[ind].prev = currentNode.label
            # else if the node isnt in the queue yet, add it in
            else:
                print("count",count)
                print("node",graph[currentNode.label][0][i])
                count+=1
                newNode = Node(graph[currentNode.label][0][i])
                newNode.cost = currentNode.cost + graph[currentNode.label][1][i]
                newNode.prev = currentNode.label
                queue.insert(newNode)
    print("Dijkstra ended w/o result")
    return "not found", None
#create a data structure that refelects previous node and cost
# change pq to reflect assignment 2
