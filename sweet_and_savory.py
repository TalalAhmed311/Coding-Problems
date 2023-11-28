# Given an array of dishes. Negative represents sweet dish and positive represent savory dish
# Goal is to find the best pair when get added returns a umber that is closet to target

def seperate_array(arr):
    postive,negative = [],[]

    for value in arr:
        if value>=0:
            postive.append(value)
        else:
            negative.append(value)

    return sorted(postive), sorted(negative,reverse=True)


def sweetAndSavory(dishes,target):
    positive, negative = seperate_array(dishes)

    # Check if any of array is empty

    if positive==[] or negative==[]:
        return [0,0]
    max_val = float("-inf")
    pair = [0,0]
    i, j = 0, 0

    while i<len(positive) and j<len(negative):

        value = positive[i] + negative[j]

        if value<=target:
            if max_val<value:
                max_val = value
                pair = [positive[i],negative[j]]
            
            i+=1
        else:
            j+=1

            
    return pair

