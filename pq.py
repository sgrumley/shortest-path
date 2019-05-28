class PriorityQueue(object):

    def __init__(self):
        self.items = [0]
        self.available_items = set()

    # overide len function to not include 0
    def __len__(self):
        return len(self.items) - 1

    def up_heap(self):
        i = len(self)
        while i // 2 > 0:
            if self.items[i].cost < self.items[i // 2].cost:
                self.items[i // 2], self.items[i] = self.items[i], self.items[i // 2]
            i = i // 2

    # insert item to last position then upheap to satisfy heap rules
    def insert(self, item):
        self.items.append(item)
        self.available_items.add(item.label)
        self.up_heap()

    # while node has children find the biggest and compare it
    def down_heap(self, i):
        while i * 2 <= len(self):
            mc = self.min_child(i)
            if self.items[i].cost > self.items[mc].cost:
                self.items[i], self.items[mc] = self.items[mc], self.items[i]
            i = mc

    # determine which child is bigger and return its index
    def min_child(self, i ):
        if i * 2 + 1 > len(self):
            return i * 2
        if self.items[i * 2].cost < self.items[i * 2 + 1].cost:
            return i * 2
        return i * 2 + 1

    # delete function that swaps max value with last value then downheaps the swapped value to satisfy heap rules
    def remove_min(self):
        if len(self) == 0:
            return None
        min = self.items[1]
        self.available_items.remove(min.label)
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self.down_heap(1)
        return min

    # Function that uses set to verify the value is in the queue and returns index if yes
    def look_up(self, value):
        if value in self.available_items:
            for i in range(1,len(self.items)):
                if self.items[i].label == value:
                    return i
        return False

class Stack(object):
    def __init__(self):
        self.items = []
        self.s = set()

    def print_stack(self):
        for i in range(len(self.items)):
            print(self.items[i].label, end = " ")
        print()
        for i in range(len(self.items)):
            print(self.items[i].cost, end = " ")
        print()
        for i in range(len(self.items)):
            print(self.items[i].prev, end = " ")
        print()

    def __len__(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)
        self.s.add(item.label)

    def check_up(self, val):
        if val in self.s:
            return True
        else:
            return False
