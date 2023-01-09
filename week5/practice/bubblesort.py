# The bubble sort makes multiple passes through a list. It compares adjacent items and exchanges
# those that are out of order. Each pass through the list places the next largest value in
# its proper place. In essence, each item “bubbles” up to the location where it belongs.


def bubble_sort(a_list):
    for pass_num in range(len(a_list) - 1, 0, -1):
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp
            print(a_list)


myList = [30, 11, 25, 27, 9, 19, 28, 3, 21, 17]
print("Unsorted Listed: ")
print(myList)
print()
bubble_sort(myList)
print()
print("Sorted Listed: ")
print(myList)