import random
import string
a = 15
result = ''
length = ''

while len(result)<18:

    d = string.digits + string.ascii_uppercase
    b = random.choices(d)
    result += (''.join(b))
    length += (''.join(b))    
    if len(length) == 5:
        result += '-'
        length = ''
    
print(result[0:-1])
