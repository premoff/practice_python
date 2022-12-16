# The sum of the squares of the first ten natural numbers is,1^2 + 2^2+..+10^2 =385
# The square of the sum of the first ten natural numbers is, (1+2+...+10)^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is. 3025-385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum. 

n = int(input('enter a number: '))
#sum of the suares 1 to n natural numbers
sum_of_squares = 0
for i in range(1,n+1):
    sum_of_squares += i**2

#sum of the squares of 1 to n natural numbers
square_of_sum = 0
for j in range(1,n+1):
    square_of_sum += j

difference = square_of_sum**2 - sum_of_squares
print(f'square of sum = {square_of_sum**2} \nsum of square = {sum_of_squares}')
print(f' {square_of_sum**2} - {sum_of_squares} = {difference}')
