from random import randrange
lis = [randrange(100) for x in range(10)]
print(lis)


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


def buddle_sort(seq):
    for i in range(len(seq)-1):
        for j in range(len(seq)-1-i):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]


# buddle_sort(lis)
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





