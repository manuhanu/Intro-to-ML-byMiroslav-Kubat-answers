import numpy as np
import pandas as pd

df = pd.read_csv('pies.csv',header =0)
df = df.rename(columns ={'class':'clss'})

def naive_bayes(atts,df):
    cols=df.columns.values.tolist()
    px_given_pos=1
    px_given_neg=1
    for i in cols[0:5]:
        cond_prob_mat = pd.crosstab(df[i],df['clss'],normalize='columns')
        px_given_pos*=cond_prob_mat.loc[atts[i],'pos']
        px_given_neg*=cond_prob_mat.loc[atts[i],'neg']
    
    if px_given_pos>px_given_neg:
        return('most probable class for the given set of attributes is positive')
    else: return('most probable class for the given set of attributes is negative')
 
x = {'shape': 'square',
     'crust-size': 'thick',
     'crust-shade': 'gray',
     'filling-size': 'thin',
     'filling-shade': 'white'}
naive_bayes(x,df)
