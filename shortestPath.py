import Dijkstra as algo


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
        else:
            temp = line.split()
            if temp[0] in graph:
                graph[temp[0]][0].append(temp[1])
                graph[temp[0]][1].append(int(temp[2]))
            else:
                tempArr=[]
                endNode =[temp[1]]
                weight =[int(temp[2])]
                tempArr.append(endNode)
                tempArr.append(weight)
                graph.setdefault(temp[0], tempArr)
        i+=1


    return numVert, numEdge, graph, s, f


fileName = "input.txt"
numVert, numEdge, graph, startNode, endNode =  readFile(fileName)
"""
print("Graph contains:" )
print(numVert, "Vertices")
print(numEdge, "Edges")
print("Find the shortest path from", startNode, "to", endNode)
print(graph)
"""
algo.dijkstra(graph,startNode,endNode)
