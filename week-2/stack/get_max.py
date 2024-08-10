def getmax(ops):
    stack = []
    results = []

    for operation in ops:
        op = list(map(int, operation.split()))
        print(op)

        if op[0] == 1:
            stack.append(op[1])
        elif op[0] == 2:
            if stack:
                stack.pop()
        elif op[0] == 3:
            if stack:
                results.append(max(stack))

    return results

#time complexity is O(n) where n is the number of operations








#You have an empty sequence, and you will be given  queries. Each query is one of these three types:
#
# 1 x  -Push the element x into the stack.
# 2    -Delete the element present at the top of the stack.
# 3    -Print the maximum element in the stack.


ops = ["1 97", "2", "1 20", "2", "1 26", "1 20", "3", "1 91", "3"]
print(getmax(ops))