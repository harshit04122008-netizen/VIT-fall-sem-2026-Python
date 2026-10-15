max_size = 100
stack = []
top = -1
def init():
    global top
    top = -1

def isfull():
    return top == max_size -1

def isempty():
    return top == -1

def push(val):
    global top
    if not isfull():
        top += 1
        print(f"Item {val} is pushed onto the shelf")
        stack.append(val)

def pop():
    global top
    if isempty():
        print("No items in the shelf")
        return False
    else:
        popped = stack.pop()
        top -= 1
        print(f"Item {popped} is popped from the shelf")

def disp():
    global top
    if isempty():
        print("Shelf is empty")
    else:
        print("Items in the shelf:",end=" ")
        for i in stack[::-1]:
            print(i , end=" ")
        print()

init()

while True:
    option = list(map(int,input().split()))
    if option[0] == 1:
        push(option[1])
    elif option[0] == 2:
        pop()
    elif option[0] == 3:
        disp()
    elif option[0] == 4:
        print("Exiting the warehouse")
        break
    else:
        print("Invalid choice")
        