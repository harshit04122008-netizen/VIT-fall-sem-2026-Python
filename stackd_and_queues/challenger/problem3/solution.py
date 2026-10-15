MAX_SIZE = 100
stack = [0] * 100
top = -1

def printf(format_str, *args):
    print(format_str % args, end='')

def isfull():
    global top
    return top == MAX_SIZE - 1

def isempty():
    global top
    return top == -1
    
def push(value):
    global top
    if not isfull():
        stack.append(value)
        top += 1
        print(f"Book {value} is added to the shelf")
        
def pop():
    global top
    if isempty():
        print("No books on the shelf")
        return False
    else:
        popped = stack.pop()
        top -= 1
        print(f"Book {popped} is removed from the shelf")

def displayStack():
    global top
    if isempty():
        print("shelf is empty")
        return False
    else:
        print("Books on the shelf:" , end =" ")
        for i in stack[::-1]:
            if i != 0:
                print(i , end =" ")
        print()

def peek():
    global top
    if isempty():
        print("Shelf is empty")
    else:
        print(f"Top book on the shelf:{stack[::-1][0]}")

def main():
    import sys
    input_data = []
    
    # Read all input at once
    for line in sys.stdin:
        input_data.extend(line.strip().split())
    
    i = 0
    while i < len(input_data):
        try:
            choice = int(input_data[i])
            i += 1
            
            if choice == 1:
                if i < len(input_data):
                    value = int(input_data[i])
                    i += 1
                    push(value)
            elif choice == 2:
                pop()
            elif choice == 3:
                displayStack()
            elif choice == 4:
                peek()
            elif choice == 5:
                printf("Exiting the shelf management system\n")
                break
            else:
                printf("Invalid choice\n")
        except (ValueError, IndexError):
            break

if __name__ == "__main__":
    main()
