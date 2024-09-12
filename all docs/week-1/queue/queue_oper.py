def downToZero(n):
    for i in range(n, -1,):
        if i == 0:
            return n
        if n % i == 0:
            n = n // i
            return downToZero(n)







print(downToZero(3)) # 3
