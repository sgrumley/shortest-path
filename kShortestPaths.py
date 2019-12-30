import NodeClass
import time
import pickle
import Dijkstra as dbm
import sys
import algo


# read in file to dictionary and variables
def read_file(file_name):
    # data equals every line in input file
    with open(file_name) as file:
        data = list(file)

    # define variables other than edges, nodes and weights
    graph = {}
    end_node_parents = []
    first = data[0].split()
    num_vert = int(first[0])
    num_edge = int(first[1])
    last = data[-1].split()
    s = last[0]
    f = last[1]
    k = int(last[2])
    # for every edge, node and weight split the line into words
    for i in range(1, len(data)-1):
        temp = data[i].split()
        # if the node is already in the dictionary add the end node and weight to the value
        if temp[0] in graph:
            if temp[1] == f:
                end_node_parents.append(temp[0])
            graph[temp[0]][0].append(temp[1])
            graph[temp[0]][1].append(float(temp[2]))
        # Else create key and add the end node and weight to the value
        else:
            temp_arr = []
            endNode = [temp[1]]
            if temp[1] == f:
                end_node_parents.append(temp[0])
            weight = [float(temp[2])]
            temp_arr.append(endNode)
            temp_arr.append(weight)
            graph.setdefault(temp[0], temp_arr)

    return num_vert, num_edge, graph, s, f, k, end_node_parents


# creates a path by backtracking through a list of nodes iterating from end node.prev
def make_path(explored, path, cost, previousPath):
    # Iterate backwards through explored list
    for x in range(len(explored)-1,-1,-1):
        currentPath = explored.items[x]
        if currentPath.label == previousPath:
            path.append(currentPath)
            previousPath = currentPath.prev
    # reverse the path to make it go from start to finish
    path.reverse()
    # parse information into path object
    pathObj = NodeClass.Path(path, cost)
    return pathObj


# quick sort
def sort(data):
    less = []
    equal = []
    greater = []

    if len(data) > 1:
        pivot = data[0].replacedDif
        for x in range(len(data)):
            if data[x].replacedDif < pivot:
                less.append(data[x])
            elif data[x].replacedDif == pivot:
                equal.append(data[x])
            elif data[x].replacedDif > pivot:
                greater.append(data[x])
        return sort(less)+equal+sort(greater)
    else:
        return data


file_name = sys.argv[1]
# read file in
num_vert, num_edge, graph, startNode, endNode, k, end_node_parents = read_file(file_name)
print(startNode, endNode)
startBegin = time.time()
# Run Dijkstra algorithm to find the shortest path
result, explored, changes = dbm.dijkstra(graph, startNode, endNode)

print("Search time",time.time() - startBegin)
# sort changes (list of all updates dijkstra made) from smallest change to largest
changes = sort(changes)
# define kPaths and add the first path found from Dijkstra
kPaths = [result]


""" Check if goal adjacent nodes have been explored """
# remove the goal node parent that is in the final solution
end_node_parents.remove(result.path[-2].label)
# create a copy of explored nodes to preserve original state
for i in range(len(explored)):
    for j in range(len(end_node_parents)):
        if end_node_parents[j] == explored.items[i].label:
            # Define path and add last 2 nodes in
            # ExploredCpy = copy.deepcopy(explored)
            path=[]
            path.append(explored.items[-1])
            path.append(explored.items[i])
            # Define previous path as the node leading into the current second last node
            previousPath = explored.items[i].prev
            # Get cost for the path
            for x in range(len(graph[explored.items[i].label][1])):
                if graph[explored.items[i].label][0][x] == endNode:
                    index = x
            cost = explored.items[i].cost + graph[explored.items[i].label][1][index]
            # Pass all parameters to return a path object of the new solution
            finalPath = make_path(explored, path, cost, previousPath)
            kPaths.append(finalPath)


""" Find minimum alternative paths """
# iterate through changes from smallest to largest and see if and of the changed nodes are in the shortest path
selected = False
for i in range(len(changes)):
    # Could potentially become a set
    for j in range(len(result)):
        if selected == True:
            selected = False
            break
        # if we have k paths stop loops
        if len(kPaths) >= k:
            break
        # If the node in result appears in changes made
        if changes[i].label == result.path[j].label:
            # Check if that node was explored by Dijkstra
            checks = explored.check_up(changes[i].label)
            if checks == True:
                # Find the position in explored list and revert the change
                for x in range(len(explored.items)):
                    if explored.items[x].label == changes[i].label:
                        print(explored.items[x].label)
                        start = time.time()
                        explored.items[x].cost =  changes[i].cost
                        explored.items[x].prev =  changes[i].prev
                        # Iterate through the explored lsit and create a path that will contain the alternative route
                        path=[]
                        path.append(explored.items[-1])
                        previousPath = path[0].prev
                        cost = path[0].cost + changes[i].replacedDif
                        finalPath = make_path(explored, path, cost, previousPath)
                        # Check if path already exists
                        kPaths.append(finalPath)
                        print("k", len(kPaths))
                        print("Search time", time.time() - startBegin)
                        selected = True
                        break
print()
print("K Paths")
for i in range(len(kPaths)):
    print(kPaths[i].cost)

if len(kPaths) < k:
    final = algo.run(graph, startNode, endNode, k)

    for i in range(len(final)):
        final[i].printPath()
