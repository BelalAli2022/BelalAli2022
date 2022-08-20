class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def repr(self):
        output = "["
        while self.items:
            output += str(self.items.pop()) + ","
        return output + "]"

"""
x = Queue()

print(x.isEmpty())
x.enqueue(4)
x.enqueue("dog")
x.enqueue(True)
x.enqueue(5678)
print(x.size())
print(x.repr())
"""

