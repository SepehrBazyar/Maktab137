def is_primal(number: int):
    for i in range(2, number):
        if number % i == 0:
            return False

    return True


print(is_primal(1))
