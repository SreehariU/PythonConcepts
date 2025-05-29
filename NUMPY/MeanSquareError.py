import numpy as np

def MSE(prediction,label):
    n=np.size(prediction)
    val=(1/n)*(np.sum(np.square(np.subtract(prediction,label))))
    return val

p=np.array([1,2,3])
l=np.array([1,2,3])
val=MSE(p,l)
print("MSE:",val)

