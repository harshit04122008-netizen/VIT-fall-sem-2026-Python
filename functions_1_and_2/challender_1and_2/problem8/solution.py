from math import prod as prod
n = int(input())
L = list(map(int,input().split()))
sub_list =[]
for i in range(n):
    for j in range(i+1,n+1):
        sub = L[i:j]
        sub_list.append(sub)
largest_list = max(sub_list , key =lambda x: sum(x))
max_product = max(sub_list ,key = lambda x: prod(x))
print("PMax:",prod(max_product))
print("SMax:",sum(largest_list))