import Dijkstra as algo
import algorithm
import algo

def readFile(fileName):
    file = open(fileName, "r")
    i = 0
    graph = {}
    for line in file:
        if i == 0:
            temp = line.split()
            numVert = int(temp[0])
            numEdge = int(temp[1])

        elif i==numEdge+1:
            temp = line.split()
            s = temp[0]
            f = temp[1]
            k = int(temp[2])
        else:
            temp = line.split()
            if temp[0] in graph:
                graph[temp[0]][0].append(temp[1])
                #graph[temp[0]][1].append(int(temp[2]))
                graph[temp[0]][1].append(float(temp[2]))
            else:
                tempArr=[]
                endNode =[temp[1]]
                #weight =[int(temp[2])]
                weight =[float(temp[2])]
                tempArr.append(endNode)
                tempArr.append(weight)
                graph.setdefault(temp[0], tempArr)
        i+=1


    return numVert, numEdge, graph, s, f, k


fileName = "finalInput.txt"
#fileName = "input.txt"

numVert, numEdge, graph, startNode, endNode, k =  readFile(fileName)
print(startNode,endNode)
"""
print("Graph contains:" )
print(numVert, "Vertices")
print(numEdge, "Edges")
print("Find the shortest path from", startNode, "to", endNode)
print(graph)


#print(first path found)
for i in range(len(path)):
    print(path[i].label)
"""
print("-----------------------------------------------------------------------")
#final = algorithm.run( graph, startNode, endNode, k)
final = algo.run( graph, startNode, endNode, k)
#exit()
print("-----------------------------------------------------------------------")
print(len(final))
for i in range(len(final)):
    #print(final[i].label)

    final[i].printPath()
