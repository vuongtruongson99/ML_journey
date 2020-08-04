import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data_train = pd.read_csv("./datasets_train1.csv")
data = data_train.values
print(len(data))
print(data[1, 0])