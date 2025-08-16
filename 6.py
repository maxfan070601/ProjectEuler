def sum_squared_diff(num):
    squares_sum = 0
    sum_squared = 0
    for i in range(1, num+1):
        squares_sum += i*i
    for i in range(1, num+1):
        sum_squared += i
    return abs(sum_squared*sum_squared - squares_sum)


print(sum_squared_diff(100))