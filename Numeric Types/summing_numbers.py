def mysum(*args):
    """
    A simple function that replicates the built-in sum function.
    """
    sum = 0
    for num in args:
        sum += num
    return sum


sum = mysum(1, 2, 4, 5, 6, 5)
print(f"The sum of the inputted values is {sum}")


def my_sum2(*args, start=0):
    """
    This fxn replicates the built-in sum fxn by adding the option start value.
    """
    sum = start
    for num in args:
        sum += num
    return sum


start5 = my_sum2(*[1, 2, 3, 4], 5)
print(f"Starting with 5: {start5}")
