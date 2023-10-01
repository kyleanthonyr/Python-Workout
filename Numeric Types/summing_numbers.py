def mysum(*args):
    """
    A simple function that replicates the built-in sum function.
    """
    sum = 0
    for num in args:
        sum += num
    return sum


sum = mysum(1, 2, 4, 5, 6, 5)
print(sum)
