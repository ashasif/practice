import matplotlib.pyplot as plt
a=[]
b=[]
c=[]
i=-20
for i in range(-20,21):
    def f(x):
        return x**2 - 5*x - 6
    x=i
    f1 = 2*x - 5

    tol = x

    y=x-(f(x)/f1)

    count=0

    x=i
    if(x==0):
        y = x - (f(x)/f1)
        tol=y-x
        while (abs(tol)>10**(-5)):
            y=x-(f(x)/f1)
            tol=y-x
            x=y
            count+=1
        #print(y, count)
    elif(x==1 or x==2 or x==3 or x==4):
        continue
    else:
        while (abs(tol)>10**(-5)):
            y=x-(f(x)/f1)
            tol = y-x
            x=y
            count+=1
           # print(y, count)
    print("for i is ", i, " The Root is ", y , "Total iteration",count)
    a.append(i)
    b.append(y)
    c.append(count)
plt.plot(a,b)
plt.show()
plt.plot(a,c)
plt.show()
