#  Q18
import re

#  Only ended ".com" or ".net"


#  a = re.compile('.*[@].*[.]com |.*[@].*[.]net')
a = re.compile(".*[@].*[.](?=com$|net$).*$")
print(a.match("pahkey@gmail.com"))
print(a.match("kim@daum.net"))
print(a.match("lee@myhome.co.kr"))




# b = 'park@naver.com, kim@daum.net, lee@myhome.co.kr'
# c = a.findall(b)
# print(c)
#  .com이나 .net로만 끝나야 한다 =
#   .*[@].*[.]([^c]..|.[^o].|..[^m])$


