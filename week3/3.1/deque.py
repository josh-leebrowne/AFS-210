from collections import deque 

# Deque is short for Double Ended Queue.  It is a hybrid between a Stack and a Queue providing 
# the functionality of both in one data structure.
#
# The time complexity of adding or removing an item on either side of a deque 
# takes constant time O(1).
#
# Deque Operations:
# append(item)          : Insert the item to the right end of deque.  Same as stack "push" method
# appendleft(item)      : Insert the item to the left end of deque.  Same as queue "enqueue" method
# insert(index,item)    : Insert the item at the given index
# pop()                 : Delete an item from the right end of deque.  Same as the stack "pop"                                method
# popleft()             : Delete an item from the left end of deque. Same as queue "dequeue" method
# remove(item)          : Remove the first occurrence of the item
# count(item)           : Return the total number of occurrences of the given value
# rotate(n)             : Rotate the deque n number of times.  
#                         A positive value rotates to the right
#                         A negative value rotates to the left
# reverse()             : Reverse the order of the deque


#                 Deque
#  <---- Left Side     Right Side ---->
#
# -------------------------------------
# |  1  |  2  |  3  |  4  |  5  |  6  |
# -------------------------------------
#
#  <---- Queue Like     Stack Like ---->

months = deque(['February','March','April','June','July','August','September','October', 'November'])


# months.append('December')
# months.appendleft('January')
# months.pop()
# print(months)
# months.popleft()
# print(months)

months.rotate(4)
print(months)