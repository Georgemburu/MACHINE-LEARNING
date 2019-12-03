''' 
[1,3] => 0
[3,1]=>1
[2,1]=>1
[1,2] => 0
[3,2]=> 0
[2,3]=> 0
'''
import numpy as np
alpha = 0.05
weights = np.array([0.2,0.4])
trainingData = np.array([
    [1,3],#home
    [3,1],#away
    [2,1],#away
    [1,2],#home
    [2,3],#home
    [3,2],#away
    ])
trainingLabels = np.array([0,1,1,0,0])

for iteration in range(40):
    for i in range(len(trainingData)):
        input = trainingData[i]
        print('input=>',input)

        prediction = input.dot(weights)
        print('prediction',prediction)
        if(prediction>0.5):
            print('away team WON')
        else:
            print(' home team  WON')
        label = trainingLabels[i]
        error = (prediction-label)**2
        print('error',error)
        delta = prediction-label

        weights = weights- (alpha*(input*delta))