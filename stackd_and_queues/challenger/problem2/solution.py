import sys
MAX_SIZE = 20
stack = []
top = -1
def is_full():
    global top
    return top == MAX_SIZE -1

def is_empty():
    global top
    return top == -1

def push(data):
    global top
    if not is_full():
        stack.append(data)
        top += 1

def pop():
    global top
    if is_empty():
        return False
    else:
        popped = stack.pop()
        top -= 1
        return popped

def peek():
    global top
    return stack[top]

def find_minimum():
    return  min(stack)

def main():
    n = int(sys.stdin.readline().strip())
    values = list(map(int, sys.stdin.readline().strip().split()))
    for value in values:
        push(value)
    print("Minimum element in the stack:", find_minimum())
    popped = pop()
    if popped != float('-inf'):
        print("Popped element:", popped)
    print("Minimum element in the stack after popping:", find_minimum())

if __name__ == "__main__":
    main()