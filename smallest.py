def smallest(elements, done=False):
    seconds = {}
    while len(elements) > 1:
        mins = []
        i = 0
        while i < len(elements):
            if i + 1 < len(elements):
                smaller = min(elements[i], elements[i + 1])
                larger = max(elements[i], elements[i + 1])
                mins += [smaller]
                seconds[smaller] = seconds.get(smaller, []) + [larger]
            else:
                mins += [elements[i]]
            i += 2
        elements = mins
    smallest = elements[0]
    if done:
        return smallest
    else:
        return seconds[smallest]


def next_smallest(elements, done=False):
    """
    Give an algorithm to find the second smallest element in a list of n
    elements.
    Worst Case Total Comparisons:
        n + ceiling(lg n) - 2
    """
    smalls = smallest(elements)
    seconds = smallest(smalls, done)
    return seconds


def third_smallest(elements, done=False):
    """
    Give an algorithm to find the 3rd smallest element in a list
    Worst Case Total Comparisons:
        n - 1 + [ceiling(lg n) + ceiling(lg lg n) - 2] + ceiling(lg n) - 2
    """
    smalls = next_smallest(elements)
    seconds = smallest(smalls, done)
    return seconds

if __name__ == '__main__':
    import random
    L = random.sample(range(0, 30), 10)
    print L
    print "2nd smallest:", next_smallest(L, True)
    print "3rd smallest:", third_smallest(L, True)
