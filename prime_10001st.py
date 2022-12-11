# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10001st prime number?

def isprime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
        
    return True

nth_prime=int(input('enter a number: '))
num = 1
count = 0

while count<nth_prime:
    num += 1
    if isprime(num):
        count += 1

print(f'{nth_prime}th/st prime is {num}')
    
        

 
