def memo(n, m):
    mem = {}
    if m and n == 1:
        return 1
    if m and n == 0:
        return 0

    mem = memo(m - 1, n) + memo(m, n-1)
    return mem


memo(2, 3)