#main.py

import bank
import bankdb
new = bank.Bank()
while True:
    print('1.newuser \n2.my balance \n3.deposit \n4.withdraw money \n5.revome user \n6.quit ')
    choice = int(input('what you want :'))
    if choice==1:
        new.newuser()
    elif choice==2:
        a = new.getbalance()
        print(f"Hi! {a[0]} your current balance is {a[1]}")
        bankdb.quit()
    elif choice==3:
        b = new.deposit()
        print(f"Hi! {b[1]} your current balance is {b[2]}")
        bankdb.quit()
    elif choice==4:
        c = new.withdraw()
        print(f"Hi! {c[1]} your current balance is {c[2]}")
        bankdb.quit()
    elif choice==5:
        new.remove_user()
        print('user was removed from the database')
    elif choice==6:
        bankdb.quit()
        break
    

