import pq
import NodeClass
import copy


def dijkstra(graph, start_node, end_node):
    # define all objects for search
    explored = pq.Stack()
    queue = pq.PriorityQueue()
    change_checker = set()
    start_node = NodeClass.Node(start_node)
    start_node.cost = 0
    queue.insert(start_node)
    changes = []
    # While there is still elements in the queue
    while len(queue) > 0:
        # Pop minimum cost from queue as current node and add it too list of explored nodes
        current_node = queue.remove_min()
        explored.push(current_node)

        # if current node is goal node return path and cost
        if current_node.label == end_node:
            path = [explored.items[-1]]
            previous_path = path[0].prev
            cost = path[0].cost
            # Iterate through explored nodes and piece together the path from  the goal node to start node
            for x in range(len(explored) -1, -1, -1):
                current_path = explored.items[x]
                if current_path.label == previous_path:
                    path.append(current_path)
                    previous_path = current_path.prev
            path.reverse()
            result = NodeClass.Path(path, cost)
            return result, explored, changes

        # Check if node current node has connections
        try:
            length = len(graph[current_node.label][0])
        except:
            break
        # Iterate through all children nodes
        for i in range(length):
            #  Check if new Node is already in the queue
            ind = queue.look_up(graph[current_node.label][0][i])
            # If node is in queue and the current path is shorter -> update
            if ind != False:
                new_cost = current_node.cost + graph[current_node.label][1][i]
                previousWeight = queue.items[ind].cost
                # if the current cost is smaller than the cost of the node, update it
                if new_cost < previousWeight:
                    # If the current node hasn't been updated before
                    if current_node.label not in change_checker:
                        change_checker.add(current_node.label)
                        changes.append(copy.deepcopy(queue.items[ind]))
                        changes[-1].replaced(current_node.label, new_cost)
                    # Update previous node and new cost
                    queue.items[ind].cost = new_cost
                    queue.items[ind].prev = current_node.label
            # Else if the node isn't in the queue yet, creat node object and add it in
            elif ind == False:
                new_node = NodeClass.Node(graph[current_node.label][0][i])
                new_node.cost = current_node.cost + graph[current_node.label][1][i]
                new_node.prev = current_node.label
                queue.insert(new_node)
    return None

def forYen(graph, startNode, endNode):
    #print("Dijkstra started")
    explored = pq.Stack()
    queue = pq.PriorityQueue()
    startNode = NodeClass.Node(startNode)
    startNode.cost=0
    queue.insert(startNode)
    updated=0
    count = 0
    actUp = 0
    while len(queue) > 0:
        # pop minimum cost from queue as current node
        currentNode = queue.remove_min()
        explored.push(currentNode)
        # if current node is goal node return path and cost
        if currentNode.label == endNode:
            #print("end node found")
            path=[]
            path.append(explored.pop())
            previousPath = path[0].prev
            cost = path[0].cost
            #Iterate through explored nodes and piece together the path from  the goal node to start node
            for x in range(len(explored) -1, -1, -1):
                currentPath = explored.pop()
                if currentPath.label == previousPath:
                    path.append(currentPath)
                    previousPath = currentPath.prev
            #print("Dijkstra ended w/ result")
            path.reverse()
            result = NodeClass.Path(path, cost)
            #append result
            # remove weight to end node


            return result
        #print()
        #print("current node:",currentNode.label, "prev:",currentNode.prev ,"Cost:",currentNode.cost)
        # check if node connects to anything
        try:
            length = len(graph[currentNode.label][0])
            #print("length",length)
            #print("lookup lenght",len(queue))
            #print()
        except:
            break
        # iterate through all children nodes
        for i in range(length):
            #  check if new Node is already in the queue
            ind = queue.look_up(graph[currentNode.label][0][i])
            # If node is in queue and the current path is shorter -> update
            if ind != False:
                #print("updated count", updated)
                updated +=1
                newWeight = currentNode.cost + graph[currentNode.label][1][i]
                previousWeight = queue.items[ind].cost
                # if the current cost is smaller than the cost of the node, update it
                if newWeight < previousWeight:
                    #print("actual updates:", actUp)
                    actUp += 1
                    queue.items[ind].cost = newWeight
                    queue.items[ind].prev = currentNode.label
            # else if the node isnt in the queue yet, add it in
            else:
                #print("count",count)
                #print("node",graph[currentNode.label][0][i])
                count+=1
                newNode = NodeClass.Node(graph[currentNode.label][0][i])
                newNode.cost = currentNode.cost + graph[currentNode.label][1][i]
                newNode.prev = currentNode.label
                queue.insert(newNode)
    #print("Dijkstra ended w/o result")
    return None
