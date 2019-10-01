# divide and conquer
from sys import maxsize

def max_sub_arr(arr, l, r):
    if l == r:
        return arr[l]
    mid = (l+r)//2
    L = max_sub_arr(arr, l, mid)
    R = max_sub_arr(arr, mid+1, r)
    C = max_sub_arr_crossing(arr, l, mid, r)
    return max(L, R, C)

def max_sub_arr_crossing(a, l, m, r):
    left_sum = - maxsize
    right_sum = - maxsize
    l_sum = 0
    r_sum = 0

    # left sum
    for i in range(m, l-1, -1):
        l_sum += a[i]
        if l_sum > left_sum:
            left_sum = l_sum
    # right sum
    for i in range(m+1, r+1):
        r_sum += a[i]
        if r_sum > right_sum:
            right_sum = r_sum

    return left_sum + right_sum

arrayA = [1, -4, 3, 5, 7, -9, -7, 7, 7, -15, 2, 4, 3]
print("max sum of sub array is equal to", max_sub_arr(arrayA, 0, len(arrayA)-1))
