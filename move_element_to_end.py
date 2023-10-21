# Given an integer array and an integer
# Task is to move the given integer value in the end of array

def moveElementToEnd(array, toMove):
    # Write your code here.

    r = len(array)-1
    l = 0

    while l<r:
        if array[l]==toMove:
            if array[r] != toMove:
                array[l] = array[r]
                array[r] = toMove
                l+=1
                r-=1
                
            else:
                r-=1
        else:
            l+=1

        
    return array
            
