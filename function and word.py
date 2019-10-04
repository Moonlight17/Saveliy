import sys
reload(sys)
sys.setdefaultencoding('utf-8')



zabc = 30
two = 50
tree = 120


def Sum(a, b, c):
    sum = a + b + c
    return sum

out = Sum(abc, two, tree)
print(out)