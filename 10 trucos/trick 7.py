def show_help():
    print("Con este truco podemos obtener fácilmente\n"
          "la veces que se repite cada elemento de una lista\n"
          "---------------------------------------")


def get_counter_traditional(elements=("a", "a", "a", "b", "b", "c")):
    clean = dict()
    for element in set(elements):
        clean[str(element)] = elements.count(element)

    return clean


def get_counter_trick(elements=("a", "a", "a", "b", "b", "c")):
    from collections import Counter
    return dict(Counter(elements))


if __name__ == "__main__":
    show_help()
    print(get_counter_traditional())
    print("--------")
    print(get_counter_trick())
