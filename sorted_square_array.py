array = [1, 2, 3, 5, 6, 8, 9]
temp = [0 for _ in range(len(array))]
# print(temp)
array = [0, 25, 25, 100, 100]
array = [-50, -13, -2, -1, 0, 0, 1, 1, 2, 3, 19, 20]
# array = [-10, -5, 0, 5, 10]
array = [-10, -5, 0, 5, 10]

l = 0
r = len(array)-1
temp = [0 for _ in range(len(array))]
while l<=r:

    if abs(array[l])>abs(array[r]):
        temp[l] = array[r]**2
        temp[r] = array[l]**2
        

    elif abs(array[l])<abs(array[r]):
        temp[l] = array[l]**2
        temp[r] = array[r]**2

    elif abs(array[l])==abs(array[r]):
        if l==r:
            temp[l] = array[l]**2

        else:

            temp[l] = array[l]**2
            temp[r] = array[r]**2

    l+=1
    r-=1


print(temp)
print(l,r)
        