# %%
import numpy as np

a = np.array([[3,6,9],[2,4,6]])

print(a)

# %%
import numpy as np

x = np.arange(12).reshape(3,4)

print(x)
# %%
import numpy as np

y = x[np.ix_([0,2],[1,3])]

print(y)

# %%
# Excercise_8
import numpy as np
randomInt=np.random.randint(1,21,20)
print(randomInt)
randomInt2=randomInt.reshape(5,4)
print(randomInt2)
randomInt3=randomInt2[np.ix_([0,4],[0,3])]
print(randomInt3)

# %%
# matplotlib
import matplotlib.pyplot as plt
import mpl_tc_fonts
mpl_tc_fonts.show_font_setting()
x = np.arange(0, 5, 0.1)
y = np.square(x)

plt.plot(x,x,'r--',x,x*2,'bs',x,x*3,'g^')
plt.title("數據圖")
plt.xlabel("横坐標")
plt.ylabel("縱坐標")
plt.show()

# %%       
# Exercise_8

import numpy as np
np_rand=np.random.randint(1,21,size=20)
print("隨機正整數:",np_rand)
print("X矩陣內容:")
x=np_rand.reshape(5,4)
print(x)
print("最大:",np.max(np_rand))
print("最小:",np.min(np_rand))
print("平均:",np.mean(np_rand))
print("總和:",np.sum(np_rand))
print("標準差:",np.std(np_rand))
z = x[np.ix_([0,-1],[0,-1])]
print("四個角落元素:")
print(z)

# %%       
# Exercise_9


# %% 
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(500,3), columns=list('xyz'), index=pd.date_range('1/1/2022', periods=500))

df = df.cumsum()

df.plot(colormap='gray').set_ylabel('Value', fontsize=12,)

df2 = pd.DataFrame(np.random.rand(5,3), columns=['a', 'b', 'c'])

df2.plot(kind='bar', fontsize=12, stacked=True)
# %%


# mysql
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")