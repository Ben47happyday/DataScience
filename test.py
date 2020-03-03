import pandas as pd 
import numpy as np
import random as rd 
import matplotlib.pyplot as plt


d = {'col1':[1,2,3,4,5],'col2':[11,12,13,14,15]}

df = pd.DataFrame(data=d)



print(df)

#X.groupby(["Cluster"]).mean()[["LoanAmount","ApplicantIncome"]]