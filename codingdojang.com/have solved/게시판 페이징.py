# https://codingdojang.com/scode/406

m = int(input("총 건수를 입력하시오(m)\n:"))
n = int(input("한 페이지에 보여줄 게시물 수를 입력하시오(n)\n:"))
if m == 0:
    print("총페이지 수는 0개입니다")
elif m % n == 0:
    print("총페이지 수는 %d개입니다" % (m/n))
elif m % n != 0:
    print("총페이지 수는 %d개입니다" % (m//n+1))



