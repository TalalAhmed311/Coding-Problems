arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

a1 = [-1, 3, 5, 10, 20, 28]
a2 = [15, 17, 26, 134, 135]

sortedarrayOne = sorted(arrayOne)
sortedarrayTwo = sorted(arrayTwo)
print(sortedarrayTwo)
i = 0
j = 0
arrOneLen = len(arrayOne)
arrTwoLen = len(arrayTwo)
dist = float("inf")
abs_dist = float("inf")
pair = []
while i<arrOneLen and j<arrTwoLen:
    firstNum = sortedarrayOne[i]
    secondNum = sortedarrayTwo[j]
    
    if firstNum==secondNum:
        print([firstNum,secondNum])
        break 
        

    if firstNum<secondNum:
        abs_dist = secondNum-firstNum
        i+=1
    elif secondNum<firstNum:
        abs_dist = firstNum - secondNum
        j+=1

    if dist>abs_dist:
        dist = abs_dist
        pair = [firstNum,secondNum]