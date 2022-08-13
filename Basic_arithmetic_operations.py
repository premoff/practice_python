
def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)

a = int(input('enter first no :'))
b = int(input('enter second no :'))
c = input('enter arithmatic operator: ')

if c=='/':
    print(div(a,b))
elif c=='*':
    print(mul(a,b))
elif c=='+':
    print(add(a,b))
elif c=='-':
    print(sub(a,b))
else:
    print('enter valid operator')

    
