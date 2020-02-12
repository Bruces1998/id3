'''
Function to calculate entropy
and
Information gain
'''
#imports
import numpy as np
import pandas as pd

#data loading and preprocessing
data = pd.read_csv('data.csv')
columns = []
for column in data:
    columns.append(column)
columns = columns[1:]
target = columns.pop()


#function entropy
def entropy(no_of_positives, no_of_negatives):
    pn = no_of_positives/(no_of_negatives+ no_of_positives)
    ng = no_of_negatives/(no_of_negatives+no_of_positives)
    if pn==0:
        return float(0 + (ng * np.log2(ng)))
    elif ng ==0:
        return float((pn* np.log2(pn)) + 0)
    else:
        return float(-(pn* np.log2(pn)) -(ng * np.log2(ng)))


#function information_gain
def info_gain(data):#data is of form .....
    ent = entropy(list(data[1]).count('Y'), list(data[1]).count('N'))
    w_sum = 0
    child = {}
    for i in set(data[0]):
        child[i] = []

    for i,j in zip(data[0],data[1]):
        child[i].append(j)
    for keys in child:
        w_sum = w_sum + entropy(child[keys].count('Y'), child[keys].count("N"))*(child[keys].count('Y')+child[keys].count("N"))/(list(data[1]).count('Y')+ list(data[1]).count('N'))


    return ent - w_sum

#Results
infoResults = []
for column in columns:
    infoResults.append(info_gain([list(data[column]), list(data[target])]))
dataf = pd.DataFrame()
dataf["Attributes"] = columns
dataf["IG"] = infoResults
print(dataf)
