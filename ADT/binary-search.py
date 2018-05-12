def binarySearch1(alist, item):  # Iterative
    lf = 0
    rt = len(alist) - 1
    while lf <= rt:
        mid = (lf + rt) // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            rt = mid - 1
        else:
            lf = mid + 1
    return False


def binarySearch(alist, item):  # Recursive
    if not alist:
        return False
    mid = len(alist) // 2
    if alist[mid] == item:
        return True
    elif item < alist[mid]:
        return binarySearch(alist[:mid], item)  # Actually time complexity is O(k) because of slicing
    else:
        return binarySearch(alist[mid + 1:], item)


if __name__ == "__main__":
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
    alist = []
    blist = [1]
    print(binarySearch(alist, 1))
    print(binarySearch(blist, 1))
    print(binarySearch(testlist, 3))
    print(binarySearch(testlist, 13))
