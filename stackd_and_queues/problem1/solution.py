MAX_SIZE = 100
items = []
top = -1
def initialize():
    global top
    top = -1

def isFull():
    return top == MAX_SIZE - 1

def isEmpty():
    return top == -1
def push(value):
    global top
    if not isFull():
        top += 1
        items.append(value)
        print("Pushed:",value)

def pop():
    global top
    if isEmpty():
        print("Stack is empty. Nothing to pop.")
    else:
        global top
        popped = items.pop(top)
        top -= 1
        print("Popped:",popped)

def display():
    global top
    if isEmpty():
        print("Stack is empty.")
    else:
        print("Stack Elements:",end=" ")
        for i in items[::-1]:
            print(i, end=" ")
    print()

def main():
    initialize()
    while True:
        try:
            inputs = input().strip().split()
            if not inputs:
                continue
            choice = int(inputs[0])
            if choice == 1:
                if len(inputs) < 2:
                    value = input().strip()
                else:
                    value = inputs[1]
                push(value[0])
            elif choice == 2:
                pop()
            elif choice == 3:
                display()
            elif choice == 4:
                return
            else:
                print("Invalid choice")
        except EOFError:
            break

if __name__ == "__main__":
    main()