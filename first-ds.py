import numpy as np
import random
import pandas as pd
schoolData = {'name':['Tunji','Tunde','Tolu','James'],'age':[22,21,19,17],'department':['Math','Agriculture','Botany','physics']}
df = pd.DataFrame(schoolData)
print (df)
print(df.describe())
print(df['name'])
Older = df['age'] >19
dff = df[Older]
print(dff)