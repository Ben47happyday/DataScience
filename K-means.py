import pandas as pd 
import numpy as np
import random as rd 
import matplotlib.pyplot as plt

data = pd.read_csv ('clustering.csv')

K = 4


color=['blue','green','cyan','yellow']



X = data[["LoanAmount","ApplicantIncome"]]

print(X) 

Centroids = (X.sample(n=K))

plt.scatter(X["ApplicantIncome"],X["LoanAmount"], c="grey")
plt.scatter(Centroids["ApplicantIncome"],Centroids["LoanAmount"], c= 'red')
plt.xlabel('MonthIncome')
plt.ylabel('Load Amount')

# Step 3 - Assign all the points to the closest cluster centroid
# Step 4 - Recompute centroids of newly formed clusters
# Step 5 - Repeat step 3 and 4

diff = 1
j=0

while(diff!=0):
    XD=X
    i=1
    for index1,row_c in Centroids.iterrows():
        ED=[]
        for index2,row_d in XD.iterrows():
            d2=(row_c["LoanAmount"]-row_d["LoanAmount"])**2  
            d1=(row_c["ApplicantIncome"]-row_d["ApplicantIncome"])**2
            d=np.sqrt(d1+d2)
            ED.append(d)
    
        X[i]=ED #cover x[1] to into two columns and 155 rows, which would be (index and distince to centrol)
        print (X[i]) 
        i=i+1

    C=[]

    for index,row in X.iterrows():
        print("row")
        print(row)
        min_dist=row[1]
        
        pos=1
        for i in range(K):
            if row[i+1] < min_dist:
                min_dist = row[i+1]
                pos=i+1
        C.append(pos)
    X["Cluster"]=C  #created an new column and save C values into it
    print ("Cluster Here")
    print (X["Cluster"])
    Centroids_new = X.groupby(["Cluster"]).mean()
    if j == 0:
        diff=1
        j=j+1
    else:
        diff = (Centroids_new['LoanAmount'] - Centroids['LoanAmount']).sum() + (Centroids_new['ApplicantIncome'] - Centroids['ApplicantIncome']).sum()
        print(diff.sum())
    Centroids = X.groupby(["Cluster"]).mean()[["LoanAmount","ApplicantIncome"]]


for k in range(K):
    data=X[X["Cluster"]==k+1]
    plt.scatter(data["ApplicantIncome"],data["LoanAmount"],c=color[k])

plt.scatter(Centroids["ApplicantIncome"],Centroids["LoanAmount"],c='red')
plt.xlabel('Income')
plt.ylabel('Loan Amount (In Thousands)')
plt.show()