# change pathLabel to label
class Node(object):
    def __init__(self, label):
        self.label = label
        self.cost = float('inf')
        self.prev = None
        self.replacedBy = None
        self.replacedByCost = None
        self.replacedDif = None

    def printNode(self):
        print("label:", self.label)
        print("cost:", self.cost)
        print("prev:", self.prev)
        if self.replacedBy != None:
            print("New cost:", self.replacedByCost)
            print("replaced by:", self.replacedBy)
            print("Difference in change", self.replacedDif)

    def replaced(self, label, weight):
        self.replacedByCost = weight
        self.replacedBy = label
        self.replacedDif = self.cost - self.replacedByCost



class Path(object):
    def __init__(self, path, cost):
        self.path = path
        self.cost = cost
        temp = []
        for i in range(len(self.path)):
            temp.append(self.path[i].label)
        self.label = ' '.join(temp)

    def __len__(self):
        return len(self.path)

    def printPath(self):
        print("Cost: ", self.cost)
        print("Path: ", self.label)


    def merge(self, extension):
        totalPath = self.path
        for a in range(len(extension.path)):
            if len(extension)== 0:
                break
            totalPath.append(extension.path[a])
        totalCost = extension.cost + self.cost
        return Path(totalPath, totalCost)
