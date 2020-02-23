import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp2d

xlist = [247,288,328,370]
ylist = [990,967.5,945,922.5,900]
X,Y = np.meshgrid(xlist,ylist)

print(X)
print(Y)
Z = [[0.31,0.37,0.34,0.31],
     [0.34,0.42,0.40,0.31],
     [0.37,0.42,0.42,0.34],
     [0.37,0.42,0.40,0.34],
     [0.28,0.40,0.37,0.31]]

# arbitrary grid number
ngrid = 500

# make grid
xi = np.linspace(247,370,ngrid)
yi = np.linspace(990,900,ngrid)

interp = interp2d(xlist,ylist,Z,kind = "cubic")
znew = interp(xi,yi)

print(znew)
contour = plt.contourf(xi,yi,znew)
#plt.scatter(X,Y,c=Z)
#plt.clabel(contour, inline=True, fontsize=8)
plt.xlabel("Width (mm)")
plt.ylabel("Height(mm)")
plt.colorbar()
plt.show()
