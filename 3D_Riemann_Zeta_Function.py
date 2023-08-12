import numpy as np
import matplotlib.pyplot as plt
from scipy.special import zeta
from sympy import lambdify, symbols, Eq, solve

# Define the Riemann zeta function
def riemann_zeta(s):
    return zeta(s)

# Evaluate and visualize the zeta function for various real inputs
s_real = np.linspace(0.1, 20, 100)

zeta_values_real = riemann_zeta(s_real)

plt.figure(figsize=(10, 6))
plt.plot(s_real, np.real(zeta_values_real), label='Real part')
plt.plot(s_real, np.imag(zeta_values_real), label='Imaginary part')
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.legend()
plt.title('Riemann Zeta Function')
plt.grid()
plt.show()
