def loop1():
    # Sum the odd numbers between 1 and 20
    odd_sum = 0
    for i in range(20):
        if (i % 2) == 1:
            odd_sum += i
    return odd_sum


def loop2():
    # Sum the even numbers between 1 and 20
    i = 0
    even_sum = 0
    while i < 20:
        if (i % 2) == 0:
            even_sum += i
        i += 1
    return even_sum

print(loop1())
print(loop2())


def loop1Rec(num, current, sum = 0):
    
    if current == num:
        return sum
    elif (current % 2 == 1 and current != num):
        sum += current
        return loop1Rec(num, current + 1, sum)
    else: return loop1Rec(num, current + 1, sum)


num = 20
current = 0
sum = 0
print(loop1Rec(num, current, sum))



def loop2Rec(num, current, sum = 0):
    
    if current == num:
        return sum
    elif (current % 2 == 0 and current != num):
        sum += current
        return loop2Rec(num, current + 1, sum)
    else: return loop2Rec(num, current + 1, sum)


num = 20
current = 0
sum = 0
print(loop2Rec(num, current, sum))





def loop3Rec(num, odd_sum=0, val=0):
    val = val or 1
    if (val == num):
        return odd_sum
    elif (val % 2 == 1):
        odd_sum += val
    val+=1
    return loop3Rec(num, odd_sum, val)

print(loop3Rec(20))