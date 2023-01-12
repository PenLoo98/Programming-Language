# https://codingdojang.com/scode/492

n = int(input("숫자 n을 입력하시오\n:"))

for i in range(n):
    print((n-i-1)*"O", end="")
    print((i+1) * "X", end="")
    print()