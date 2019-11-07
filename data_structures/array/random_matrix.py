def random_matrix(n):
    """ Generate random n x n matrix without repeated entries in rows or columns.
    The entries are integers between 1 and n.
    """
    from random import shuffle

    a = list(range(n + 1))
    shuffle(a)

    # Use slicing to left rotate
    m = [a[i:] + a[:i] for i in range(n + 1)]

    # Shuffle rows in matrix
    shuffle(m)

    # Shuffle cols in matrix (optional)
    m = list(map(list, zip(*m)))  # Transpose the matrix
    shuffle(m)

    return m


m = random_matrix(9)
print('\n'.join(map(str, m)))
