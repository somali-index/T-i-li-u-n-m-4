import numpy as np
import matplotlib.pyplot as plt

x=np.array([[147,150,153,158,163,165,168,170,173,175,178,180,183]]).T
y=np.array([[49,50,51,54,58,59,60,62,63,64,66,67,68]]).T

plt.plot(x,y, 'ro')
plt.axis([140, 190, 45, 75])
plt.xlabel('cao')
plt.ylabel('nang')


one = np.ones((x.shape[0], 1))
xbar = np.concatenate((one, x), axis=1)

A = np.dot(xbar.T, xbar)
w = np.dot(xbar.T, y)
b = np.dot(np.linalg.pinv(A),w)
print('w =', w)
print ('A=',A)
print('b=',b)

b_0=b[0][0]
b_1=b[1][0]
x0=np.linspace(145, 185, 2, endpoint=True)
y0=b_0+b_1*x0
plt.plot(x0,y0)
plt.show()

b_0 = b[0][0]
b_1 = b[1][0]


x_new = 200
y_new = b_0 + b_1 * x_new
print("Khi chiều cao =", x_new, "cm")
print("Cân nặng dự đoán =", y_new, "kg")