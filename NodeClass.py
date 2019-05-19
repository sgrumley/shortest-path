
class Node():
    def __init__(self, label):
        self.label = label
        self.cost = float('inf')
        self.prev = None

    def printNode(self):
        print("label:", self.label)
        print("cost:", self.cost)
        print("prev:", self.prev)
