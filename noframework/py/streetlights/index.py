'''
[0,1,0]=>stop
[1,0,1]=>walk
[0,0,1]=>walk
[0,1,1]=>stop
[1,1,1]=>stop
[0,0,0]=>walk
[1,0,0]=>walk
[1,1,0]=>stop
'''
'''
0 => stop
1 => walk
'''
import numpy as np

weights = np.array([0.1,-0.5,0.5])
alpha = 0.01
trainingData = np.array([
    [0,0,0],
    [0,1,1],
    [0,0,1],
    [1,1,1],
    [0,1,1],
    [1,0,1],
    # test data
    [1,0,0], #=>stop / 0 
    [0,1,0], #=>stop/0
    ])
trainingLabel = np.array([0,1,0,1,1,0])


for iteration in range(70):
    
    for i in range(len(trainingLabel)+1):
        input = trainingData[i]
        print('input=>',input)
        prediction = input.dot(weights)
        print('prediction',prediction)
        try:
            label = trainingLabel[i]
            print('Label=>',label)
        except:
            print('no label')
        
        if prediction>0.5:
            print('WALK')
        else:
            print('STOP')
        error = (prediction - label) **2
        print('error',error)
        delta = prediction - label
        print('delta',delta)

        # adjust the weights
        weights = weights - (alpha *(input*delta))



