import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import MySQLdb
from flask_mysqldb import MySQL 

style.use("fivethirtyeight")

fig =plt.figure()
ax1=fig.add_subplot(1,1,1)

def animate(i):
    conn = MySQLdb.connect("localhost", "root", "", "hnproject")
    cursor=conn.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("select * from exam")
    graph_data = cursor.fetchall()
    print(graph_data)
        
    #graph_data=open('exam.txt','r').read()
    lines = graph_data.split(",")
    xs=[]
    ys=[]
    for line in lines:
        if len(line)>1:
            x, y = line.split(',')
            xs.append(x)
            ys.append(y)
    ax1.clear()
    ax1.plot(xs, ys)

ani=animation.FuncAnimation(fig, animate, interval=1000)
plt.show()