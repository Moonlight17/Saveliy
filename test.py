import sys
reload(sys)
sys.setdefaultencoding('utf-8')


print('Hello, World')
def Test(a):
    print(a)

def STRING123(word):
    print(type(word))
    if (type(word) == 'str'):
        print('str')
    elif (type(word) == 'int'):
        print('int') 
    print('test')
    for i in range(word):
        print (i)
print('first function')
Test(13)
STRING123(10000000)