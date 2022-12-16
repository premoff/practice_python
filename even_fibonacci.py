

#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms 
#will be:       1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


def fibonacci(n):
    
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

#fib = []
total = 0
limit = int(input('enter a range :')
for i in range(1,limit):
    a = fibonacci(i)
    #print(a)
    if a%2==0:
        #fib.append(a)
        total += a
#print(f'sum of even fibonacci {sum(fib)}')
print(f'sum of even-valued terms {total}')
