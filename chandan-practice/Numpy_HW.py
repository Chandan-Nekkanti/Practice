import numpy as np
from scipy import stats as st

#Q1
arr = np.arange(1,11)
mod_arr = 5*arr-2
print(mod_arr)

#Q2
narr = np.array([8, 20, 22, 20, 10, 20, 22, 8])
print(np.mean(narr))
print(np.median(narr))
print(st.mode(narr)[0])

#Q4
arr3 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr3)
print(arr3[1])
print(arr3[1][1])

