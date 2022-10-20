import pandas as pd
df=pd.read_csv('input_indices.csv', sep=",", header=None, usecols=[0,1])
df1=df[0]
df2=df[1]
print(df1)
print(df2)
with open("indices_input_files.txt", "w") as f:
    for i in range(len(df)):
            file_name=df[0][i]
            number=df[1][i]
            f.write("@echo off\n")
            f.write("set logfile="+file_name+"sp.log\n")
            f.write("set sq=sq.dat\n")
            f.write("set ind="+file_name+"sp.ind\n")
            f.write("set sal="+file_name+"sp.sal\n")
            f.write("set natom="+"0"+str(number)+"\n")
            f.write("set input=0\n")
            f.write("set basis=03\n")
            f.write("(echo %natom% && echo %input% && echo %basis%) | INDICES-AGOSTO-GASTONK.exe %logfile% %sq% %ind% %sal%\n")
    f.write("\n")
