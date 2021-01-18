def show_help():
    print("Este es un truco muy simple nos permite \n"
          "eliminar elementos repetidos de una lista  \n"
          "---------------------------------------")


def remove_repeated_traditional(elements=("a", "a", "a", "b", "b", "c")):
    clean = list()
    for element in elements:
        if element not in clean:
            clean.append(element)

    return clean


def remove_repeated_trick(elements=("a", "a", "a", "b", "b", "c")):

    return list(set(elements))


if __name__ == "__main__":
    show_help()
    print(remove_repeated_traditional())
    print("--------")
    print(remove_repeated_trick())