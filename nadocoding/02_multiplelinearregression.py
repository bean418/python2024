# -*- coding: utf-8 -*-
"""02_multipleLinearRegression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pDdkBu2ADMxZH_I_fWD74dRNOXgtEHt2

# Multiple Linear Regression
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("MultipleLinearRegressionData.csv")

df.head()

df.shape

df.dtypes

X = df.iloc[:, :-1]
y = df.iloc[:, -1]
print(X, y)

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers = [('encoder', OneHotEncoder(drop = "first"), [2])], remainder = 'passthrough')
# first column을 drop한다. -> 다중공선성 문제 해결

X = ct.fit_transform(X)

X

# 1 0 : Home
# 0 1 : Library
# 0 0 : Cafe

"""## Seperate Data Set"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

"""## Machine Learning (Multiple regression)"""

from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(X_train, y_train)

"""## Compare predicted value and actual value"""

y_pred = reg.predict(X_test)
y_pred

y_test

print(reg.coef_, reg.intercept_)

print(reg.score(X_train, y_train), '\n',
      reg.score(X_test, y_test))

"""## Model Evaluation

1. MAE : Mean Absolute Error
2. MSE : Mean Squared Error
3. RMSE : Root Mean Squared Error
4. R2 : Coefficient of Determination
"""

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

mean_absolute_error(y_test, y_pred)

mean_squared_error(y_test, y_pred)

mean_squared_error(y_test, y_pred, squared = False)
# RMSE

r2_score(y_test, y_pred)

reg.score(X_test, y_test)

# reg.score은 R2 값을 반환한다.