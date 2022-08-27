

import mysql.connector
myconn=mysql.connector.connect(host="localhost",user="root",passwd="admin")
cur=myconn.cursor()
try:
    dbs=cur.execute("show databases")
except:
    myconn.rollback()
for i in cur:
    print(i)
myconn.close()


# In[ ]:





# In[ ]:




