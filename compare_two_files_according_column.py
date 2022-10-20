import pandas as pd
df1=pd.read_csv("atoms.csv", header=None, usecols=[0,1])
df2=pd.read_csv("list_choice.csv", header=None, usecols=[0])
target_file=df2[0].map(lambda x:x.split('sp')[0]).to_list()
df_target=df1.loc[df1[0].isin(target_file)]
df_target.to_csv("input_indices.csv", header=None, index=None)
