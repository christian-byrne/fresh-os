import pandas as pd

# --Input columns to dataframe
# (disincluding outputs columns -- political compass targets)
# (disincluding anything you can't get data for from census)
X= pd.read_csv(
    '~/btn/btn/btNeutral/algorithm/formatted_data.csv',
    usecols =[0,1,2,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18])

# Convert Target column (what you are predicting) to dataframe
target_column = pd.read_csv(
    '~/btn/btn/btNeutral/algorithm/formatted_data.csv',
    usecols =[21])

# Convert Target Column dataframe to array
Y = []
for i in target_column['party']:
    Y.append(i)

##### -------Troubleshooting------- #####
### check if inputs and tagets are all numbers
# import numpy as np
# print(np.isnan(X).any())
# print(np.isnan(Y).any())
### check if inputs and targets are all finite
# print(np.isfinite(X).any())
# print(np.isfinite(Y).any())
### Rehshape input, target, or test vectors to 2D
### array.reshape(-1, 1) if your data has a single feature
### array.reshape(1, -1) if it contains a single sample
# import numpy as np
# testVec = np.array([1,6,1,52,0,1,0,0,0,0,0,0,0,0,1,-3,0,-2])
# properly_formmated_testVec = testVec.reshape(1, -1)