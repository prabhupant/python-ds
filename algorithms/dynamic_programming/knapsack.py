
def unbounded_knapsack(W, v, w):
   
    m = [0 for i in range(W + 1)]
 
    start = min(w)
    for i in range(start, W + 1):
        m[i] = m[i-1]
        for k, vk in enumerate(v):
            if w[k] <= i and m[i] < m[i - w[k]] + vk:
                m[i] = m[i - w[k]] + vk

    return m[W]

def zero_one_knapsack(W, v, w):

    m = [[0 for k in range(W + 1)] for i in range(len(w) + 1)]

    for i in range(len(v)):
        m[i][0] = 0

    for i in range(W + 1):
        m[0][i] = 0

    start = min(w)
    for item in range(1, len(v) + 1):
        for max_w in xrange(start, W + 1):
            w_i = w[item - 1]

            if w_i > max_w:
                m[item][max_w] = m[item - 1][max_w]
            else:
                m[item][max_w] = max(m[item - 1][max_w], m[item - 1][max_w - w_i] + w_i)

    return m[len(v)][W]