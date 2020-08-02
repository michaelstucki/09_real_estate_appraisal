def find_sig_nums(nums, predicate):
    for n in nums:
        if predicate(n):
            yield n


numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34]
sig = find_sig_nums(numbers, lambda x: x % 2 == 1)

for s in sig:
    print(s, end=', ')

print()
