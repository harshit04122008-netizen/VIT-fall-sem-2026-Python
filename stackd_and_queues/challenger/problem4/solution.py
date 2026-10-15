MAX_SIZE = 5
pages = [0] * MAX_SIZE
front = -1
rear = -1
def initializeQueue():
    global front , rear
    front = -1
    rear = -1

def isEmpty():
    return front == -1

def isFull():
    return front == (rear+1)%MAX_SIZE
    
def enqueue(p):
    global front , rear
    if isFull():
        print("Queue is full. Cannot enqueue.")
        return False
    
    if isEmpty():
        front = rear = 0
        
    else:
        rear = (rear+1)%MAX_SIZE
    pages[rear] = p
    print(f"Print job with {p} pages is enqueued.")
    return True
def dequeue():
    global front , rear
    if isEmpty():
        print("Queue is empty.")
        return False , 0
    p = pages[front]
    if front == rear:
        front = rear = -1
    else:
        front = (front+1)%MAX_SIZE
    return True , p

def display():
    global front , rear
    if isEmpty():
        return False
    else:
        i = front 
        print("Print jobs in the queue:" , end =" ")
        while i != rear:
            print(pages[i], end =" ")
            i = (i+1)%MAX_SIZE
        print(pages[rear])
def main():
    initializeQueue()
    while True:
        try:
            inputs = input().strip().split()
            if not inputs:
                continue
            option = int(inputs[0])

            if option == 1:
                if len(inputs) < 2:
                    continue
                p = int(inputs[1])
                enqueue(p)

            elif option == 2:
                success, p = dequeue()
                if success:
                    print(f"Processing print job: {p} pages")
                else:
                    print("Queue is empty.")

            elif option == 3:
                display()

            elif option == 4:
                print("Exiting program")
                return

            else:
                print("Invalid option.")
        except:
            break

if __name__ == "__main__":
    main()
