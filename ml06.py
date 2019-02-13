# id = Iris Demo

# importing the numply library and using
# np as my alias to reference it in code

import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree


# Now I want to import the iris datase
iris_data_set = load_iris()

# Print out the features in the dataset
print(" " * 40)
print("Features")
print(iris_data_set.feature_names)

# Print out our flower names aka labels
print(" " * 40)
print("Labels")
print(iris_data_set.target_names)

# Lets take a look at our data
# Lets have a look at the first row
print("-" * 40)
print("We are just going to take a peek at the data. On row 0")
# Notice the data below will line up perfectly with
# the features above
print("Notice the data below will line up perfectly with the features above")
print(iris_data_set.data[0])

# Lets look at the label for this line of data
print("_" * 40)
print("Show the label for row 0. Wre are just taking a peek at the data")
print("Label Table")
print("0=setosa 1=versicolor 2=virginica")
print("label=", iris_data_set.tatget[0])

print("_" * 40)
print("The iris data set will be used to classify 3 types of flowers")
print("The data set is 150 rows. 50 rows for each flower")
print("The rows are in order")
print("0-49 = setosa")
print("50-99 = versicolor")
print("100-149 = virginica")
# Print out the full data set to have a reference
print("_" * 40)
print("The full data set to have a reference")
for i in range(len(iris_data_set.target)):
    print("Example %d: Labels %s: Features %s:" % (i, iris_data_set.target[i], iris_data_set.data[i]))


