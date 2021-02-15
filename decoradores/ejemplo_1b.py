
# we need to make a new function that Verifies that
# a denominator is different from zero
def catch_zero_denominator(num):
    return num != 0


# then we start to chance the original function
def get_module_division(a, b):
    if catch_zero_denominator(b):
        return a % b
    else:
        return -1


# here also
def get_int_division(a, b):
    if catch_zero_denominator(b):
        return a // b
    else:
        return -1


if __name__ == '__main__':

    print(get_module_division(5, 0))
    print(get_int_division(5, 0))
