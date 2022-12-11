
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? Ans = 232792560

small_positive = 20

while small_positive>0:
    factors = []
    for i in range(1,21):
        if small_positive%i==0:
            factors.append(i)
        else:
            break        
    
    if factors == [i for i in range(1,21)]:
        print(f'{small_positive} - {factors}')
        
        break
    else:
        small_positive += 1

