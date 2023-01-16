
# Coin Change problem - Example of Greedy Algorithm

coins = [1, 5, 10, 25]
changeNeeded = 46


def changeDue(change):
    coinsUsed = []
    coins.reverse()
    for coin in coins:
        while coin <= change:
            change -= coin
            coinsUsed.append(coin)
        if change == 0:
            break
    return coinsUsed
    
print(changeDue(changeNeeded))   