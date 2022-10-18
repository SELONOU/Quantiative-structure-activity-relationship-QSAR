import pandas as pd
df=pd.read_csv('57_compounds_all_indices.csv', header=None, usecols=[247,249,330,288,7,53,23,212,342])
print(df)
df.to_csv('indices_equations_choose_header.csv')
df.to_csv('indices_equtions_choose_without_header.csv', header=None, index=False)
