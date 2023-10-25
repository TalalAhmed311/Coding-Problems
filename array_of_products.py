arr = [5,1,4,2]

def arrayOfProducts(array):
    # Write your code here.

    stack = []

    for i in range(len(array)):
        temp = array.copy()
        temp.pop(i)
        prod = 1
        for j in temp:
            prod*=j

        stack.append(prod)

    return stack