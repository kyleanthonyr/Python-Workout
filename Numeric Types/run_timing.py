def run_timing():
    """ 
    This function asks the user how long (in mins) it took to run 10km.
    It continues to ask how long (in mins) it took for additional runs, 
    until the user presses Enter.

    Then the fxn calculates the average run time over however many runs
    and Exits. 
    """

    counter = 0
    all_runtime = []

    while True:
        # prompt user for run time
        run_time = input("Enter 10 km run time: ")

        # keep a count of runs and track run times
        counter += 1
        all_runtime.append(run_time)

        # Exit program on Enter
        if not run_time:
            break

    # Drop empty character at end of list
    all_runtime = all_runtime[:-1]

    # Convert to int type
    all_runtime = [int(x) for x in all_runtime]

    # Sum run times
    sum_runtime = sum(all_runtime)

    # Calculate average run time
    avg_runtime = sum_runtime / (counter - 1)

    # Output average run times and num of runs
    print(
        f"You had an average run time of {round(avg_runtime, 1)} mins over {counter - 1} runs.")


run_timing()
