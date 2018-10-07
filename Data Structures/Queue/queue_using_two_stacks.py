old_stack, new_stack = [], []

for _ in range(int(input())):
    value = list(map(int, input().split()))
    if value[0] == 1:
        if not new_stack:
            head = value[1]
        new_stack.append(value[1])
    elif value[0] == 2:
        if not old_stack:
            while new_stack: old_stack.append(new_stack.pop())
        old_stack.pop()
    else:
        print(old_stack[-1] if old_stack else head)