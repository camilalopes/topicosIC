import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.optimize import minimize

def rosen(parametros):
    x1, x2 = parametros
    return 100.0 * (x1-x2 ** 2.0) ** 2.0 + (x2-1) ** 2

x1 = np.arange(-2, 3)
x2 = np.arange(-2, 3)
y = rosen([x1, x2])
print('y ')
print(y)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x1, x2, y)


x0 = np.array([-100, -100])
resultado = minimize(rosen, x0)

print('resultado x ')
print(resultado.x)
print('resultado y ')
print(resultado.fun)