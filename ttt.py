import mysql.connector
import re
mydb = mysql.connector.connect(host="localhost", user="root",password="", database="chatbot")
mycursor = mydb.cursor()

mycursor.execute("SELECT happy FROM newplaylist")
myresult = mycursor.fetchall()

for x in myresult:
    y=str(x)
    y = str(y).replace('(','').replace(')','').replace(',','').replace("'", "")
##    y=re.sub("(',')", "", y)
##    y=re.sub("(,)", "", y)
##    y=re.sub("('')", "", y)
##    y=re.sub("( )", "", y)
    print(y)
       

