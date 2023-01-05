#Find the Index of the First Occurrence in a String

def strStr(s, sub_str):
      
  for i in range(len(s)):
    print(s[i:i+len(sub_str)])
    if sub_str==s[i:i+len(sub_str)]:
      return i
    else:
      continue
  return -1

a = 'mississippi'
sub_str = 'issip'
print(strStr(a,sub_str))
