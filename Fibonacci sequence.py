def P(n):
    Pibo = []
    Pibo += 0, 1
    index_before_value = 0
    index_after_value = 1
    while len(Pibo) <50:
        index_value = index_before_value + index_after_value
        Pibo.append(index_value)
        index_before_value = index_after_value
        index_after_value = index_value
    if (n in Pibo) and (n == 0):
        Pibo = [0]
    elif (n in Pibo) and (n == 1):
        Pibo = [0, 1, 1]
    elif n in Pibo:
        # Pibo.index(n) 인덱스 번호
        del Pibo[(Pibo.index(n)+1):]
    elif n not in Pibo:
        while n not in Pibo:
            n -= 1
        del Pibo[(Pibo.index(n) + 1):]
    else:
        Pibo = ["잘못된 입력입니다"]
    return Pibo
print(P(34))









