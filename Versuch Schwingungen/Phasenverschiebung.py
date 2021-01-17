import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import math

f, fh, phi, deltaphi, A_s, A_g = np.genfromtxt('Frequenzabhängigkeit.txt', unpack=True)
plt.plot(fh, deltaphi, 'xr', label='Messwerte')
L= 3.5*10**(-3)
C= 5.0*10**(-9)
R= 271.6
plt.plot(fh, 100*(-np.arctan((-fh*R*C)/(1-L*C*fh**2))), label=r'$\Delta \phi(f)$')

plt.xlim(0, 65000)
plt.title('Phasenverschiebung')
plt.xlabel('f [Hz]')
plt.ylabel(r'$\Delta \phi \, [\mu s]$')
plt.legend()
plt.savefig('Phasenverschiebung.pdf')
