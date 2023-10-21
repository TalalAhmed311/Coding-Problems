def twoNumberSum(array, targetSum):
    # Write your code here.
    temp = []
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):

            if array[i]+array[j]==targetSum:
                temp.append(array[i])
                temp.append(array[j])
                return temp
        

    return temp
        
