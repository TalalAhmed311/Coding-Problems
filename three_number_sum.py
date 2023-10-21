# Brute Force

def threeNumberSum(array, targetSum):
    # Write your code here.
    triplets = []
    for i in range(len(array)-2):
        for j in range(i,len(array)-1):
            for k in range(j+1,len(array)):

                if array[i]+array[j]+array[k]==targetSum:
                    triplets.append(sorted([array[i],array[j],array[k]]))
                    
                
    return triplets


# Optimize solution O(n^2) 
def threeNumberSum(array, targetSum):
    sortArr = sorted(array)
    triplets = []
    for i in range(len(sortArr)):
        curr = sortArr[i]
        l = i+1
        r = len(sortArr)-1

        while l<r:
            cs = curr + sortArr[l] + sortArr[r]

            if cs == targetSum:
                triplets.append([curr,sortArr[l],sortArr[r]])
                l+=1
                r-=1
            elif cs<targetSum:
                l+=1
            else:
                r-=1
                
        
    return triplets
