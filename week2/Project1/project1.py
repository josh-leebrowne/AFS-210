# def loop1():
#     # Sum the odd numbers between 1 and 20
#     odd_sum = 0
#     for i in range(20):
#         if (i % 2) == 1:
#             odd_sum += i
#     return odd_sum
#
#
# def loop2():
#     # Sum the even numbers between 1 and 20
#     i = 0
#     even_sum = 0
#     while i < 20:
#         if (i % 2) == 0:
#             even_sum += i
#         i += 1
#     return even_sum


# def loop1Rec(num, odd_sum):
#
#
# # Duplicate the loop1 function using recursion
#
def loop2Rec(num):
    if num <= 1:
        return num
    elif num >= 1 and (num % 2 == 1):
        return num + loop2Rec(num - 1)


num = 20
print(loop2Rec(num))




