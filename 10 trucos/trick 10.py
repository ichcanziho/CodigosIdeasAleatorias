def show_help():
    print("Con este truco podemos obtener la \n"
          "transpuesta de una matriz de forma simple.\n"
          "---------------------------------------")


def show_matrix(matrix):

    for row in matrix:
        print(row)


def transpose(matrix):

    return map(list, zip(*matrix))


if __name__ == "__main__":
    show_help()
    matrix = [[1, 2, 3], [4, 5, 6]]
    show_matrix(matrix)
    print("-------")
    show_matrix(transpose(matrix))

