
# lets first make two basic functions
def get_module_division(a, b):
    return a % b


def get_int_division(a, b):
    return a//b


if __name__ == '__main__':

    print(get_module_division(5, 2))
    print(get_int_division(5, 2))
