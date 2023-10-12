def my_steps(n):
    if n < 1 or n > 25:
        raise ValueError("Input is not between 1-25")

    if n <= 2:
        return x

    num = [0] * (n + 1)
    num[1] = 1
    num[2] = 2

    for i in range(3, n + 1):
        num[i] = num[i - 1] + num[i - 2]

    return num[n]
