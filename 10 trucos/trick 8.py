def show_help():
    print("Con este truco podemos obtener la moda de una lista\n"
          "en otras palabras el valor que más se repite\n"
          "---------------------------------------")


def get_most_common_element_traditional(elements=("a", "a", "a", "b", "b", "c")):
    most_common = ""
    repetitions = 0
    for element in set(elements):
        count = elements.count(element)
        if count > repetitions:
            most_common = element
            repetitions = count

    return most_common


def get_most_common_element_trick(elements=("a", "a", "a", "b", "b", "c")):

    return max(set(elements), key=elements.count)


if __name__ == "__main__":
    show_help()
    print(get_most_common_element_traditional())
    print("--------")
    print(get_most_common_element_trick())