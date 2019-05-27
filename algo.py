import Dijkstra as algo
import copy
import pq
import NodeClass
import time
# where root path is made turn it into a path object with Cost
# reverse dikstra result
def run(graph, startNode, endNode, k):
    start = time.time()
    initPath = algo.dijkstra(graph,startNode,endNode)
    print(time.time() - start)
    #return cost, path
    initPath.printPath()

    #return 0
    A= []
    B = pq.PriorityQueue()
    A.append(initPath)

    # for k-1 shortest paths
    for i in range(1,k):
        print(i, "shortest path")
        print(A[i-1].label)
        # iterate through previous shortest path nodes
        for j in reversed(range(len(A[i -1])-1)):
            print()
            print("new B")
            print("================================================")

            #if j == len(A[i -1])-1:
            #    j -= 1


            # spur node = the current node that will be removed from the path
            spurNode = A[i-1].path[j]
            print("Spur Node:", spurNode.label)
            #create root path up to spur node
            rootPath = []
            rootCost = 0
            for x in range(j):
                rootPath.append(A[i-1].path[x])
            rootCost = spurNode.cost
            rootPathClass= NodeClass.Path(rootPath, rootCost)
            print("_-_-_-_-_-_-_-_-_-_-_-_-")
            print("Root:")
            rootPathClass.printPath()

            #remove edge from spur node to next node
            localGraph = copy.deepcopy(graph)
            if spurNode.label != endNode:
                for y in range(len(localGraph[spurNode.label][0])):
                    if localGraph[spurNode.label][0][y]== A[i-1].path[j+1].label:
                        print("Removing", localGraph[spurNode.label][0][y], localGraph[spurNode.label][1][y])
                        del localGraph[spurNode.label][0][y]
                        del localGraph[spurNode.label][1][y]
                        break

            # recalculate the best path without the above defined edge
            print("_-_-_-_-_-_-_-_-_-_-_-_-")
            print("Spur:")
            spurPath = algo.dijkstra(localGraph,spurNode.label, endNode)


            # If dikstra doesnt find a path skip iteration
            if spurPath == None:
                print("unable to find  path")
                continue
            spurPath.printPath()
            # find total cost by summing cost of last values
            if len(rootPath) == 0:
                totalCost = spurPath.cost
            elif len(spurPath) == 0:
                totalCost = rootPath.cost
            else:
                totalCost =  rootPathClass.cost + spurPath.cost

            # Append spur path to root path
            totalPath = rootPathClass.merge(spurPath)
            print("_-_-_-_-_-_-_-_-_-_-_-_-")
            print("Total:")
            totalPath.printPath()

            #print("current path being assessed:", pathFinal.pathLabel, pathFinal.cost)
            cont = B.contains(totalPath)
            if cont == False:
                B.insert(totalPath)
            #if j == 0:
            #    exit()
                #print("inserted")


        dupe = True
        #check if B is already in A
        while (dupe == True):
            dupe = False
            tempForA = B.removeMax()
            if tempForA == None:
                break
            for a in range(len(A)):
                print(A[a].label)
                print(tempForA)
                if  A[a].label == tempForA.label:
                    dupe = True
                    #print("comp",pathFinal.pathLabel, A[a].pathLabel)
            if dupe == False:
                A.append(tempForA)
                print("A recieved", tempForA.label)
                print("cost", tempForA.cost)



        #print("INNER IS DONE")
        #print(len(B), "left in B")
        if len(B) == 0:
            break
    return A
