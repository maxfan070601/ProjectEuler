from scipy.stats import false_discovery_control


def palindrome_brute_force():
    max = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            if is_palindrome(list(str(i * j))) and i * j > max:
                max = i * j
                break
    return max


def is_palindrome(nums: list) -> bool  :
    reversed_nums = []
    for i in range(len(nums)-1, -1, -1):
        reversed_nums.append(nums[i])
    for i in range(len(nums)):
        if nums[i] != reversed_nums[i]:
            return False
    return True

print(palindrome_brute_force())