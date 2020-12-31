import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace('\t', " "*4)

f2 = open(dst, 'w')
f2.write(space_content)
f2.close()

print(space_content)