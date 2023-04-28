def newtonRaphson(g, x0, eps, delta, itermax):
    iter = 0
    xn = x0
    while iter < itermax:
        f, fx = g(xn)
        xn_1 = xn - f/fx  # new root
        if abs(xn_1 - xn) < eps:
            break
        if abs(xn_1 - xn) > delta:
            raise ValueError('Error: Divergence')
        iter += 1
        xn = xn_1
    if iter == itermax:
        raise ValueError('Error: Maximum Number of Iterations')
    x = xn
    return x, iter
