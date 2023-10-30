# a function that writes that takes an  unordered listthat returns the array's majority element
# Constraint: 
# Don't sort it and use constant space 


# Solution 1:
# Time = O(n) Space = O(n)
def majorityElement(array):
    # Write your code here.

    majority = {}

    for i in range(len(array)):
        if array[i] not in majority:
            majority[array[i]] = 1
        else:
            majority[array[i]] += 1

    if majority:
        
        return max(majority, key=lambda k: majority[k])
    
    return -1


# Solution 2:
# Time = O(n) Space = O(1)
def majorityElement(array):
    # Write your code here.

    counter = 0
    maj_elem = None
    for value in array:

        if counter==0:
            maj_elem = value

        if value==maj_elem:
            counter+=1
        else:
            counter-=1
        
    return maj_elem

