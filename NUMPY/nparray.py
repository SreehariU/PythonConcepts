import numpy as np

#creating arrays
list0=np.array(0)
list1 = np.array([9,3,6,4,2,7,8])
list11 = np.array([9,3,6,4,2,7,8])
list2 = np.array(['b','a'])
list3 = np.array([[1,2,3],
                  [4,4,5],
                  [6,7,8]])
list4 = np.array([[11,22,33],
                  [44,45,65],
                  [69,78,87]])

#datatypes of arrays
print(list1.dtype)
print(list2.dtype)

#var type check
print(type(list1))

#slicing array
print(list3[:1])
print(list1[:2])

#dimension check
print(list3.ndim)
print(list0.ndim)

#shape row * coloum
print(list3.shape)
print(list1.shape)

#size
print(list3.size)

#array operation
print(np.concatenate((list1,list11)))
print(np.sort(list1))

#condition
print(list1[list1>5])
check=(list1>=5)
print(list1[check])

#stacking
print(np.hstack((list3,list4)))
print(np.vstack((list3,list4)))

#broadcasting
print("broatcasting\n")
list3=list3*10
print(list3)

#list operations
print("\nList Operations\n")
print("\nSum:",np.sum(list3))
print("\nMax:",np.max(list3))
print("\nMim:",np.min(list3))