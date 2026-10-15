MAX_CUSTOMERS = 5
customerIDs = [0] * MAX_CUSTOMERS
front = -1
rear = -1

def initializeQueue():
    global front, rear
    front = -1
    rear = -1

def isFull():
    return front == (rear + 1)%MAX_CUSTOMERS

def isEmpty():
    return front == -1

def addCustomer(customerID):
    global front , rear
    if isFull():
        return 0 
    if isEmpty():
        front = rear = 0
        
    else:
        rear = (rear + 1)%MAX_CUSTOMERS
    customerIDs[rear] = customerID
    return True
    
def processCustomer():
    global front , rear
    if isEmpty():
        return False , 0
    popped = customerIDs[front]
    if front == rear:
        front = rear = -1
    else:
        front = (front + 1)%MAX_CUSTOMERS
    return popped , True
        
def displayQueue():
    global front , rear
    if isEmpty():
        print("Checkout queue is empty.")
        return False
    else:
        i = front
        print("Customers waiting in the checkout queue:" ,end =" ")
        while i != rear:
            print(customerIDs[i] , end= " ")
            i = (i+1)%MAX_CUSTOMERS
        print(customerIDs[rear])

def main():
    initializeQueue()
    while True:
        try:
            option = int(input())
        except:
            break

        if option == 1:
            try:
                customerID = int(input())
                if addCustomer(customerID) == 0:
                    print("Checkout queue is full.")
                else:
                    print(f"Customer ID {customerID} joined the checkout queue.")
            except:
                break
        elif option == 2:
            customerID, success = processCustomer()
            if success == 0:
                print("Checkout queue is empty.")
            else:
                print(f"Processed Customer ID: {customerID}")
        elif option == 3:
            displayQueue()
        elif option == 4:
            print("Exiting Program")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
