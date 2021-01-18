def show_help():
    print("Este es un truco sencillo para enumerar \n"
          "la posición de un elemento :)  \n"
          "---------------------------------------")


def show_index_traditional(elements=("a", "b", "c")):
    i = 1
    for element in elements:
        print(i, element)
        i += 1


def show_index_trick(elements=("a", "b", "c")):
    for i, element in enumerate(elements, 1):
        print(i, element)


if __name__ == "__main__":
    show_help()
    show_index_traditional()
    print("--------")
    show_index_trick()
