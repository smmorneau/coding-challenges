"""
Consider a sorted list L of n integers, each of which must be distinct (that
is, the list contains no duplicates). L may contain negative elements. Give
an algorithm (describe in English, and then give pseudo-code) that finds all
indicies i such that L[i] = i. Your algorithm should run in O(lg n + k) time,
where k is the number of elements i such that L[i] = i.
"""


def find_indicies(L, index=0):
    if len(L) <= 2:
        solution = []
        for j in range(len(L)):
            if L[j] == j + index:
                solution.append(L[j])
            if L[j] > j + index:
                break
        return solution

    m = len(L) / 2
    if L[m] > m + index:
        return find_indicies(L[:m], index)
    elif L[m] < m + index:
        return find_indicies(L[m:], index + m)
    else:
        solution = [L[m]]
        for j in range(m-1, -1, -1):
            if L[j] != j + index:
                break
            solution.append(L[j])
        for j in range(m+1, len(L)):
            if L[j] != j + index:
                break
            solution.append(L[j])
        return solution

if __name__ == '__main__':
    import random
    L = random.sample(range(-5, 15), 10)
    L.sort()
    print L
    print find_indicies(L)
