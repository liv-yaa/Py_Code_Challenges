# START SOLUTION #

    higher_than = 0
    lower_than = 101
    guess = None

    while guess != val:
        num_guesses += 1
        guess = (lower_than - higher_than) // 2 + higher_than

        if val > guess:
            higher_than = guess

        elif val < guess:
            lower_than = guess

    # END SOLUTION
