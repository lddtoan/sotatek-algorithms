def m_profit(arr):
    p = [arr[i] - arr[i - 1] for i in range(1, len(arr))]
    return sum(filter(lambda x: x > 0, p))


if __name__ == '__main__':
    arr1 = [1000, 2000, 3000, 4000, 5000]
    arr2 = [7000, 1000, 5000, 3000, 6000, 4000]
    arr3 = [5000, 4000, 3000, 2000, 1000]

    print(arr1, '->', m_profit(arr1))
    print(arr2, '->', m_profit(arr2))
    print(arr3, '->', m_profit(arr3))