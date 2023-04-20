def m_cross_sub_arr(arr, l, m, h):
    m_l_sum = 0
    m_r_sum = 0
    s = 0
    for i in range(m, l - 1, -1):
        s += arr[i]
        if s > m_l_sum:
            m_l_sum = s
    s = 0
    for i in range(m + 1, h + 1):
        s += arr[i]
        if s > m_r_sum:
            m_r_sum = s
    return m_l_sum + m_r_sum

def m_sub_arr(arr, l, h):
    if l == h:
        return max(arr[l], 0)
    m = (l + h) // 2
    l_sum = m_sub_arr(arr, l, m)
    r_sum = m_sub_arr(arr, m + 1, h)
    c_sum = m_cross_sub_arr(arr, l, m, h)
    return max([l_sum, r_sum, c_sum])



def m_profit(arr):
    p = [arr[i] - arr[i - 1] for i in range(1, len(arr))]
    m = 0
    for i in range(len(p) - 1):
        s = m_sub_arr(p, 0, i) + m_sub_arr(p, i + 1, len(p) - 1)
        if s > m:
            m = s
    m = max(m, m_sub_arr(p, 0, len(p) - 1))
    return m

def m_sub_arr_dp(arr):
    s = 0
    m = 0
    for i in arr:
        if s + i < i:
            s = i
        else:
            s += i
        if s > m:
            m = s
    return m


def m_profit_dp(arr):
    p = [arr[i] - arr[i - 1] for i in range(1, len(arr))]
    m = 0
    for i in range(1, len(p)):
        s = m_sub_arr_dp(p[:i]) + m_sub_arr_dp(p[i:])
        if s > m:
            m = s
    m = max(m, m_sub_arr_dp(p))
    return m


if __name__ == '__main__':
    arr1 = [4000, 6000, 1000, 4000, 2000, 5000]
    arr2 = [1000, 2000, 3000, 4000, 5000]
    arr3 = [7000, 1000, 5000, 3000, 6000, 4000]
    arr4 = [5000, 4000, 3000, 2000, 1000]


    print('Divide and conquer solution:')
    print(arr1, '->', m_profit(arr1))
    print(arr2, '->', m_profit(arr2))
    print(arr3, '->', m_profit(arr3))
    print(arr4, '->', m_profit(arr4))

    print('DP solution:')
    print(arr1, '->', m_profit_dp(arr1))
    print(arr2, '->', m_profit_dp(arr2))
    print(arr3, '->', m_profit_dp(arr3))
    print(arr4, '->', m_profit_dp(arr4))