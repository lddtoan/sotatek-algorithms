def n_arr(arr):
    s = sum(arr)
    return [s - i for i in arr]

if __name__ == '__main__':
    arr1 = [1, 2, 6, 10]
    arr2 = [6.1, -1.2, 22, 0.6]
    arr3 = [1, 2, 3]
    arr4 = [2, 0, 2, 1]

    print(arr1, '-> ', n_arr(arr1))
    print(arr2, '-> ', n_arr(arr2))
    print(arr3, '->', n_arr(arr3))
    print(arr4, '->', n_arr(arr4))