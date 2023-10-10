def my_steps(n):
    if n < 1 or n > 25:
        raise ValueError("Input must be between 1 and 25")

    if n <= 2:
        return n

    ways = [0] * (n + 1)
    ways[1] = 1
    ways[2] = 2

    for i in range(3, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]

    return ways[n]
