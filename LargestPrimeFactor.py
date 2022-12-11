#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
import time
start_time = time.time()
def largest_prime_factor(n):
    prime_factors = []
    for i in range(1,n//2+1): #factors
        if n%i==0:
            x = True
            for j in range(2,i//2+1): # check the factor is prime
                if i%j==0:
                    x = False
                    break
                x = True  
            if x:
                prime_factors.append(i)
    return max(prime_factors)




print(f'{largest_prime_factor(11)} is the largest prime factor of the number 600851475143')

end_time = time.time()
print(f'total execution time {end_time-start_time}')

