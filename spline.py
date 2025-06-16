import scipy.interpolate as scipl
import numpy as np
import matplotlib.pyplot as plt


x_lis =[
0,
132,
33,
10,
20,
30,
40,
50,
60,
70,
80,
90,
100,
110,
120,
130,
140,
150,
160,
170,
180,
190,
200,
220,
250
]

y_lis =[
0,
173,
67,
23,
44,
62,
78,
93,
107,
118,
129,
139,
148,
157,
165,
172,
178,
185,
190,
196,
202,
206,
211,
219,
230,
]

# 昇順にソート
x_lis_np = np.array(x_lis)
y_lis_np = np.array(y_lis)
sort_idx = np.argsort(x_lis_np)
x_lis_sorted = x_lis_np[sort_idx]
y_lis_sorted = y_lis_np[sort_idx]


x = np.arange(x_lis_sorted[0], x_lis_sorted[-1]+0.1, 0.1)
f_sci=scipl.CubicSpline(x_lis_sorted,y_lis_sorted)

# coeffs = np.polyfit(x_lis_sorted, y_lis_sorted, deg=len(x_lis_sorted)-1)
# poly25 = np.poly1d(coeffs)
# print(poly25)

# coeffs = np.polyfit(x_lis_sorted, y_lis_sorted, deg=len(x_lis_sorted)-16)
# poly10 = np.poly1d(coeffs)
# print(poly10)

coeffs = np.polyfit(x_lis_sorted, y_lis_sorted, deg=len(x_lis_sorted)-21)
poly5 = np.poly1d(coeffs)
print(poly5)

coeffs = np.polyfit(x_lis_sorted, y_lis_sorted, deg=len(x_lis_sorted)-21)
poly4 = np.poly1d(coeffs)
print(poly4)

coeffs = np.polyfit(x_lis_sorted, y_lis_sorted, deg=len(x_lis_sorted)-23)
poly3 = np.poly1d(coeffs)
print(poly3)


plt.plot(x_lis_sorted, y_lis_sorted,'o')
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