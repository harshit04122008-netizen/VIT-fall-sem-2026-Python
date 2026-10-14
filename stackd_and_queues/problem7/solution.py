SIZE = 5
queue = [''] * SIZE
front = -1
rear = -1
def isfull():
    global front , rear
    return front == (rear+1)%SIZE
    
def isempty():
    return front == -1
    
    
def enqueue(reg):
    global front , rear
    if isfull():
        print("Exit queue is full.")
        return False
    if isempty():
        front = rear = 0
    else:
        rear = (rear+1)%SIZE
    queue[rear] = reg
    print(f"Car {reg} joined the exit queue.")

def dequeue():
    global front , rear
    if isempty():
        print("Exit queue is empty.")
        return False , 0
    reg = queue[front]
    if front == rear:
        front = rear = -1
    else:
        front = (front +1)%SIZE
    print(f"Car {reg} has exited the parking lot.")
        

def display():
    global front , rear
    if isempty():
        print("Exit queue is empty.")
    else:
        print("Cars waiting in the exit queue:",end=" ")
        i = front
        while i != rear:
            print(queue[i],end = " ")
            i = (i+1)%SIZE
        print(queue[rear])

while True:
    try:
        choice = int(input())
        if choice == 1:
            reg = input().strip()
            enqueue(reg)
        elif choice == 2:
            dequeue()
        elif choice == 3:
            display()
        elif choice == 4:
            print("Exiting the parking lot system.")
            break
        else:
            print("Invalid menu option.")
    except:
        break