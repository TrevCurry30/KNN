"""
K Nearest Neighbors Classifier
"""
import numpy as np

def KNN_Classifier(X_train, y_train, new): 
    """This function computes the class of a given data_point using the KNN algorithm."""
    Index_of_Closest = 0
    for i in range(len(X_train)):
        if compute_distance(X_train[i], new) < compute_distance(X_train[Index_of_Closest], new):
            Index_of_Closest = i
    new_label = y_train[Index_of_Closest]
    return new_label

def compute_distance(arr1, arr2):
    """This function returns the distance between two points with any number of dimensions"""
    dist=0
    for i in range(len(arr1)):
        temp=arr1[i]-arr2[i]
        temp=temp**2
        dist+=temp
    return np.sqrt(dist)

# Generating data
X_train = np.array([[1,3], [4,2], [6,7], [11, 14], [9, 15], [10, 13], [18,20]])
#X_train = [1, 2, 4, 16, 17, 18, 19]
y_train = [0, 0, 0, 1, 1, 1, 1]
X_test = np.array([[-2, 1], [2,4], [6,5], [-10, 23], [10, 12], [15, 12], [18, 21]])
#X_test = [-2, 6, 10.9, 12, 18.5, 24, 38]

# CLassifying new datapoints
for new in X_test:
    print(KNN_Classifier(X_train, y_train, new))
