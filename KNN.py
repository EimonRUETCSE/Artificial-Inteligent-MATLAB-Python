import numpy as np
import matplotlib.pyplot as plt
import math
import operator
import random




def euDist(x1,x2,l): #Calculating Euclidian Distance

        dist = 0
        for i in range(l):
            dist+=pow((x1[i]-x2[i]),2)
            
        return math.sqrt(dist)

    

def Neigh (train,test,k,dataset): #Calculatinf Nearest Neighbor

        dist=[]
        l=len(test)-1

        for i in range(len(train)):
            d=euDist(test,train[i],l)
            dist.append((dataset[i],d))
            
        dist.sort(key=operator.itemgetter(1))

        #print('Distance: ' + str(dist))

        neighbour=[]
        for i in range(k):
            neighbour.append(dist[i][0])

        return neighbour

def getVote(neighbors): #Voting for test case
    classVotes = {}
    for x in range(len(neighbors)):
        response = int(neighbors[x][-1])
        #print('Class of Neighbors: ' + str(response))
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1

        #print('ClassVotes: ' + str(classVotes))
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse = True)
    return sortedVotes[0][0]


    




def main():
        #Randomly generate dataset
        data=np.random.randint(0, 100, size=[30,2])
        label=np.random.randint(0, 3, size=[30,1])

        #Horizontal stack of data and label
        dataset=np.hstack([data,label])

        #Scatter plot
        plt.scatter(data[:,0],data[:,1],c=label)
        


        plt.show()
        print(dataset)

        #Randomly generate test dataset
        testSet=np.random.randint(0, 30, size=[10,2])

        accu=[]
        k_values=[]

        for i in range(15): #Use different k values
                prediction=[]
                correct = 0
                


               
                    
               
                k=((2*i)+1)#Taking odd values of k
                k_values.append(k)

                for i in range(len(data)):
                        neighbors = Neigh(data, data[i],k,dataset)
                        #print('\n')
                        #print('TestData: ' + str(data[i]))
                        #print('Nearest Neighbors:' + str(neighbors))
                        result= getVote(neighbors)
                        #print('Prediction: ' + str(result))
                        #print('\n')
                 
                        prediction.append(result)


               # print('\n')
               # print('Prediction: ' + str(prediction))


                #Calculating accuracy
                for i in range(len(prediction)):
                             if label[i] == prediction[i]:
                                correct += 1
                accuracy=(correct / (len(prediction))) * 100.0
                accu.append(accuracy)
                       
                print('--------------------------------------------')
                print('K =',str(k))
                print('Accuracy: ' + str(accuracy))

        
                
                
       # print('K_values:'+str(k_values))
       # print('Accu:'+str(accu))

        plt.plot(k_values,accu,label='K VS Accuracy')
        plt.legend(loc='upper center')
        plt.show()
       

         
       
            
    

    

  



main()




        


    
        
