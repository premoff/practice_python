#bankdb.py

import mysql.connector

# Connecting from the server
conn = mysql.connector.connect(host="host-name",
                              user="username",password="password",
                              database = "database-name")
print('connection succeed')


# insert data into database
def insertinto(acc_no,name,balance):
  cur = conn.cursor()
  sql = "INSERT INTO testdb.bank values (%s,%s,%s);"
  val =  (acc_no,name,balance) 
  
  cur.execute(sql,val)
  conn.commit()

#select query
def select(acc_no):
  cur = conn.cursor()
  sql = 'SELECT * FROM testdb.bank where acc_no=%s;'%acc_no
  cur.execute(sql)
  user_balance = cur.fetchone()   
  return user_balance
  # for x in myresult:
  #   print(x)
  #   cur.close()

#update
def update(acc_no,amount):
  cur = conn.cursor()
  sql = 'UPDATE bank SET balance=%s where acc_no=%s;'
  val = (amount,acc_no)
  cur.execute(sql,val)
  conn.commit() 
  return(select(acc_no))
  
def deluser(acc_no):
  cur = conn.cursor()
  sql = "DELETE FROM bank WHERE acc_no=%s;"
  val = (acc_no,)
  cur.execute(sql,val)
  conn.commit()

# Disconnecting from the server
def quit():
  conn.close()
  print('server disconnected')

