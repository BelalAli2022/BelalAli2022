class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                 temp = temp.right
            else:
                 return "found"
        return False

    def BFS(self):
        queue = []
        result = []
        queue.append(self.root)
        while len(queue) > 0:
            current_node = queue.pop(0)
            result.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return result

    def dfs_preorder_traversal(self):
        result = []

        def traverse(current_node):        # ( rt L R ) preorder
            if current_node is not None:
                result.append(current_node.value)
                traverse(current_node.left)
                traverse(current_node.right)
        traverse(self.root)
        return result

    def dfs_inorder_traversal(self):
        result = []

        def traverse(current_node):        # ( L rt R ) preorder
            if current_node is not None:
                traverse(current_node.left)
                result.append(current_node.value)
                traverse(current_node.right)
        traverse(self.root)
        return result

    def dfs_postorder_traversal(self):
        result = []

        def traverse(current_node):        # ( L R rt ) preorder
            if current_node is not None:
                traverse(current_node.left)
                traverse(current_node.right)
                result.append(current_node.value)
        traverse(self.root)
        return result

    def findmax(self, max_node):
        while max_node.right:
            max_node = max_node.right
            return max_node

    def delete(self, value):
        if self.root is None:
            return "tree is empty!"
        temp = self.root
        parent = None
        while temp is not None:                   # first search for the item we want to delete
            if value < temp.value:
                parent = temp
                temp = temp.left
            elif value > temp.value:
                parent = temp
                temp = temp.right
            else:                                      # now temp has the node to be deleted

                if not temp.left:                    # if it has one child right or leaf
                    if parent.value > temp.value:      # temp at parent left
                        parent.left = temp.right
                        return
                    else:                              # temp at parent right
                        parent.right = temp.right
                        return

                elif not temp.right:                 # if it has one child left or leaf
                    if parent.value > temp.value:      # temp at parent left
                        parent.left = temp.left
                        return
                    else:                              # temp at parent right
                        parent.right = temp.left
                        return

                else:                               # now have two children
                        max_node = self.findmax(temp)    # to return max_node of the subtree of the temp
                        self.delete(max_node.value)      # delete this max_node to not repeat two nodes
                        temp.value = max_node.value      # return the max_node value to the temp.value
                        return

        return print("not found")


""" that one child condition in delete function is working also at the leaf because we equal the parent pointer with
#  temp.right or temp.left which is equal to None in the two cases if leaf)"""


""" if not temp.left and not temp.right:   # if the element is a leaf

                    if parent.value > temp.value:      # leaf at parent left
                        parent.left = None
                        return
                    else:
                        parent.right = None
                        return """





my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)
print(my_tree.contains(80))

print(my_tree.BFS())

print(my_tree.dfs_preorder_traversal())
print(my_tree.dfs_inorder_traversal())
print(my_tree.dfs_postorder_traversal())