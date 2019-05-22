import Dijkstra as algo
import copy
import pq
import NodeClass

def run(path, graph, startNode, endNode, k):
    A=[]
    B = pq.PriorityQueue()
    tempCost = 7
    initPath = NodeClass.Path(path, tempCost )
    A.append(initPath)

    for i in range(1,k):
        print(i, "shortest path")

        lengthA = len(A[i -1]) -1
        for j in range(lengthA ):
            print()
            print()
            spurNode = A[i-1].path[j]
            rootPath = []
            for x in range(j):
                rootPath.append(A[i-1].path[x])

            #remove edge from spur node
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
                print("unable to find  path")
                break

            # Needs fixing, temp fix to reverse
            spurPath.reverse()

            # find total cost by summing cost of last values
            if len(rootPath) == 0:
                totalCost = spurPath[-1].cost
            elif len(spurPath) == 0:
                totalCost = rootPath[-1].cost
            else:
                print("bCost", bCost, "rootPath", rootPath[-1].cost, "spur path", spurPath[-1].cost)
                totalCost =  rootPath[-1].cost + spurPath[-1].cost

            # Append spur path to root path
            totalPath = rootPath

            for a in range(len(spurPath)):
                if len(spurPath)== 0:
                    break
                totalPath.append(spurPath[a])

            # parse data into object form
            pathFinal = NodeClass.Path(totalPath, totalCost)
            print("current path being assessed:", pathFinal.pathLabel, pathFinal.cost)
            cont = B.contains(pathFinal)
            if cont == False:
                B.insert(pathFinal)
                print("inserted")



            # add shortest B to A
        dupe = True
        #check if B is already in A
        while (dupe == True):
            dupe = False
            tempForA = B.removeMax()
            for a in range(len(A)):
                if  A[a].pathLabel == tempForA.pathLabel:
                    dupe = True
                    print("comp",pathFinal.pathLabel, A[a].pathLabel)
            if dupe == False:
                A.append(tempForA)
                print("A recieved", tempForA.pathLabel)



        print("INNER IS DONE")
        print(len(B), "left in B")
        if len(B) == 0:
            break
    return A
