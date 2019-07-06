def mergeSort(x):
    if (len(x) > 1):
        mid = len(x) // 2

        left = x[:mid]
        right = x[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if (left[i] <= right[j]):
                x[k] = left[i]
                i = i + 1
            else:
                x[k] = right[j]
                j = j + 1
            k = k + 1
        while i < len(left):
            x[k] = left[i]
            i = i + 1
            k = k + 1
        while j < len(right):
            x[k] = right[j]
            j = j + 1
            k = k + 1
    return x

print(mergeSort([1, 5, 3, 2, 4, 7, 8, 3]))
