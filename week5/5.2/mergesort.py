def mergeSort(nlist):
    print("Splitting ",nlist)

    if len(nlist) > 1:
        middle = len(nlist)//2
        l = nlist[:middle]
        r = nlist[middle:]
        mergeSort(l)
        mergeSort(r)
        nlist = merge(nlist,l,r)

    print("Merging ",nlist)

def merge(nlist,lefthalf,righthalf):
    i=j=k=0       
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            nlist[k]=lefthalf[i]
            i=i+1
        else:
            nlist[k]=righthalf[j]
            j=j+1
        k=k+1
    while i < len(lefthalf):
        nlist[k]=lefthalf[i]
        i=i+1
        k=k+1
    while j < len(righthalf):
        nlist[k]=righthalf[j]
        j=j+1
        k=k+1
    return nlist

list = [55,31,26,20,63,7,51,74,81,40]
n = len(list)
mergeSort(list)
print(list)