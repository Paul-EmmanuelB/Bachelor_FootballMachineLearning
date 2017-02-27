from matplotlib import pyplot as plt
import numpy as np
from ameliorershoot import expf, xexpalpha
import math

x=np.arange(10)
y= 1-np.exp(-x)
y1=x**2


plt.figure(1)
plt.ylim(ymin=0, ymax=15)
plt.plot(x,y,'r')
plt.plot(x,y1,'y')
plt.xlabel('Distance ballon-but')
plt.ylabel('Norme de shoot')
plt.title('Fonctions de shoot')
plt.legend(("y=1-exp(-x)","y=x**2"),'best')
plt.show
