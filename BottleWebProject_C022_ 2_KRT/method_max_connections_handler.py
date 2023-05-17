import numpy as np


def find_max_degree_vertices(graph, k):
    relat_matrix = np.array(graph)
    A = np.array(graph)

    # вычисление булевой степени матрицы смежности и суммирование с таблицей достижимостей
    for i in range(2, k+1):
        l = np.linalg.matrix_power(relat_matrix.astype(bool), i)
        l = l.astype(int)
        A = np.add(A, l)

    n = len(graph)
    A = A.astype(bool)
    A = A.astype(int)

    print(A)

    max_sum = 0
    for row in A:
        row_sum = max(0, sum(row))
        max_sum = max(max_sum, row_sum)

    for i in range(n):
        if sum(A[i]) == max_sum:
            print(i+1)


find_max_degree_vertices([[0, 1, 1, 0, 0, 1, 1, 0],
                          [1, 0, 1, 0, 0, 0, 0, 0],
                          [1, 1, 0, 0, 0, 1, 1, 0],
                          [0, 0, 0, 0, 0, 0, 1, 0],
                          [0, 0, 0, 0, 0, 1, 1, 1],
                          [1, 0, 1, 0, 1, 0, 0, 0],
                          [1, 0, 1, 1, 1, 0, 0, 0],
                          [0, 0, 0, 0, 1, 0, 0, 0]], 3)

