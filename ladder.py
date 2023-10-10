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

if __name__ == "__main__":
    try:
        n = int(input("Enter the ladder height 1-25: "))
        result = my_steps(n)
        print(f"The total number of ways to climb the ladder: {result}")
    except ValueError as x:
        print(f"Error: {x}")
