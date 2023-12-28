
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def validateBst(tree):
    return bstHelper(tree,float("-inf"),float("inf"))

    
def bstHelper(tree,minValue,maxValue):
    if tree is None:
        return True

    if tree.value < minValue or tree.value>=maxValue:
        return False
    leftValid = bstHelper(tree.left,minValue,tree.value)
    return leftValid and bstHelper(tree.right,tree.value,maxValue)
    
