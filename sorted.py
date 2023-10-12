def reverse_sort_dictionary(inDict):
    if not isinstance(inDict, dict):
        raise TypeError("Input is not a dictionary")

    sorted_items = sorted(inDict.items(), key=lambda x: x[0], reverse=True)

    result = [(name, data[0]) for name, data in sorted_items]

    return result
