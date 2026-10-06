def subset_sum_recursive(nums, S):
    subsets = [[]]
    for r in nums:
        subsets += [current_sub + [r] for current_sub in subsets]
    subsets.sort()
    for i in subsets:
        if len(i) == 3:
            if sum(i) == S:
                print(i)
                return True
                break

nums = list(map(int, input().split()))
S = int(input())

if not subset_sum_recursive(nums, S):
    print(sorted(nums, reverse=True))
    print("false")