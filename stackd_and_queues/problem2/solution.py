MAX_TEXT_LENGTH = 100

textStack = [''] * MAX_TEXT_LENGTH
stackTop = -1

def initialize():
    global stackTop
    stackTop = -1

# You are using Python
def isFull():
    return stackTop == MAX_TEXT_LENGTH - 1

def isEmpty():
    return stackTop == -1
    
def pushCharacter(value):
    global stackTop
    if not isFull():
        stackTop += 1
        textStack.append(value)
        print("Typed character:",value)
    else:
        print("Stack is full")

def popCharacter():
    global stackTop
    if isEmpty():
        print("Text editor buffer is empty. Nothing to undo.")
    else:
        popped = textStack.pop()
        stackTop -= 1
        print("Undo: Removed character",popped)

def view():
    global stackTop
    if isEmpty():
        print("Text editor buffer is empty.")
    else:
        print("Current text:",end=" ")
        for i in textStack[::-1]:
            print(i,end=" ")
        print()

def main():
    global stackTop
    choice = 0
    input_char = ''
    initialize()
    while True:
        choice = int(input())
        if choice == 1:
            input_char = input()
            pushCharacter(input_char)
        elif choice == 2:
            popCharacter()
        elif choice == 3:
            view()
        elif choice == 4:
            return
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()