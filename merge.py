def merge_list(list1, list2):
    if not (isinstance(list1, list) and isinstance(list2, list)):
        raise TypeError("Both inputs must be lists")
    
    # Merges both of the lists
    merged_list = list1 + list2

    #Simple bubble sort to sort the lists
    x = len(merged_list)
    for i in range(x - 1):
        for j in range(0, x - i - 1):
            if merged_list[j] > merged_list[j + 1]:
                merged_list[j], merged_list[j + 1] = merged_list[j + 1], merged_list[j]

    return merged_list
