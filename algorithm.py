import Dijkstra as algo
import copy

def run(path, graph, startNode, endNode, k):
    A=[]
    B=[]
    A.append(path)

    for i in range(1,k):
        print(i, "shortest path")
        for j in range(len(A[i-1])):
            spurNode = A[i-1][j]
            rootPath = []
            for x in range(j):
                rootPath.append(A[i-1][x])
            """ checking root path and spur node
            print(spurNode.label)
            print(len(rootPath))
            """
            #remove edges and nodes
            localGraph = copy.deepcopy(graph)
            if spurNode.label != endNode:
                for y in range(len(localGraph[spurNode.label][0])):
                    print(y, "out of", len(localGraph[spurNode.label][0]))
                    if localGraph[spurNode.label][0][y]== A[i-1][j+1].label:
                        print("looking to reomove", localGraph[spurNode.label][0][y], localGraph[spurNode.label][1][y])
                        del localGraph[spurNode.label][0][y]
                        del localGraph[spurNode.label][1][y]
                        break
            #spurPath = Dikstra()
            cost, spurPath = algo.dijkstra(localGraph,spurNode.label, endNode)
            spurPath.reverse()

            totalPath = []
            print(spurPath,"spur")
            for a in range(len(rootPath)):
                if len(rootPath) == 0:
                    break
                totalPath.append(rootPath[a])
            print(totalPath)
            for a in range(len(spurPath)):
                if len(spurPath)== 0:
                    break
                totalPath.append(spurPath[a])
            totalPath.append(rootPath)

            print("b4",totalPath)
            for a in range(len(totalPath)):
                print(totalPath[a].label)

            #B.append(totalPath)
            B.append(spurPath)
            # add shortest B to A
        break
        if B == []:
            break
