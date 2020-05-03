# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 09:33:20 2020

@author: jackf
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

x = [12.8,14.5,15.6,16.8,19.8]
y = [17.7508376, 18.2006998, 18.2170916, 17.9105262,17.0878295]
f2 = interp1d(x, y, kind='cubic')
xnew = np.linspace(12.8, 19.8, num=300, endpoint=True)
ynew = f2(xnew)
#print(str(ynew[np.amax(ynew)])+", "+
 #   str(max(ynew)))
plt.plot(x, y, 'o', xnew, ynew, '-')
plt.legend(['data', 'Estimated line'], loc='best')
plt.xlabel("Water content (%)")
plt.ylabel("Dry Unit Weight (kN/m^3)")
plt.show()
#print(f2(xnew))
