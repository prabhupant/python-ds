def prefix_sums(ls: [int]) -> [int]:
    """
    Returns list of prefix sums for given list of integers.
    """
    n = len(ls)
    total = 0
    sums = [0] * n
    for i in range(n):
        total += ls[i]
        sums[i] = total
    return sums
