def isValidSubsequence(array, sequence):
    # Write your code here.

    len_seq = len(sequence)
    j = 0
    for i in range(len(array)):
        if sequence[j]==array[i]:
            j+=1

        if j == len_seq:
            return True

    return False
        
            
    
