# malabanan, angelo - perez, eric
# 2ece-a
# machine problem 5 (python solution)

import matplotlib.pyplot as plt
import numpy as np

# set-up of values of n
nval = (range(0, 200))
n = np.array([range(0,200)])

# input and eval of eqn
eqn = (input("Enter function x(n): "))
eqnval = eval(eqn)
x = eqnval.transpose()

def xf(n):
    return eval(eqn)

def yf (n):
    
    if n==0:
        return (-1.5 * xf(n)) + (2*xf(n+1)) - (0.5 * xf(n+2))
    
    elif n > 0 and n <= 198:
        return (0.5 * xf(n+1)) - (0.5 * xf(n-1))
    
    elif n == 199:
        return (1.5 * xf(n)) - (2 * xf(n-1)) + (0.5 * xf(n-2))

xval = x
yval = [ yf(n) for n in nval ]

plt.plot(nval, xval, 'r', label = 'x(n)')
plt.plot(nval, yval, 'b', label = 'y(n)')
plt.legend()
plt.xlabel('n')
plt.ylabel('x(n) and y(n)')
plt.title('Graphs of x(n) and y(n)')