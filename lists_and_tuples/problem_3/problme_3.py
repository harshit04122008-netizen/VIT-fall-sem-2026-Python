L = input().split()
i = 0
L_2 =  []
while i<(len(L)-1):
    if i<(len(L)-2):
        a = int(L[i])
        b = int(L[i+1])
        c = int(L[i+2])
        if b>a and b>c:
            L_2.append(b)
    elif i<len(L):
        a = int(L[i])
        b = int(L[i+1])
        if b>a:
            L_2.append(b)
    i = i + 1
print("Peaks:",L_2)