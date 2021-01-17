import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import math

f, phi, deltaphi, A_s, A_g = np.genfromtxt('Frequenzabhängigkeit.txt', unpack=True)

def U(f):
    return 0.7 / math.sqrt((1-3.5*5.0)^2+f^2 *30.3^2* 5.0^2)
plt.plot(f, U)
plt.savefig('Kondensatorspannung.pdf')
