# an especial case of decorators are called CONSTRUCTORS
# constructors are a functions that allows you to make new
# instances of a family of functions

def multiplier_constructor(value):
    def multiplier(num):
        return value * num
    return multiplier


by_twice = multiplier_constructor(2)
by_ten = multiplier_constructor(10)

if __name__ == '__main__':

    print(by_twice(10))
    print(by_ten(5))

