class Node:
    def __init__(self, my_record):
        self.next_node = None
        self.record = my_record


class Linkedlist:
    def __init__(self):
        self.head = None

    def insert(self, record):
        new_node = Node(record)
        new_node.next_node = self.head
        self.head = new_node

    def delete(self,record):
        if self.head is None:
            return "empty linked list"
        if self.head.record == record:
            self.head = self.head.next_node
            return True
        current_node = self.head
        while current_node and current_node.next_node:
            if current_node.next_node.record == record:
                current_node.next_node = current_node.next_node.next_node      # delete here
                return True
            else:
                current_node = current_node.next_node                        # shift here
        return False

    def __str__(self):
        result = []
        current_node = self.head
        while current_node:
              result.append(current_node.record)
              current_node = current_node.next_node
        return result

    def contains(self, record):
        current_node = self.head
        while current_node:
            if current_node.record == record:          # found my element
                return True
            current_node = current_node.next_node     # shift
        return False




my_link = Linkedlist()
my_link.insert(34)
my_link.insert(True)
my_link.insert("good !")
my_link.insert(44)
print(my_link.__str__())
print(my_link.delete(44))
print(my_link.__str__())
print(my_link.contains(44))

mylist = ['d', 'a', 'c', 'b']
mylist.sort() # Returns None
print(mylist) # ['a', 'x', 'y', 'z', 'd', 'e', 'f']
