import numpy as np;
weights = np.array([0.5,1,0.9]);
alpha = 0.01;

streetlights = np.array([
    [0,0,1],
    [0,1,1],
    [0,0,1],
    [1,1,1],
    [0,1,1],
    [1,0,1]
]);
walk_vs_stop = np.array([0,1,0,1,1,0]);

for i in range(40):
    error_for_all_lights = 0;
    for row_index in range(len(streetlights)):
        input = streetlights[row_index];
        goal_prediction = walk_vs_stop[row_index];
        
        prediction = input.dot(weights);
        print('input',input,'weights',weights,'DOT',prediction)

        print('prediction: '+ str(prediction));
        error = (prediction - goal_prediction)**2;

        error_for_all_lights += error;
        delta = prediction-goal_prediction;
        print('delta',delta)
        print('prediction:',prediction,'- goal prediction',goal_prediction,'==',delta)
        print('WEIGHTS bfore',weights)
        print('input',input,'* delta',delta,'input * delta',(input*delta))
        weights = weights - (alpha *(input*delta));
        
        print('alpha *(input*delta)',(alpha *(input*delta)))
        print('WEIGHTS edited',weights)


       
    
    print('Weights:'+str(weights));
    print('Error:'+str(error));
