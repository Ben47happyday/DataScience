import pandas as pd 
import numpy as numpy
import random as rd 
import matplotlib.pyplot as plt

data = pd.read_csv ('clustering.csv')

for index , each in data.iterrows(): 
    print(each)

