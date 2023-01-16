import random

input = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]

print(f"Before Shuffle: {input}")

for i in range(5):
    for i in range(len(input)-1):
            x = random.randint(0,i+1)
            input[i],input[x] = input[x], input[i]
    print(input)

#Time Complexity O(n)



