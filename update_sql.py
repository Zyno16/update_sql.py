import mysql.connector

try:
    conn = mysql.connector.connect(
        user = "userpython",
        host = "localhost",
        passwd = "123456",
        database = "arabicinfo"
        )
    cur = conn.cursor()
    cur.execute("update emp set empname ='zin' where empno =1")
    conn.commit()

except mysql.connector.Error as e:
        print(e)

 
