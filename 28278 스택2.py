import sys
input = sys.stdin.readline

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.is_empty():
            return -1
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0

    def top(self):
        if self.is_empty():
            return -1
        return self.stack[-1]


stack = Stack()

N = int(input().rstrip())

for _ in range(N):
    command = input().rstrip().split()

    if command[0] == '1':
        stack.push(int(command[1]))
    elif command[0] == '2':
        print(stack.pop())
    elif command[0] == '3':
        print(stack.size())
    elif command[0] == '4':
        print(int(stack.is_empty()))
    elif command[0] == '5':
        print(stack.top())
