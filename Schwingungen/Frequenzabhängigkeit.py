import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import math

f, fh, phi, deltaphi, A_s, A_g = np.genfromtxt('Frequenzabhängigkeit.txt', unpack=True)


plt.plot(fh, A_s, 'xr')
plt.xlim(0, 65000)
plt.title('Kondensatorspannung gemessen')
plt.xlabel('f [Hz]')
plt.ylabel(r'$U_c$''[V]')
plt.savefig('Frequenzabhängigkeit.pdf')

