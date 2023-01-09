# Sequential (Linear) Search on Unordered List
# Time Complexity = O(n)
def linear_search(list, term):
	list_size = len(list)
	for i in range(list_size):
		if term == list[i]:
			return True
	return False

myList1 = [11, 30, 25, 27, 9, 19, 28, 3, 21, 17]
print(linear_search(myList1,4))

# Sequential (Linear) Search on Ordered List
# Time Complexity = O(n)
def linear_search(list, term):
	list_size = len(list)
	for i in range(list_size):
		if term == list[i]:
			return True
		elif list[i] > term:
			return False
	return False

myList2 = [3, 9, 11, 17, 19, 21, 25, 27, 28, 30]
print(linear_search(myList1,4))