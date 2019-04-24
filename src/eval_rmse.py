#!/usr/bin/env python

import sys
import pandas as pd
import numpy as np


from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


def rmse(y_actual, y_predicted):
    return sqrt(mean_squared_error(y_actual, y_predicted))

df = pd.read_csv(sys.argv[1])
print(df.head())

x_train, x_test, y_train, y_test = train_test_split(df.freesolv, df.freesolv, test_size=0.2)
for y in y_test:
    print(np.random.choice(y_train),y)
