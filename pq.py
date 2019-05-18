class PriorityQueue(object):
    def __init__(self):
        self.items = [0]

    def __len__(self):
        return len(self.items) - 1

    #parent node = node position / 2
    def upHeap(self):
        i = len(self)
        while i // 2 > 0:
            if self.items[i] > self.items[i // 2]:
                self.items[i // 2], self.items[i] = self.items[i], self.items[i // 2]
            i = i // 2

    def insert(self, item):
        self.items.append(item)
        self.upHeap()


    def downHeap(self, i):
        while i * 2 <= len(self):
            mc = self.min_child(i)
            if self.items[i] < self.items[mc]:
                self.items[i], self.items[mc] = self.items[mc], self.items[i]
            i = mc

    #can this be simplified to the last val in array
    def min_child(self, i ):
        if i * 2 + 1 > len(self):
            return i * 2
        if self.items[i * 2] > self.items[i * 2 + 1]:
            return i * 2
        return i * 2 + 1

    def removeMax(self):
        if len(self) == 0:
            return ("No items left to remove")
        max = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self.downHeap(1)
        return max

    def peek(self):
        return self.items[1]

    def heapify(self):
        i = len(self.items)
        while i > 0:
            self.downHeap(i)
            i = i - 1

"""
pq = PriorityQueue()
pq.insert("Sam")
pq.insert("Jesse")
pq.insert("Adam")
pq.insert("Lucy")
pq.insert("Jack")
print(pq.removeMax())
print(pq.removeMax())
print(pq.removeMax())
print(pq.removeMax())
print(pq.removeMax())
print(pq.removeMax())
print(pq.removeMax())
"""
