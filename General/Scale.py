import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn import linear_model 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 
from sklearn.preprocessing import StandardScaler

# Create the arrays that represent the values
scale = StandardScaler()

# Load dataset
df = pd.read_csv("..\Python Tutorial\General\cars.csv")

# Create the arrays that represent the values
X = df[['Weight', 'Volume']]

# Execute a method that returns some important key values of Linear Regression
scaledX = scale.fit_transform(X)

# Print the scaled values
print(scaledX)