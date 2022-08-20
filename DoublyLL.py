class Node:
    def __init__(self,my_record):
        self.record = my_record
        self.forward = None
        self.backward = None

class DLL:
    def __init__(self):
        self.head = None

    def insert(self, record):
        new_node = Node(record)
        if not self.head:                   # insert in an empty DLL
            self.head = new_node
            new_node.forward = None
            new_node.backward = None
        else:
            self.head.backward = new_node
            new_node.forward = self.head
            self.head = new_node

    def repr(self):
        current_node = self.head
        result = []
        while current_node:                                # until current_node is null
            result.append(current_node.record)
            current_node = current_node.forward
        return result

    def delete(self,value):
        if not self.head:
            return "empty DLL"
        if self.head.record == value:              # delete the first element
            self.head = self.head.forward
            self.head.backward = None
            return True

        current_node = self.head
        while current_node:
            if not current_node.forward and current_node.record == value:              # check to delete the last element
                  current_node.backward.forward = None  # to allow the pointer of the prev_node point to null
                  return True

            elif current_node.record == value:            # delete here between elements
                current_node.forward.backward = current_node.backward  # next_node.backward = prev_node
                current_node.backward.forward = current_node.forward   # prev_node.forward = next_node
                return True

            else:
                current_node = current_node.forward    # shift to the next node
        return False







my_dll = DLL()
my_dll.insert(55)
my_dll.insert("good")
my_dll.insert(33)
my_dll.insert(22)
my_dll.insert(40)
my_dll.insert(60)
print(my_dll.repr())
my_dll.delete(55)
my_dll.delete(60)
my_dll.delete(20)
print(my_dll.repr())







