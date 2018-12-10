from random import randrange


lis = [randrange(100) for i in range(10)]

print(lis)


def buddle_sort(seq):
    for i in range(len(seq)-1):
        for j in range(len(seq)-1-i):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]

# buddle_sort(lis)
# print(lis)


def gnome_sort(seq):
    i = 0
    while i < len(seq):
        if i == 0 or seq[i-1] <= seq[i]:
            i += 1
        else:
            seq[i-1], seq[i] = seq[i], seq[i-1]
            i -= 1

# gnome_sort(lis)
# print(lis)


def insert_sort(seq):
    for i in range(len(seq)):
        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1

# insert_sort(lis)
# print(lis)


def select_sort(seq):
    for i in range(len(seq)-1, 0, -1):
        max_j = i
        for j in range(i):
            if seq[j] > seq[max_j]:
                max_j = j
        seq[i], seq[max_j] = seq[max_j], seq[i]


# select_sort(lis)
# print(lis)


def quick_sort(seq):
    if len(seq) < 2: return seq

    pivot = seq[randrange(len(seq)-1)]

    seq.remove(pivot)

    left = [x for x in seq if x <= pivot]
    right = [y for y in seq if y > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


# print(quick_sort(lis))


def merge_sort(seq):
    mid = len(seq) // 2
    left, right = seq[:mid], seq[mid:]

    if len(left) > 1: left = merge_sort(left)
    if len(right) > 1: right = merge_sort(right)

    res = []

    while left and right:
        if left[-1] > right[-1]:
            res.append(left.pop())
        else:
            res.append(right.pop())

    res.reverse()

    return (left or right) + res


# print(merge_sort(lis))


from collections import defaultdict


def count_sort(seq, key=lambda x: x):
    res, temp = [], defaultdict(list)

    for x in seq:
        temp[key(x)].append(x)

    for k in range(min(temp), max(temp)+1):
        res.extend(temp[k])

    return res


# print(count_sort(lis))


def bucket_sort(seq):
    buckets = [0] * (max(seq)+1)
    res = []

    for i in seq:
        buckets[i] += 1

    for j in range(len(buckets)):
        if buckets[j] != 0:
            for k in range(buckets[j]):
                res.append(j)
    return res


# print(bucket_sort(lis))


def radix_sort(seq):
    digit = len(str(max(seq)))

    for i in range(digit):
        buckets = [[] for j in range(10)]

        for s in seq:
            buckets[s//(10**i)%10].append(s)

        seq = [a for b in buckets for a in b]

    return seq


print(radix_sort(lis))


def top_sort(G):
    in_degree = dict((u, 0) for u in G)

    for u in G:
        for v in G[u]:
            in_degree[v] += 1

    Q = [u for u in G if in_degree[u] == 0]
    S = []

    while Q:
        u = Q.pop()
        S.append(u)

        for v in G[u]:
            in_degree[v] -= 1

            if in_degree[v] == 0:
                Q.append(v)

    return S
