def fibonacci():
    even_sum = 0
    prev1 = 1
    prev2 = 1
    while prev1 + prev2 <= 4000000:
        s = prev1 + prev2
        if s % 2 == 0:
            even_sum += s
        prev2 = prev1
        prev1 = s
    return even_sum

print(fibonacci())