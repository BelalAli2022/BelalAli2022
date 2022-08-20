class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items==[]

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        self.items.pop()

    def removeRear(self):
        self.items.pop(0)

    def size(self):
        return len(self.items)

    def elements(self):
        output = "["
        while self.items:
            output += str(self.items.pop()) + ","
        return output + "]"

x = Deque()
print(x.isEmpty())
x.addFront(3)
x.addFront("belal")
x.addFront(True)
print(x.size())
#x.removefront()
print(x.elements())
print(x)