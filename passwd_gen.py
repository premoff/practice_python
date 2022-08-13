
import random
import string


def password(passwd_length):
    passwd = ''
    while len(passwd)<=passwd_length:
        characters = ''.join(random.choices(string.digits)) + ''.join(random.choices(string.ascii_uppercase)) + ''.join(random.choices(string.ascii_lowercase)) + ''.join(random.choices(string.punctuation))
        passwd += characters
    return(passwd)

while True:
    passwd_length = int(input('length of the password: '))
    if passwd_length<8:
        print('enter passwd length minimum 8 character')
        continue
    else:
        print(password(passwd_length))
        break
