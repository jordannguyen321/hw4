def my_steps(x):
    if x < 1 or x > 25:
        raise ValueError("Input must be between 1 and 25")

    if x <= 2:
        return x

    num = [0] * (x + 1)
    num[1] = 1
    num[2] = 2

    for i in range(3, x + 1):
        num[i] = num[i - 1] + num[i - 2]

    return num[n]
