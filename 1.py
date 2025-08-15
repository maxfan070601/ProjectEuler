def compute_multiples():
    sum = 0
    for i in range(0, 1000, 3):
        sum += i
    for i in range(0, 1000, 5):
        sum += i
    for i in range(0, 1000, 15):
        sum -= i
    return sum

def compute_multiples_advanced():
    return (3 + 999) / 2 * 333 + (5 + 995) / 2 * 199 - (15 + 990) / 2 * 66

print(compute_multiples())
print(compute_multiples_advanced())