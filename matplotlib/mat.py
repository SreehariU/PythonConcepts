import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2,100)
plt.figure()
plt.title("TITLE")
plt.plot(x,x,label='linear')
plt.plot(x,x*x,label='quadratic')
plt.plot(x,x**3,label='Cubic')
plt.legend()
plt.xlabel('X label')
plt.ylabel('Y label')
plt.show()