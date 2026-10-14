
def enqueue(data, queue):
    queue.append(data)
    
def print_averages(size, queue):
    for i in range(size-1):
        print((queue[i]+queue[i+1])/2 , end= " ")
    print()

def print_sum(queue):
    print("Sum of all elements:",sum(queue))

def print_even_odd_count(queue):
    count_even = 0
    count_odd = 0
    for i in queue:
        if i % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    print("Number of even elements:",count_even)
    print("Number of odd elements:",count_odd)

n = int(input())
values = input().split()
if len(values) != n:
    print("Error: Expected", n, "values, but got", len(values))
else:
    queue = []
    for i in range(n):
        enqueue(int(values[i]), queue)

    print("Averages of pairs:")
    print_averages(n, queue)
    print_sum(queue)
    print_even_odd_count(queue)