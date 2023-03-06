def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the maximum element in the remaining unsorted array
        max_index = i
        for j in range(i+1, n):
            if arr[j] > arr[max_index]:
                max_index = j

        # Swap the found maximum element with the last element
        arr[max_index], arr[-1] = arr[-1], arr[max_index]

    return arr
