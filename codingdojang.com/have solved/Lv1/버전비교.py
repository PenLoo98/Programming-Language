# https://codingdojang.com/scode/493

# 버전을 .으로 나눠주고
# 버전의 앞 자리부터 비교를 한다


def VerCompare(a, b):
    c = a.split('.')
    d = b.split(".")
    for i in range(3):
        if int(c[i]) > int(d[i]):
            print("%s > %s" % (a, b))
            break
        elif int(c[i]) < int(d[i]):
            print("%s > %s" % (b, a))
            break
        else:  # c[i] == d[i]
            if i == 2:
                print("%s = %s" % (a, b))
            continue


VerCompare("0.0.2", "0.0.1")
VerCompare("1.0.10", "1.0.3")
VerCompare("1.2.0", "1.1.99")
VerCompare("1.1", "1.0.1")

