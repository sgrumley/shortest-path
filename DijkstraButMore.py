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
