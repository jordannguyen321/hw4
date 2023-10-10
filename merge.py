def merge_list(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Both inputs must be lists")

    # Merges both lists into one sorted list
    merged_list = list1 + list2

    # Bubble sort 
    n = len(merged_list)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if merged_list[j] > merged_list[j + 1]:
                merged_list[j], merged_list[j + 1] = merged_list[j + 1], merged_list[j]

    return merged_list
