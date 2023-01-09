# Quick sort algorithm uses a divide and conquer technique.

# Requires selecting an efficient pivot point.  All the elements to be sorted will be compared with this pivot. Pivot should be roughly larger that half of the elements.

# Next, the elements are reordered such that all elements less than the pivot are to the left of the pivot and all elements greater than the pivot are to the right. This is referred to as Partitioning.

# Next repeat the above steps recursively to elements smaller than the pivot.  

# Then recursively to the elements greater than the pivot.  

# The base case of the recursion is a single element.

# The time complexity of Quick sort is O(𝑛 log 𝑛) but may degrade to O(𝑛^2) if the pivot points are not near the middle of the list.

def quick_sort(a_list, start, end):
    # list size is 1 or less (which doesn't make sense)
    if start >= end:
        return

    # Call the partition helper function to split the list into two section 
    # divided between a pivot point
    pivot = partition(a_list, start, end)
    quick_sort(a_list, start, pivot-1)
    quick_sort(a_list, pivot+1, end)
        
def partition(a_list, start, end):
    # Select the first element as our pivot point
    pivot = a_list[start]
    
    # Start at the first element past the pivot point
    low = start + 1
    high = end

    while True:
        while low <= high and a_list[high] >= pivot:
            high = high - 1
        while low <= high and a_list[low] <= pivot:
            low = low + 1

        if low <= high:
            a_list[low], a_list[high] = a_list[high], a_list[low]
        else:
            break

    a_list[start], a_list[high] = a_list[high], a_list[start]

    return high


myList = [30, 11, 25, 27, 9, 19, 28, 3, 21, 17]
print("Unsorted Listed: ")
print(myList)
print()
quick_sort(myList,0,len(myList)-1)
print()
print("Sorted Listed: ")
print(myList)