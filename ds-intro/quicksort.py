def quickSort(arr, **kwargs):
    left = kwargs.get("left", 0)
    right = kwargs.get("right", len(arr) - 1)

    if left >= right:
        return

    pivot = arr[int((left + right) / 2)]
    idx = partion(arr, left, right, pivot)
    quickSort(arr, left=left, right=idx-1)
    quickSort(arr, left=idx, right=right)


def partion(arr, left, right, pivot):
    while left < right:
        while arr[left] < pivot:
            left += 1

        while arr[right] > pivot:
            right -= 1

        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return left


a=[1, 4, 2, 57, 2, 12, 3, 141, 12, 23, 5]
quickSort(a)
print(a)
