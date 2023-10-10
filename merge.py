def merge_list(l1, l2):
    if not (isinstance(l1, list) and isinstance(l2, list)):
        raise TypeError("Both inputs must be lists")
    
    # Merges both of the lists
    mergedList = l1 + l2

    #Simple bubble sort to sort the lists
    x = len(mergedList)
    for i in range(x - 1):
        for j in range(0, x - i - 1):
            if mergedList[j] > mergedList[j + 1]:
                mergedList[j], mergedList[j + 1] = mergedList[j + 1], mergedList[j]

    return mergedList
