# change pathLabel to label
class Node(object):
    def __init__(self, label):
        self.label = label
        self.cost = float('inf')
        self.prev = None

    def printNode(self):
        print("label:", self.label)
        print("cost:", self.cost)
        print("prev:", self.prev)

class Path(object):
    def __init__(self, path, cost):
        self.path = path
        self.cost = cost
        temp = []
        for i in range(len(self.path)):
            temp.append(self.path[i].label)
        self.label = ''.join(temp)

    def __len__(self):
        return len(self.path)

    def printPath(self):
        print("Cost: ", self.cost)
        print("Path: ")
        for i in range(len(self.path)):
            print( self.path[i].label, end= " ")
        print()
        print()
