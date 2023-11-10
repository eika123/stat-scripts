import numpy as np
from numpy import sqrt, log, pi, sin, cos
import matplotlib.pyplot as plt

N = 10000000

## Box-Muller algorithm - see Casella & Berger page 249
# Choose two *independent* uniform(0,1) variables
U1 = np.random.uniform(0,1, N)
U2 = np.random.uniform(0,1, N)

R = sqrt(-2*log(U1))
theta = 2*pi*U2

X = R*cos(theta)
Y = R*sin(theta)

# Now X and Y are independent normal(0,1) random variables

print(np.corrcoef(X, Y))


if N < 10000:
    plt.plot(X)
    plt.plot(Y)
    plt.show()

