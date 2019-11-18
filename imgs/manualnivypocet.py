# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt


# Example data
defocus = [-1, -2, -3, -4, -5, -6, -7, 0, 1, 2, 3, 4, 5, 6]
rotation = [-70.73, -67.73, -56.77, -48, -33.8, 28.23, -2, -79.81, -86.38, -87.94, -96.38, -112, -141, -116]

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

colors = (0,0,0)
area = np.pi*3

fit = np.polyfit(defocus, rotation, 1)
fit_fn = np.poly1d(fit) 
# Plot
plt.scatter(defocus, rotation, s=area, c=colors, alpha=0.5)


plt.plot(defocus, rotation, 'yo', defocus´, fit_fn(defocus), '--k')

plt.xlabel(r'$\Delta z$ [$\mu$m]', fontsize=16)
plt.ylabel(r'$\Delta \varphi$ $\left[ ^\circ\right]$', fontsize=16)
plt.title(r"Plan Fluor 20",
          fontsize=16, color='black')
# Make room for the ridiculously large title.
#plt.subplots_adjust(top=0.8)

plt.savefig('vysledek.pdf', format='pdf')
plt.savefig('vysledek.png', format='png')
plt.savefig('vysledek.svg', format='svg')
plt.show()