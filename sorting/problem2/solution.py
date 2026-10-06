n = int(input())
dates = []
for i in range(n):
    d , m , y = map(int,input().split())
    dates.append((d,m,y))
for i in range(n):
    min_idx = i
    for j in range(i+1,n):
        date_j = (dates[j][2],dates[j][1],dates[j][0])
        date_min = (dates[min_idx][2],dates[min_idx][1],dates[min_idx][0])
        if date_j > date_min:
            min_idx = j
    dates[i] , dates[min_idx] = dates[min_idx] , dates[i]
for d , m , y in dates[len(dates)::-1]:
    print(d , m , y)