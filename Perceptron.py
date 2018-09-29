
import random
import matplotlib.pyplot as plt

X1 = [1,1,1,2,3,6,7,8,9,9]
X2 = [3,4,5,4,5,1,2,1,2,1]
y = [1,1,1,1,1,0,0,0,0,0]

i=0
while(i<10):
    if(y[i] == 0):
        plt.scatter(X1[i], X2[i], s=30, c=(1,0,0))
    elif(y[i] == 1):
        plt.scatter(X1[i], X2[i], s=30, c=(0,1,0))
    i=i+1
    
w0 = random.randint(1,10)
w1 = random.randint(1,10)
w2 = random.randint(1,10)

def draw_Line(w0,w1,w2):
    k=0
    Y = [0,0,0,0,0,0,0,0,0,0]
    X = [1,2,3,4,5,6,7,8,9,10]
    while(k<10):
        Y[k] = -(w1/w2)*X[k] + w0/w2
        if(y[k] == 0):
            plt.scatter(X1[k], X2[k], s=50, c=(1,0,0))
        elif(y[k] == 1):
            plt.scatter(X1[k], X2[k], s=50, c=(0,1,0))
        k=k+1
    plt.plot(X,Y,'b')
    plt.show()
    
draw_Line(w0,w1,w2)

calculated_Y=[0,0,0,0,0,0,0,0,0,0]


iteration=0

while(iteration<100):
    i=0
   
    while(i<10):
   
        calculated_Y[i]=w0+(w1*X1[i])+(w2*X2[i])
    
        if(calculated_Y[i]<0 and y[i]==1):
            w1=w1+X1[i]
            w2=w2+X2[i]
            w0=w0+((X1[i]+X1[i])/2)
        
        if(calculated_Y[i]>0 and y[i]==0):
            w1=w1-X1[i]
            w2=w2-X2[i]
            w0=w0-((X1[i]+X1[i])/2)
        
        i=i+1
        
    iteration=iteration+1
    
draw_Line(w0,w1,w2)

                                 



 