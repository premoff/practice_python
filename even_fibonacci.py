def fibonacci(n):
    
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

#fib = []
total = 0
for i in range(1,5):
    a = fibonacci(i)
    #print(a)
    if a%2==0:
        #fib.append(a)
        total += a
#print(f'sum of even fibonacci {sum(fib)}')
print(f'sum of even-valued terms {total}')
