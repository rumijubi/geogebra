import pandas as pd
import multiprocessing
# small function
def squars(x):
    f1=x*x
    f2=(x+1)*(x+1)
    l=f1, f2
    return [x,l]
# function which need multi-processing for faster processing
def func2(y_list):
    list_par=multiprocessing.Pool().map(squars,lst)
    #create dataframe with results and add one row for each element in input list
    par_df = pd.DataFrame(list_par, columns=['var', 'results'])
    return par_df
lst = list(range(1,1000))
df=func2(lst)
print(df)
