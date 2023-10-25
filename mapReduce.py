# Count values to illustrate Map-Reduce implmentation

my_array = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7,8]
# print(len(my_array))


# Step 1:  Split the array 
# Suppose we trying to create distributing system setting and send each chunk(split) of data to a seperate node

spliting_factor = 3
# Defining an array of splits 
splits = []
for i in range(0,len(my_array),spliting_factor):
    splits.append(my_array[i:i+spliting_factor])



# Step 2: Create a Map 
# Initialize a mapping as array for illustrating nodes in distributed setting
# each value of array contains the mapping of values for each node

mapping = []

for split in splits:
    temp = {}
    for value in split:
        if value not in temp:
            temp[value] = 1
        else:
            temp[value] += 1

    mapping.append(temp)

# Step 3: Reduce functionality
# Collect the responses which came from every node and combine them
reduce = {}
for node_response in mapping:
    for key,value in node_response.items():
        if key not in reduce:
            reduce[key] = value
        else:
            reduce[key] += value 


print(mapping)
print(reduce)
