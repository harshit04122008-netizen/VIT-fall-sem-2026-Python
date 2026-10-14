max_ = 5
ticket_id = [0]*max_
front = -1
rear = -1

def initial():
    global front , rear
    front = -1
    rear = -1

def isempty():
    return front == -1
    
def isfull():
    return (rear+1)%max_ == front

def enqueue(ticket_Id):
    global front , rear
    if isfull():
        print("Queue is full. Cannot enqueue.")
        return False
    
    if isempty():
        front = rear = 0
        
    else:
        rear = (rear+1)%max_
    
    ticket_id[rear] = ticket_Id
    print(f"Helpdesk Ticket ID {ticket_Id} is enqueued.")
    return True
    
def dequeue():
    global front , rear
    if isempty():
        return False,0
    ticket_ID = ticket_id[front]
    
    if front == rear:
        front = rear - 1
        
    else:
        front = (front+1)%max_
        
    return True , ticket_ID
    
def display():
    if isempty():
        print("Queue is empty.")
    else:
        print("Helpdesk Ticket IDs in the queue are:",end=" ")
        i = front
        while i != rear:
            print(ticket_id[i],end=" ")
            i = (i+1)%max_
        print(ticket_id[rear])

initial()

while True:
    option = list(map(int,input().split())) 
    if option[0] == 1:
        enqueue(option[1])
        
    elif option[0] == 2:
        success , ticket_ID = dequeue()
        if success:
            print("Dequeued Helpdesk Ticket ID:",ticket_ID)
            
        else:
            print("Queue is empty.")
    elif option[0] == 3:
        display()
    elif option[0] == 4:
        print("Exiting the program")
        break
    else:
        print("Invalid option.")