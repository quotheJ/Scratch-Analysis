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

plt.plot(x_lis_sorted, y_lis_sorted,'o')

legends = []
legends.append('Row data')

lines =["-", "--", "-.", ":"]

def calculate_formula(poly):
    coeffs = np.polyfit(x_lis_sorted, y_lis_sorted, deg=len(x_lis_sorted)-(len(x_lis_sorted)-poly))
    equation = np.poly1d(coeffs)
    print(f"poly{poly}: {equation}")
    plt.plot(x, equation(x), lines[3%poly], label=f'Polynomial Fit {poly}')
    legends.append(f'Polynomial Fit {poly}')

calculate_formula(6)
calculate_formula(5)
calculate_formula(4)
calculate_formula(3)
calculate_formula(2)
calculate_formula(1)

plt.xlabel('x [-]')
plt.ylabel('y [-]')
plt.legend(legends)
plt.show()