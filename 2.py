def fibonacci():
    even_sum = 0
    prev1 = 1
    prev2 = 1
    while prev1 + prev2 <= 4000000:
        sum = prev1 + prev2
        if sum % 2 == 0:
            even_sum += sum
        prev2 = prev1
        prev1 = sum
    return even_sum

print(fibonacci())