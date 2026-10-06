a , b , c = list(map(float,input().split()))
def find_max(a,b,c):
    L = [a,b,c]
    return max(L)
maximum = find_max(a,b,c)
print(f"{maximum:.2f}", end="")