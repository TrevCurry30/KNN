"""
K Nearest Neighbors

- X is the feature and y is the label.
- The variable 'new' is the new data point.
- Create a new variable called 'Closest', which is the closest current item in the list.
- Create a new variable called 'Index_of_Closest', which is the index of the closest item in the list.
- Make a for loop that goes through every value of X.
- In the for loop, check if the absolute value of the difference between X[i] and new is less than the absolute value of the difference between Closest and new.
- If the above statement is true, then set Closest = X[i]
- As well as the above, set Index_of_Closest = i
- Once the last iteration of the loop is completed, find y[Index_of_Closest], which is the new label for 'new'
"""


X = [1, 2, 4, 16, 17, 18, 19]
y = [0, 0, 0, 1, 1, 1, 1]
new = 14
Closest = 1000000000000000

for i in range(len(X)):
    if abs(X[i]-new) < abs(Closest-new):
        Closest = X[i]
        Index_of_Closest = i

new_label = y[Index_of_Closest]
print(new_label)
