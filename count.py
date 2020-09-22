import heapq

def k_merge(*args):
    """
    Given an arbitrary number of sorted lists, build a merged sorted list.
    >>> k_merge()
    >>> k_merge([])
    []
    >>> k_merge([1], [1])
    [1, 1]
    >>> k_merge([1, 3], [5], [2, 4])
    [1, 2, 3, 4, 5]
    >>> k_merge([1, 1, 1], [3], [2, 2])
    [1, 1, 1, 2, 2, 3]
    >>> k_merge([1,4,5], [1,3,4], [2,6])
    [1, 1, 2, 3, 4, 4, 5, 6]
    """
    if not args:
        return
    return list(heapq.merge(*args))







import heapq

def k_merge(*args):
    """
    Given an arbitrary number of sorted lists, build a merged sorted list.
    >>> k_merge()
    >>> k_merge([])
    []
    >>> k_merge([1], [1])
    [1, 1]
    >>> k_merge([1, 3], [5], [2, 4])
    [1, 2, 3, 4, 5]
    >>> k_merge([1, 1, 1], [3], [2, 2])
    [1, 1, 1, 2, 2, 3]
    >>> k_merge([1,4,5], [1,3,4], [2,6])
    [1, 1, 2, 3, 4, 4, 5, 6]
    """
    if not args:
        return
    result = []
    for i in args:
        for j in i:
            result.append(j)
    heapq.heapify(result)
    return [heapq.heappop(result) for _ in range(len(result))]
