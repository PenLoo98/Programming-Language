import sys

opt = sys.argv[1]

if opt == '-a':
    memo = sys.argv[2]
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write("\n")
    f.close()

elif opt == '-v':
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo)