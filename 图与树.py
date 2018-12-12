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


# 递归版的深度优先搜索
def rec_dfs(G, s, S=None):
    if S is None: S = set()
    S.add(s)

    for u in G[s]:
        if u in S: continue
        rec_dfs(G, u, S)


# 迭代版的深度优先搜索
def iter_dfs(G, s):
    S, Q = set(), []
    Q.append(s)

    while Q:
        u = Q.pop()
        if u in S: continue
        S.add(u)
        Q.extend(G[u])
        yield u


# 通用性的图遍历函数
def traverse(G, s, qtype=set):
    S, Q = set(), qtype()
    Q.add(s)

    while Q:
        u = Q.pop()
        if u in S: continue
        S.add(u)

        for v in G[u]:
            Q.add(v)

        yield u


# 带时间戳的深度优先搜索
def dfs(G, s, d, f, S=None, t=0):
    if S is None: S = set()

    d[s] = t; t += 1

    S.add(s)

    for u in G[s]:
        if u in S: continue
        t = dfs(G, u, d, f, S, t)

    f[s] = t; t += 1

    return t


# 基于深度优先搜索的拓扑排序
def top_sort(G):
    S, res = set(), []

    def recurse(u):
        if u in S: return
        S.add(u)

        for v in G[u]:
            recurse(v)

        res.append(u)

    for u in G:
        recurse(u)

    res.reverse()
    return res


# 迭代深度的深度优先搜索
def iddfs(G, s):
    yielded = set()

    def recurse(G, s, d, S=None):
        if s not in yielded:
            yield s
            yielded.add(s)

        if d == 0: return

        if S is None: S = set()

        S.add(s)

        for u in G[s]:
            if u in S: continue

            for v in recurse(G, u, d-1, S):
                yield v

    n = len(G)

    for d in range(n):
        if len(yielded) == n: break

        for u in recurse(G, s, d):
            yield u
