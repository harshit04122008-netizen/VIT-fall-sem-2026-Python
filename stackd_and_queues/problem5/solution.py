MAX_SIZE = 5

characters = [''] * MAX_SIZE
front = -1
rear = -1

def initializeQueue():
    global front, rear
    front = -1
    rear = -1
def isEmpty():
    return front == -1

def isFull():
    return (rear + 1) % MAX_SIZE == front

def enqueue(character):
    global front , rear
    if isFull():
        print("Queue is full. Cannot enqueue.")
        return False
    if isEmpty():
        front =  rear = 0
    else:
        rear = (rear+1) %  MAX_SIZE
    characters[rear] = character
    print(f"Character {character} is enqueued.")
        

def dequeue():
    global front , rear
    if isEmpty():
        return False , 0
    character = characters[front]
    if front == rear:
        front =  rear = -1
    else:
        front = (front+1) %  MAX_SIZE
    return True , character
    

def display():
    if isEmpty():
        print("Queue is empty.")
    else:
        print("Characters in the queue are:",end =" ")
        i = front
        while i != rear:
            print(characters[i],end=" ")
            i = (i+1)%MAX_SIZE
        print(characters[rear])

def main():
    initializeQueue()
    while True:
        try:
            line = input()
            if not line:
                continue
            parts = line.strip().split()
            if not parts:
                continue
            option = int(parts[0])
            if option == 1:
                if len(parts) == 2:
                    character = parts[1]
                else:
                    character = input().strip()
                enqueue(character)
            elif option == 2:
                status, character = dequeue()
                if status:
                    print(f"Dequeued Character: {character}")
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