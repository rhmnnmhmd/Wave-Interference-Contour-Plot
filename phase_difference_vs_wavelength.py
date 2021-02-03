import math
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import pandas as pd
import sympy as sym

def theta(lamda, d):
    return 8.113*lamda/d

lamda = np.linspace(3.8e-7, 7.0e-7, 100)

plt.plot(lamda*1e7, theta(lamda, 0.1)*(1e5), label = "0.1m")
plt.plot(lamda*1e7, theta(lamda, 0.2)*(1e5), label = "0.2m")
plt.plot(lamda*1e7, theta(lamda, 0.4)*(1e5), label = "0.4m")
plt.plot(lamda*1e7, theta(lamda, 0.6)*(1e5), label = "0.6m")
plt.plot(lamda*1e7, theta(lamda, 0.8)*(1e5), label = "0.8m")
plt.plot(lamda*1e7, theta(lamda, 1)*(1e5), label = "1m")

plt.title("Plot of $\Delta \Theta_{min}$ vs $\lambda$ for different $d$ (object distance from lense) values")
plt.legend()
plt.xlabel("Wavelength, $\lambda$ ($\cdot 10^{-7}$m)")
plt.ylabel("Minimum angular separation, $\Delta \Theta_{min}$ ($\cdot 10^{-5}$ rad)")
plt.grid(True)
plt.savefig("photo")

plt.show()

