# Non-Constructible change

# Logic
# initialize change with 0
# sort coins array
#Iterate through it
# Add the coin to change if coin<= change+1
# Return change+1 if coin>change+1

coins = [1, 5, 1, 1, 1, 10, 15, 20, 100]


change = 0
soretedCoins = sorted(coins)

for coin in soretedCoins:

    if coin > change+1:
        break 

    change += coin
    print(f"Coin {coin} and Change {change}")
        

print(change+1)

# 
#
#
#
#