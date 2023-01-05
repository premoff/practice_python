# count the vowels for given string
vowels = 'aeiouAEIOU'
s = input('enter a string : ')

count = 0
for i in range(len(s)):
    if s[i] in vowels:
        count += 1

print(count)
