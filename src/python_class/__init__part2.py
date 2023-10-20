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