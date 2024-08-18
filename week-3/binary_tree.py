class Binary_Trees:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        print("Created node with data", data)

    def insertion(self, value):
        if value < self.data:
            if self.left is None:
                self.left = Binary_Trees(value)
            else:
                self.left.insertion(value)
        else:
            if self.right is None:
                self.right = Binary_Trees(value)
            else:
                self.right.insertion(value)
        print("Inserted", value)

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.data, end=' ')
        if self.right:
            self.right.inorder_traversal()
    def traversal(self,target):
        if self.data ==target:
            return True
        elif target<self.data:
            if self.data is None:
                return False
            else:
                return self.left.traversal(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.traversal(target)

# Example usage
B = Binary_Trees(10)
B.insertion(5)
B.insertion(15)
B.insertion(2)

# To print the tree's in-order traversal
B.inorder_traversal()  # Output: 2 5 10 15

print(B.traversal(20))  # Output: False
print(B.traversal(5))  # Output: True