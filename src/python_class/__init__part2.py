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