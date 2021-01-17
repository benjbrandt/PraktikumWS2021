import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import math

f, fh, phi, deltaphi, A_s, A_g = np.genfromtxt('Frequenzabhängigkeit.txt', unpack=True)

x=np.linspace(0, 300000)
plt.plot(x, (0.7)/(np.sqrt((1-3.5*10**(-3)*5*10**(-9)*x**2)**2+x**2*271.6**2*(5*10**(-9))**2)))

plt.xlim(100000, 300000)
plt.title('Kondensatorspannung theoretisch')
plt.xlabel('f [Hz]')
plt.ylabel(r'$U_c$''[V]')
plt.savefig('Frequenzabhängigkeit.theorie.pdf')