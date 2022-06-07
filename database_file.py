import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import pymysql 


#conn = pymysql.connect("localhost", "root", "", "dei_projects")
conn=pymysql.connect(host='localhost',user='root',password='',database='dei_projects',charset='utf8mb4',
cursorclass=pymysql.cursors.DictCursor)
cursor=conn.cursor(pymysql.cursors.DictCursor)
cursor.execute("select COL7, COL8 from damped_3 ")
data = cursor.fetchall()
df = pd.DataFrame(data, columns=['COL7', 'COL8'])


    

x=df['COL7']
y=df['COL8']

plt.plot(y,x)
plt.show()





