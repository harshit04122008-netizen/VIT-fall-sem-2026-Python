MAX_SIZE = 5
orders = [''] * MAX_SIZE
front = -1
rear = -1
# You are using Python
def initializeQueue():
    global front , rear
    front = -1
    rear = -1
    
def isEmpty():
    return front == -1

def isFull():
    return front == (rear+1)%MAX_SIZE

def enqueue(order):
    global front ,  rear
    if isFull():
        print("Queue is full. Cannot enqueue more orders.")
    if order not in orders:
        if isEmpty():
            front = rear =0
        else:
            rear = (rear +1)% MAX_SIZE
        orders[rear] = order
        print(f"Order for {order} is enqueued.")
        return True

def dequeue():
    global front ,  rear
    if isEmpty():
        return False , 0
    order = orders[front]
    if front == rear:
        front = rear = -1
    else:
        front = (front +1)% MAX_SIZE
    return order , True

def display():
    global front , rear
    if isEmpty():
        print("Queue is empty. No orders available.")
    else:
        print("Orders in the queue are:",end=" ")
        i = front
        while i != rear:
            print(orders[i],end =" ")
            i = (i+1)%MAX_SIZE
        print(orders[rear])

def main():
    order = ''
    option = 0

    initializeQueue()

    while True:
        try:
            option = int(input())
        except ValueError:
            break

        if option == 1:
            try:
                order = input()
                if enqueue(order):
                    pass  # Order enqueued successfully
            except ValueError:
                pass
        elif option == 2:
            order, success = dequeue()
            if success:
                print(f"Dequeued Order: {order}")
            else:
                print("No orders in the queue.")
        elif option == 3:
            display()
        elif option == 4:
            print("Exiting program", end="")
            return
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()