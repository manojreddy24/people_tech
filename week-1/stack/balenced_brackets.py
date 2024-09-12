def isBalenced(s):
    stack=[]
    for i in s:
        if i in ['{','[','(']:
            stack.append(i)
        else:
            if not stack:
                return False
            if i=='}' and  stack.pop()!='{':
                return False

            elif i==']' and stack.pop()!='[':
               return False
            elif i==')' and stack.pop()!='(':
                return False

    return len(stack)==0





print(isBalenced("{[()]}")) # True
print(isBalenced("{[(])}")) # False
print(isBalenced("{{[[(())]]}}")) # True
