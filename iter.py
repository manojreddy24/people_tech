def andXorOr(a):
    m = 0
    s = []
    for i in a:
        while s and s[-1] >= i:
            m = max(m, i^s.pop())
        if s:
            m = max(m, i^s[-1])
        s.append(i)
    return m


print(andXorOr([9,6,3,5,2])) # 15