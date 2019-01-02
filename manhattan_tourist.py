def manhattan_tourist(w_south, w_east):
    """
    Find a longest path in a weighted grid G from source (0,0) to sink (m,n). You can move south and east.
    :param w_south: 2D array of weights going south (downward). w_south(i, j) is the weight of the edge between (i − 1, j) and (i, j)
    :param w_east: 2D array of weights going east (rightward). w_east(i, j) is the weight of the edge between (i, j − 1) and (i, j)
    :return: A longest path in G from source to sink as well as the length (weight)
    """
    m = len(w_east)  # n_rows
    n = len(w_south[0])  # n_cols
    print("n_rows: {}. n_cols: {}".format(m, n))
    print("Weight: -1 => south; +1 => east.")
    lookup = [None] * m
    direction = [0] * m  # -1 => south; +1 => east.
    for i in range(m):
        lookup[i] = [None] * n
        direction[i] = [0] * n
    lookup[0][0] = 0
    # go south in the first col
    for i in range(1, m):
        lookup[i][0] = lookup[i - 1][0] + w_south[i - 1][0]
        direction[i][0] = -1

    # go east in the first row
    for j in range(1, n):
        lookup[0][j] = lookup[0][j - 1] + w_east[0][j - 1]
        direction[0][j] = 1

    # the rest, for each cell in each row, left to right
    for i in range(1, m):
        for j in range(1, n):
            from_top = lookup[i - 1][j] + w_south[i - 1][j]
            from_behind = lookup[i][j - 1] + w_east[i][j - 1]
            if from_top > from_behind:
                lookup[i][j] = from_top
                direction[i][j] = 1
            else:
                lookup[i][j] = from_behind
                direction[i][j] = -1

    print("\nWeights")
    for i in range(m):
        for j in range(n):
            print("{}\t".format(lookup[i][j]), end="")
        print()
    print("\nDirections")
    for i in range(m):
        for j in range(n):
            print("{}\t".format(direction[i][j]), end="")
        print()
    print("\nPath")
    i = m - 1
    j = n - 1
    # do until (i,j) = (0,0)
    path = []
    while True:
        path.append(lookup[i][j])
        print("i = {}. j = {}. lookup[i][j] = {}".format(i, j, lookup[i][j]))
        if i == 0 and j == 0:
            break
        from_dir = direction[i][j]
        if from_dir == 1:
            # east, so go backward
            j -= 1
        elif from_dir == -1:
            # south, so go upward
            i -= 1
    path.reverse()
    return path, lookup[m - 1][n - 1]


def manhattan_tourist_test():
    w_east = [
        [3, 2, 4, 0],
        [3, 2, 4, 2],
        [0, 7, 3, 4],
        [3, 3, 0, 2],
        [1, 3, 2, 2]
    ]
    w_south = [
        [1, 0, 2, 4, 3],
        [4, 6, 5, 2, 1],
        [4, 4, 5, 2, 1],
        [5, 6, 8, 5, 3]
    ]
    path, total = manhattan_tourist(w_south, w_east)
    print(" -> ".join([str(p) for p in path]))
    print(total)


manhattan_tourist_test()
