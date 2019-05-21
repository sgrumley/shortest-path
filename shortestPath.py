import Dijkstra as algo
import algorithm

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
                graph[temp[0]][1].append(int(temp[2]))
            else:
                tempArr=[]
                endNode =[temp[1]]
                weight =[int(temp[2])]
                tempArr.append(endNode)
                tempArr.append(weight)
                graph.setdefault(temp[0], tempArr)
        i+=1


    return numVert, numEdge, graph, s, f, k


fileName = "input.txt"

numVert, numEdge, graph, startNode, endNode, k =  readFile(fileName)
#print(startNode,endNode)
"""
print("Graph contains:" )
print(numVert, "Vertices")
print(numEdge, "Edges")
print("Find the shortest path from", startNode, "to", endNode)
print(graph)
"""
cost, path = algo.dijkstra(graph,startNode,endNode)
path.reverse()
#print(first path found)
for i in range(len(path)):
    print(path[i].label)

print("-----------------------------------------------------------------------")
algorithm.run(path, graph, startNode, endNode, k)

"""
// Initialize the set to store the potential kth shortest path.
   B = [];

   for k from 1 to K: # k iterations
       # The spur node ranges from the first node to the next to last node in the previous k-shortest path.
       for i from 0 to size(A[k − 1]) − 2:

           // Spur node is retrieved from the previous k-shortest path, k − 1.
           spurNode = A[k-1].node(i);
           // The sequence of nodes from the source to the spur node of the previous k-shortest path.
           rootPath = A[k-1].nodes(0, i);

           for each path p in A:
               if rootPath == p.nodes(0, i):
                   // Remove the links that are part of the previous shortest paths which share the same root path.
                   remove p.edge(i,i + 1) from Graph;

           for each node rootPathNode in rootPath except spurNode:
               remove rootPathNode from Graph;

           // Calculate the spur path from the spur node to the sink.
           spurPath = Dijkstra(Graph, spurNode, sink);

           // Entire path is made up of the root path and spur path.
           totalPath = rootPath + spurPath;
           // Add the potential k-shortest path to the heap.
           B.append(totalPath);

           // Add back the edges and nodes that were removed from the graph.
           restore edges to Graph;
           restore nodes in rootPath to Graph;

       if B is empty:
           // This handles the case of there being no spur paths, or no spur paths left.
           // This could happen if the spur paths have already been exhausted (added to A),
           // or there are no spur paths at all - such as when both the source and sink vertices
           // lie along a "dead end".
           break;
       // Sort the potential k-shortest paths by cost.
       B.sort();
       // Add the lowest cost path becomes the k-shortest path.
       A[k] = B[0];
       B.pop();

   return A;
"""
