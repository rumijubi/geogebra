import math as m
import pandas as pd
import numpy as np

####  5 rows in the table ####
n=8

#### 4 name of the variable ####
n_func="f(x)"

#### 3 name of the variable ####
n_var="x"

#### 2 initial value ####
x=0

#### 1 increment ####
increment=1

table="\\begin{tabular}{|c|c|}\hline{\cellcolor{medium_gray}}\\textcolor{white}{$" + n_var + "$}&{\cellcolor{medium_gray}}\\textcolor{white}{$" + n_func+ "$}\\\\\hline"
for k in range(n):
    #xs=str(round(x,2))
    xs=str(x)

    #### 0 function ####
    r=2-np.sin(x)-x**.5

    rs=str(round(r,2))
    #rs=str(r)
    s="{\cellcolor{white}}\\textcolor{gray}{$"+xs+"$}&{\cellcolor{white}}\\textcolor{gray}{${"+rs+"}$}\\\\\hline"
    table=table+s
    x=x+increment
df=pd.DataFrame([table])
df.to_clipboard(index=False, header=False)
print(table)
