import scipy.interpolate as scipl
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x_list = pd.read_csv("X.csv", header=None)[0].tolist()
y_list = pd.read_csv("Y.csv", header=None)[0].tolist()

# 昇順にソート
x_list_np = np.array(x_list)
y_list_np = np.array(y_list)
sort_idx = np.argsort(x_list_np)
x_list_sorted = x_list_np[sort_idx]
y_list_sorted = y_list_np[sort_idx]


x = np.arange(x_list_sorted[0], x_list_sorted[-1]+0.1, 0.1)
f_sci=scipl.CubicSpline(x_list_sorted,y_list_sorted)

# coeffs = np.polyfit(x_list_sorted, y_list_sorted, deg=len(x_list_sorted)-1)
# poly25 = np.poly1d(coeffs)
# print(poly25)

# coeffs = np.polyfit(x_list_sorted, y_list_sorted, deg=len(x_list_sorted)-16)
# poly10 = np.poly1d(coeffs)
# print(poly10)

coeffs = np.polyfit(x_list_sorted, y_list_sorted, deg=len(x_list_sorted)-(len(x_list_sorted)-5))
poly5 = np.poly1d(coeffs)
print(poly5)

coeffs = np.polyfit(x_list_sorted, y_list_sorted, deg=len(x_list_sorted)-(len(x_list_sorted)-4))
poly4 = np.poly1d(coeffs)
print(poly4)

coeffs = np.polyfit(x_list_sorted, y_list_sorted, deg=len(x_list_sorted)-(len(x_list_sorted)-3))
poly3 = np.poly1d(coeffs)
print(poly3)


plt.plot(x_list_sorted, y_list_sorted,'o')
# plt.plot(x, f_sci(x),'-')
# plt.plot(x, poly25(x), '--', label='Polynomial Fit 25')
# plt.plot(x, poly10(x), '--', label='Polynomial Fit 10')
plt.plot(x, poly5(x), '-', label='Polynomial Fit 5')
plt.plot(x, poly4(x), '--', label='Polynomial Fit 4')
plt.plot(x, poly3(x), '--', label='Polynomial Fit 3')
plt.xlabel('x [-]')
plt.ylabel('y [-]')
plt.legend(['Row data',
            # 'Cubic Spline',
            # 'Polynomial Fit25',
            # 'Polynomial Fit10',
            'Polynomial Fit5', 'Polynomial Fit4', 'Polynomial Fit3'])
plt.show()