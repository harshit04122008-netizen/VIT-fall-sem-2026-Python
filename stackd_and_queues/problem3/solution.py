MAX_SIZE = 100
stack = [0] * MAX_SIZE
top = -1
def isfull():
    return top == MAX_SIZE - 1

def isempty():
    return top == -1

def push(value):
    global top
    if not isfull():
        top += 1
        stack.append(value)
        print(f"Book ID {value} is pushed onto the stack")
    else:
        print("stack overflow")

def pop():
    global top
    if isempty():
        print("Stack Underflow")
    else:
        popped = stack.pop()
        top -= 1
        print(f"Book ID {popped} is popped from the stack")

def displayStack():
    global top
    if isempty():
        print("Stack is empty")
    else:
        print("Book ID in the stack:",end=" ")
        for i in stack[::-1]:
            if i != 0:
                print(i,end=" ")
        print()

def main():
    while True:
        try:
            inputs = input().strip().split()
            if not inputs:
                continue
            choice = int(inputs[0])
            if choice == 1:
                value = int(inputs[1])
                push(value)
            elif choice == 2:
                pop()
            elif choice == 3:
                displayStack()
            elif choice == 4:
                print("Exiting the program")
                break
            else:
                print("Invalid choice")
        except:
            continue

if __name__ == "__main__":
    main()