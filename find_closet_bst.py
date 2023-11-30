# Find the closet value in BST to target

def findClosestValueInBst(tree, target):
    # Write your code here.
    curr = tree
    dist = float('inf')
    node = 0
    while curr:
        if target>curr.value:
            abs_dist = abs(target-curr.value)

            if dist>abs_dist:
                dist = abs_dist
                node = curr.value
            curr = curr.right
        else:
            abs_dist = abs(target-curr.value)

            if dist>abs_dist:
                dist = abs_dist
                node = curr.value
            curr = curr.left
    return node


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
