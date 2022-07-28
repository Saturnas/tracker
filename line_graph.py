from matplotlib import animation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sqlite3 as sql

##############################
con = sql.connect("data.db")
cur = con.cursor()
statement = "SELECT * FROM currentuser"
cur.execute(statement)
userlist = cur.fetchall()
name = userlist[0][0]
sqlquery = f"SELECT * FROM {name}"
income = []
expenses = []
savings = []
months = [i for i in range(int(len(list(cur.execute(f"SELECT monthly FROM {name}")))))]
for i in cur.execute(f"SELECT * FROM {name}"):
    income.append(i[0]+i[2])
    expenses.append(i[1]+i[3])
    savings.append(i[4])
con.commit()
con.close()

#############################
x = []
y = []
y1 = []
y2 = []
##############################
fig, ax = plt.subplots(figsize =(8, 6))

def animate(i):
	pt = income[i]
	pt1 = savings[i]
	pt2 = expenses[i]
	x.append(i)
	y.append(pt)
	y1.append(pt1)
	y2.append(pt2)
	ax.clear()
	ax.plot(x, y, color='green', linestyle='solid', linewidth = 1, marker='o', markerfacecolor='cyan', markersize=4)
	ax.plot(x, y1, color='blue', linestyle='solid', linewidth = 2, marker='o', markerfacecolor='yellow', markersize=4)
	ax.plot(x, y2, color='red', linestyle='dashed', linewidth = 1, marker='o', markerfacecolor='black', markersize=4)
	ax.set_xlim([0,len(income)])
	ax.set_ylim([min(min(min(income),min(expenses),min(savings)),0),max(max(income),max(expenses),max(savings))+1000])


	ax.legend(['Income','Savings', 'Expenses'],loc='upper right', bbox_to_anchor=(1, 0.5))
	plt.grid(color = 'green', linestyle = '--', linewidth = 0.3)
	plt.xlabel('Months', fontweight ='bold', fontsize = 15)
	plt.ylabel('Amount of money', fontweight ='bold', fontsize = 12)
	plt.title('Income/expenses over time', fontweight ='bold', fontsize = 15)

ani = FuncAnimation(fig, animate, frames=len(income), interval=300, repeat=False)

plt.show()
