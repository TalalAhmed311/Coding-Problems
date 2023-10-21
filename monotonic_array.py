array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
array = [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 11]

flag = True
prev = array[0]

order = 0
if prev>array[1]:
    order = 1

for i in range(1,len(array)):
    if order==0 and prev<=array[i]:
        prev = array[i]

    elif order==1 and prev>=array[i]:
        prev = array[i]

    else:
        print(prev)
        print(array[i])
        flag = False
        break

print(flag)