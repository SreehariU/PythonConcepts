def check(limit, oddoreven):
    i=0
    list1=[]
    while (i<limit):
        if(oddoreven=="odd" and i%2!=0):
            list1.append(i)
        elif(oddoreven=="even" and i%2==0):
            list1.append(i)
        i+=1
    return(list1)

def check1(limit, oddoreven):
    i=0
    if oddoreven=='even':
        list1=[i for i in range(limit) if i%2==0]
    if oddoreven=='odd':
        list1=[i for i in range(limit) if i%2!=0]
    
    return(list1)

while(1):
    
    i=int(input("Enter Option: \n\t0-- EVEN\n    \t1-- ODD \n\t2-- EXIT"))
    n=int(input("Enter limit: "))
    list2=[]
    if(i==0):
        list2=check1(n,'even')
    elif(i==1):
        list2=check1(n,'odd')
    elif(i==2):
        print("EXITING")
        break
    else:
        print("ENTER VALID INPUT")
    print(list2)
    print("\n")

