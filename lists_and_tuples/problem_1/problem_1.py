n = int(input())
#input for the numbers of workers 

L = input().split(" ")
#input for the list of workers

for i in range(n):
    print((L[i-2]),end=" ") #to make the last two workers move to the front of the list, we use i-2 as the index to print the workers in a circular manner
    