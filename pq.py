import NodeClass as d

class PriorityQueue(object):
    def __init__(self):
        self.items = [0]

    def __len__(self):
        return len(self.items) - 1

    #parent node = node position / 2
    def upHeap(self):
        i = len(self)
        while i // 2 > 0:
            if self.items[i].cost < self.items[i // 2].cost:
                self.items[i // 2], self.items[i] = self.items[i], self.items[i // 2]
            i = i // 2

    def insert(self, item):
        self.items.append(item)
        self.upHeap()


    def downHeap(self, i):
        while i * 2 <= len(self):
            mc = self.min_child(i)
            if self.items[i].cost > self.items[mc].cost:
                self.items[i], self.items[mc] = self.items[mc], self.items[i]
            i = mc

    #can this be simplified to the last val in array
    def min_child(self, i ):
        if i * 2 + 1 > len(self):
            return i * 2
        if self.items[i * 2].cost < self.items[i * 2 + 1].cost:
            return i * 2
        return i * 2 + 1

    def removeMax(self):
        if len(self) == 0:
            return (0,0)
        min = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self.downHeap(1)
        return min

    def peek(self):
        return self.items[1]

    def lookUp(self, value):
        for i in range(1,len(self.items)):
            if self.items[i].label == value:
                return i
        return False

    def heapify(self, person):
        i = len(self.items)
        while i > 0:
            self.downHeap(i,person)
            i = i - 1


class Stack(object):
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

"""
s = Stack()
s.push("Hello")
s.push("Hellsfo")
s.push("rgs")
print(s.pop())
print(s.pop())


p = PriorityQueue()
test = d.Node('C')
test.cost = 2
p.insert(test)
test = d.Node('D')
test.cost = 3
p.insert(test)
test = d.Node('E')
test.cost = 4
p.insert(test)
test = d.Node('F')
test.cost = 5
p.insert(test)

for i in range(4):
    print(p.removeMax().printNode())
    print()
"""
