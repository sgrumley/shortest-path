import Dijkstra as algo
import copy
import pq
import NodeClass
import time
# where root path is made turn it into a path object with Cost
# reverse dikstra result
def run(graph, startNode, endNode, k):
    start = time.time()
    initPath = algo.forYen(graph,startNode,endNode)
    A= []
    B = pq.PriorityQueue()
    A.append(initPath)

    # for k-1 shortest paths
    for i in range(1,k):
        # iterate through previous shortest path nodes
        if  A[i-1] == tuple:
            break

        for j in reversed(range(len(A[i -1])-1)):
            # spur node = the current node that will be removed from the path
            spurNode = A[i-1].path[j]
            rootPath = []
            rootCost = 0
            for x in range(j):
                rootPath.append(A[i-1].path[x])
            rootCost = spurNode.cost
            rootPathClass= NodeClass.Path(rootPath, rootCost)

            #remove edge from spur node to next node
            localGraph = copy.deepcopy(graph)
            if spurNode.label != endNode:
                for y in range(len(localGraph[spurNode.label][0])):
                    if localGraph[spurNode.label][0][y]== A[i-1].path[j+1].label:
                        del localGraph[spurNode.label][0][y]
                        del localGraph[spurNode.label][1][y]
                        break

            # recalculate the best path without the above defined edge
            spurPath = algo.forYen(localGraph,spurNode.label, endNode)


            # If dikstra doesnt find a path skip iteration
            if spurPath == None:
                continue
            # find total cost by summing cost of last values
            if len(rootPath) == 0:
                totalCost = spurPath.cost
            elif len(spurPath) == 0:
                totalCost = rootPath.cost
            else:
                totalCost =  rootPathClass.cost + spurPath.cost

            # Append spur path to root path
            totalPath = rootPathClass.merge(spurPath)
            cont = B.look_up(totalPath)
            if cont == False:
                B.insert(totalPath)


        dupe = True
        #check if B is already in A
        while (dupe == True):
            dupe = False
            tempForA = B.remove_min()
            if tempForA == None:
                break
            for a in range(len(A)):
                if  A[a].label == tempForA.label:
                    dupe = True
            if dupe == False:
                A.append(tempForA)

        if len(B) == 0:
            break
    return A
