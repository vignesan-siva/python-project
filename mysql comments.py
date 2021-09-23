#update comment
"""import pymysql
db=pymysql.connect(host='localhost',user='root',password='vignesan',db='math')
cursor=db.cursor()
sql="UPDATE student SET name='siv' WHERE password='123'"
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback
    
db.close()"""
#insert comment

"""import pymysql
db=pymysql.connect(host='localhost',user='root',password='vignesan',db='math')
cursor=db.cursor()
a='siva'
b=766
c='tamilnadu'
d='sss'
sql="INSERT INTO demo (name,number,email,state)VALUES('{}','{}','{}','{}')".format(a,b,c,d)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()"""
#delete comment
"""import pymysql
db=pymysql.connect(host='localhost',user='root',password='vignesan',db='math')
cursor=db.cursor()
sql="delete From student WHERE name='vignesh'"
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()"""
#select comment
"""import pymysql
db=pymysql.connect(host='localhost',user='root',password='vignesan',db='math')
cursor=db.cursor()
sql="SELECT `name`,`number`,`email`,`state` FROM demo"#the simple is important
try:
    cursor.execute(sql)
    r=cursor.fetchall()
    print(r)
    for row in r:
        print(row)
        n=row[0]
        v=row[1]
        print("name=%s,password=%s"%(n,v))
except:
    db.rollback()
    db.close()"""
