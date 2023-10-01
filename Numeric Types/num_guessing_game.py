import random


def guessing_game():
    """ 
    This function chooses a random number between 0 and 100 (incl),
    then asks user to guess chosen number.

    Each time the number enters a guess, the program returns "Too
    high", "Too low" or "Just right".

    If the user guesses correctly, the program exits. Otherwise, 
    the user is prompted to guess again.

    """

    # selects a random numer
    num = random.randint(0, 100)

    # prompts use to guess
    user_guess = int(input("Guess which number was chosen (0-100): "))

    while user_guess != num:
        if user_guess == num:
            # print("Just right!")
            break
        if user_guess < num:
            user_guess = int(input("Too low! Try again: "))
        else:
            user_guess = int(input("Too high! Try again: "))
    print("Just right!")


guessing_game()
