
# By using the same procedure, find the values of P(L) for different values of L.
# To get the points for drawing the graph of P and L, make a table with the calculated values of P(L).


import math as m
import pandas as pd

####  5 rows in the table ####
n=6

#### 4 name of the variable ####
n_func="P(L)"

#### 3 name of the variable ####
n_var="L"

#### 2 initial value ####
x=0

#### 1 increment ####
increment=5

table="\\begin{tabular}{|c|c|}\hline{\cellcolor{medium_gray}}\\textcolor{white}{$" + n_var + "$}&{\cellcolor{medium_gray}}\\textcolor{white}{$" + n_func+ "$}\\\\\hline"
for k in range(n):
    #xs=str(round(x,2))
    xs=str(x)

    #### 0 function ####
    r=200*x+10*x**2-x**3

    rs=str(round(r,2))
    #rs=str(r)
    s="{\cellcolor{white}}\\textcolor{gray}{$"+xs+"$}&{\cellcolor{white}}\\textcolor{gray}{${"+rs+"}$}\\\\\hline"
    table=table+s
    x=x+increment
df=pd.DataFrame([table])
df.to_clipboard(index=False, header=False)
print(table)
