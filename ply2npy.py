import numpy as np
#首先要把H1_2.npy手动改成.txt后缀
a = np.loadtxt('H1_2.txt', skiprows=12, dtype=float)


print(a)
#Kind= 
print(a.shape)
b = np.ones(50158)
print(b)
c=np.c_[a,b]
np.save('H1_2.npy',c)
c_np=np.load("H1_2.npy")
print(c_np)
