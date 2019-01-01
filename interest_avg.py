import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

print("Loading csv file")
data = pd.read_csv("data.csv")
purpose_dict={}

#Link all loan interest rates associated with the purpose under a purpose key in purpose_dict
for index, row in data.iterrows():
    purpose = row["purpose"]
    interest_rate = row["int_rate"]

    if(purpose in purpose_dict):
        purpose_dict[purpose] = np.append(purpose_dict[purpose], interest_rate)
    else:
        purpose_dict[purpose] = np.array([interest_rate])

#Compute the average interest rate
print("Computing purpose interest averages")
for key in purpose_dict.keys():
    purpose_dict[key] = purpose_dict[key].mean()

#Sort purpose dict for displaying order consistency and split purpose
#keys into x and average interest values into y
lists = sorted(purpose_dict.items())
x, y = zip(*lists)

#For spicy colors ;)
bar_graph = plt.bar(x,y, color= [np.random.rand(3,) for purpose in x]) 

# Adjust the ticks if the x labels are overlapping
#plt.tick_params(axis='x', labelsize=5)

plt.xlabel("Purpose")
plt.ylabel("Avg Interest Percentage")
plt.show()