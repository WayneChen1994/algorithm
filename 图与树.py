# 寻找最大排列问题的递归算法思路的朴素实现方案（平方时间）
def navie_max_perm(M, A=None):
    if A is None:
        A = set(range(len(M)))

    if len(A) == 1: return A

    B = set(M[i] for i in A)

    C = A - B
    if C:
        A.remove(C.pop())
        navie_max_perm(M, A)

    return A


# 引用计数（线性时间）解决最大排列问题
def max_perm(M):
    n = len(M)
    A = set(range(n))
    count = [0]*n

    for i in M:
        count[i] += 1

    Q = [i for i in A if count[i] == 0]

    while Q:
        i = Q.pop()
        A.remove(i)
        j = M[i]
        count[j] -= 1

        if count[j] == 0:
            Q.append(j)

    return A


# 朴素版明星问题的解决方案
def navie_find_star(G):
    n = len(G)
    for u in range(n):
        for v in range(n):
            if u == v:
                continue
            if G[u][v]:
                break
            if not G[v][u]:
                break
        else:
            return u
    return None


# 明星问题的解决方案
def find_star(G):
    n = len(G)
    u, v = 0, 1
    for c in range(2, n+1):
        if G[u][v]:
            u = c
        else:
            v = c

    if u == n:
        c = v
    else:
        c = u

    for v in range(n):
        if v == c:
            continue
        if G[c][v]:
            break
        if not G[v][c]:
            break
    else:
        return c

    return None

