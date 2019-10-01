def sub_arr_max_sum(arr):
    max = arr[0]
    for i in range(0,len(arr)):
        for j in range(i, len(arr)):
            sum = 0
            for k in range(i, j):
                sum += arr[k]
                if sum > max:
                    max = sum
    return max

a = [1, -4 , 3, 5, 7, -9, -7, 7, 7, -15, 2, 4, 3]
print("max sum of sub array is equal to ", sub_arr_max_sum(a))
