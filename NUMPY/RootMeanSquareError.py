import numpy as np

def RMSE(prediction,label):
    n=np.size(prediction)
    rmse=np.sqrt(np.sum(np.square(np.subtract(prediction,label))*(1/n)))
    return rmse
p=np.array([1,2,3])
l=np.array([1,2,3])
val=RMSE(p,l)
print("RMSE:",val)
