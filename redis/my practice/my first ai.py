from sklearn.datasets import load_iris
import pandas as pd
iris= load_iris()
df =pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target']=iris.target_names[iris.target]
print(df.head())



