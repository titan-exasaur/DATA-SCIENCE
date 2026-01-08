import pandas as pd
import numpy as np

input_array = np.array([1,2,3,4,5])
output_array = np.array([2,3,4,5,6])

x = input_array.reshape(-1,1)
y = output_array.reshape(-1,1)

from sklearn.linear_model import LinearRegression
linear_regressor = LinearRegression()
linear_regressor.fit(x,y)
print("Training Linear Regression Model")

import joblib
joblib.dump(linear_regressor, "linreg.pkl")
print("Training and saving complete...")