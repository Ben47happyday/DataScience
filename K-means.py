import pandas as pd 
import numpy as numpy
import random as rd 
import matplotlib.pyplot as plt

data = pd.read_csv ('clustering.csv')

k = 4 

x = data[["LoanAmount","ApplicantIncome"]]
centroid = (x.sample(n=k))

plt.scatter(x["ApplicantIncome"],x["LoanAmount"], c="grey")
plt.scatter(centroid["ApplicantIncome"],centroid["LoanAmount"], c= 'red')
plt.xlabel('MonthIncome')
plt.ylabel('Load Amount')



plt.show()
