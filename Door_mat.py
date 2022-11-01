#Design a door mat
'''
Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
'''
#for better result  column input shoud be  c = 3 x row

row,column = map(int,input('enter size of mat with space').split())
for i in range(1,row,2):
    print(('.|.'*i).center(column,'-'))

print('WELCOME'.center(column,'-'))

for i in range(row-2,0,-2):
  print(('.|.'*i).center(column,'-'))
