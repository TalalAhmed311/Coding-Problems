array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
array = [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 11]

def isMonotonic(array):
    # Write your code here.


    
    if len(array)==1 or len(array)==0:
        return True

    I_order = True
    D_order = True

    for i in range(1,len(array)):
        if array[i]< array[i-1]:
            I_order =False

        if array[i] > array[i-1]:
            D_order = False

    return I_order or D_order
    