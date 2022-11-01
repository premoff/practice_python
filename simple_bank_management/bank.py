#bank.py

import bankdb as db

class Bank:
    '''Bank class'''
    def __init__(self):
        self.acc_no = 12340
        self.name = 'xyz'
        self.balance = 100
    #add new user to the bank
    def newuser(self):
        self.acc_no = int(input('create acc no :'))
        self.name = input('enter user name :')
        self.balance = int(input('enter initial deposit :'))
        db.insertinto(self.acc_no,self.name,self.balance)
        print("new user added")
    # delete user detailes from database
    def remove_user(self):
        self.acc_no = int(input('Enter acc_no :'))
        db.deluser(self.acc_no) 
    # get user balance from the database
    def getbalance(self):
        self.acc_no = int(input('enter acc no :'))
        self.balance = db.select(self.acc_no)
        return (self.balance[1],self.balance[2])
    # add amount to the user and update the database
    def deposit(self):
        self.acc_no = int(input('Enter acc_no :'))
        self.deposit =  int(input('enter amount :'))
        current_balance = (db.select(self.acc_no)[2])+self.deposit
        self.balance = db.update(self.acc_no,current_balance)
        print(self.balance)
        return self.balance
    # less the account balance by withdraw amount and update the database
    def withdraw(self):
        self.acc_no = 12346 #int(input('enter acc no :'))
        withdraw_amount = 100 #int(input('how much want :'))
        current_balance = db.select(self.acc_no)[2]
        self.balance = current_balance - withdraw_amount
        self.balance = db.update(self.acc_no,self.balance)
        return self.balance

