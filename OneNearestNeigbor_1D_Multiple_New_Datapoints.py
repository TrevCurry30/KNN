"""
K Nearest Neighbors

- X is the feature and y is the label.
- The variable 'news' is the list of new data points.
- Create a function called 'KNN' which takes in 'X', 'y', and 'new' (Everything with an asterisk is inside the function)
* Create a new variable called 'Closest', which is the closest current item in the list.
* Create a new variable called 'Index_of_Closest', which is the index of the closest item in the list.
* Make a for loop that goes through every value of X.
* In the for loop, check if the absolute value of the difference between X[i] and new is less than the absolute value of the difference between Closest and new.
* If the above statement is true, then set Closest = X[i]
* As well as the above, set Index_of_Closest = i
* Once the last iteration of the loop is completed, find y[Index_of_Closest] and save it in 'new_label', which is the new label for 'new'
* Return new_label
- Create a for loop that goes through each item in 'news'
- Inside the for loop, print KNN with inputs 'X', 'y', and 'new'
"""

def KNN(X, y, new): 
    Closest = 1000000000000000
    for i in range(len(X)):
        if abs(X[i]-new) < abs(Closest-new):
            Closest = X[i]
            Index_of_Closest = i
    new_label = y[Index_of_Closest]
    return new_label


X = [1, 2, 4, 16, 17, 18, 19]
y = [0, 0, 0, 1, 1, 1, 1]
news = [-2, 6, 10.9, 12, 18.5, 24, 38]

for new in news:
    print(KNN(X, y, new))
