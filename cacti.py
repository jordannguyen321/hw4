def cacti_number(arr):
    def is_valid(x, y):
        return 0 <= x < len(arr) and 0 <= y < len(arr[0])

    def can_place_cactus(x, y):
        return (
            is_valid(x, y) and
            arr[x][y] == 0 and
            all(arr[i][j] != 1 for i in range(x - 1, x + 2) for j in range(y - 1, y + 2) if is_valid(i, j))
        )
    count = 0
    for x in range(len(arr)):
        for y in range(len(arr[0])):
            if can_place_cactus(x, y):
                count += 1
                arr[x][y] = 1
    return count
