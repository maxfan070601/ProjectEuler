def compute_multiples():
    s = 0
    for i in range(0, 1000, 3):
        s += i
    for i in range(0, 1000, 5):
        s += i
    for i in range(0, 1000, 15):
        s -= i
    return s

def compute_multiples_advanced():
    return (3 + 999) / 2 * 333 + (5 + 995) / 2 * 199 - (15 + 990) / 2 * 66

print(compute_multiples())
print(compute_multiples_advanced())