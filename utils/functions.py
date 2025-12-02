def is_primal(number: int):
    if number < 0:
        raise ValueError("Not Negative")

    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


# print(is_primal(1))
