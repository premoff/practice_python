# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

x = False
for i in range(999,99,-1):  # iterate from high to low 
    if x==True:
        break               # terminate for loop
    for j in range(999,99,-1):   
        product = i * j
        temp = product
        reverse = 0
        while product>0:
            remainder = product%10
            reverse = (reverse * 10) + remainder
            product //= 10
        if reverse==temp:
            print(f'the largest palindrom made from the product of two 3-digit number is {i*j} = {i} x {j}')
            x = True
            break       # terminate for loop 
