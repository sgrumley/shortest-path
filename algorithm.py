import Dijkstra as algo
import copy
import pq
import NodeClass
import time
# where root path is made turn it into a path object with Cost
# reverse dikstra result
def run(graph, startNode, endNode, k):
    start = time.time()
    cost, path = algo.dijkstra(graph,startNode,endNode)
    print(time.time() - start)
    #return cost, path
    print("cost: ", path[0].cost)
    path.reverse()
    #return 0
    A= []
    B = pq.PriorityQueue()
    initPath = NodeClass.Path(path, cost )
    A.append(initPath)

    # for k-1 shortest paths
    for i in range(1,k):
        print(i, "shortest path")
        # iterate through previous shortest path nodes
        for j in range(len(A[i -1]) -1):
            #print()
            #print()
            # spur node = the current node that will be removed from the path
            spurNode = A[i-1].path[j]
            #create root path up to spur node
            rootPath = []
            rootCost = 0
            for x in range(j):
                #print("j",x, j)
                #print(A[i-1].path[x].label, A[i-1].path[x].cost)
                rootCost += A[i-1].path[x].cost

                rootPath.append(A[i-1].path[x])
            rootCost +=  A[i-1].path[j].cost
            rootPathClass= NodeClass.Path(rootPath, rootCost)
            """
            for i in range(len(rootPath)):
                print("cost: ", rootPath[i].cost)
                print("label: ", rootPath[i].label)
            """
            #remove edge from spur node to next node
            localGraph = copy.deepcopy(graph)
            if spurNode.label != endNode:
                for y in range(len(localGraph[spurNode.label][0])):
                    if localGraph[spurNode.label][0][y]== A[i-1].path[j+1].label:
                        #print("looking to reomove", localGraph[spurNode.label][0][y], localGraph[spurNode.label][1][y])
                        del localGraph[spurNode.label][0][y]
                        del localGraph[spurNode.label][1][y]
                        break

            # recalculate the best path without the above defined edge
            bCost, spurPath = algo.dijkstra(localGraph,spurNode.label, endNode)

            # If dikstra doesnt find a path skip iteration
            if spurPath == None:
                #print("unable to find  path")
                break

            # Needs fixing, temp fix to reverse
            spurPath.reverse()

            # find total cost by summing cost of last values
            if len(rootPath) == 0:
                totalCost = spurPath[-1].cost
            elif len(spurPath) == 0:
                totalCost = rootPath[-1].cost
            else:
                totalCost =  rootPathClass.cost + spurPath[-1].cost
                """
                print(len(rootPath))
                print("bCost", bCost, "rootPath", rootPath[-1].cost, "spur path", spurPath[-1].cost)
                print("should cost be", spurPath[0].cost)
                print(spurNode.cost)
                print(rootPathClass.cost)
                """


            # Append spur path to root path
            totalPath = rootPath

            for a in range(len(spurPath)):
                if len(spurPath)== 0:
                    break
                totalPath.append(spurPath[a])

            # parse data into object form
            pathFinal = NodeClass.Path(totalPath, totalCost)
            #print("current path being assessed:", pathFinal.pathLabel, pathFinal.cost)
            cont = B.contains(pathFinal)
            if cont == False:
                B.insert(pathFinal)
                #print("inserted")


        dupe = True
        #check if B is already in A
        while (dupe == True):
            dupe = False
            tempForA = B.removeMax()
            for a in range(len(A)):
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
