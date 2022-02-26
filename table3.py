import math as m


#### rows in the table ####
n=6

#### name of the variable ####
n_func="P(L)"

#### name of the variable ####
n_var="L"

#### initial value ####
x=0

#### increment ####
increment=5

table="\\begin{tabular}{|c|c|}\hline{\cellcolor{medium_gray}}\\textcolor{white}{$" + n_var + "$}&{\cellcolor{medium_gray}}\\textcolor{white}{$" + n_func+ "$}\\\\\hline"
for k in range(n):
    #xs=str(round(x,2))
    xs=str(x)

    ##### function  ####
    r=200*x+10*x**2-x**3

    rs=str(round(r,2))
    #rs=str(r)
    s="{\cellcolor{white}}\\textcolor{gray}{$"+xs+"$}&{\cellcolor{white}}\\textcolor{gray}{${"+rs+"}$}\\\\\hline"
    table=table+s
    x=x+increment
print(table)
