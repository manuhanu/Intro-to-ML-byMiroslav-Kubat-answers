import pandas as pd
import numpy as np

def getk(df,clss):
    m = len(df[df['clss'].str.contains(clss)])
    k =1/(np.sqrt(2*np.pi)**m)
    return k

def getprob(df,clss,atts):
    k=getk(df,clss)
    clssdf = df[df['clss'].str.contains(clss)]
    condp=1
    p=0
    for key in atts:
        for index,row in clssdf.iterrows():
            p+=np.exp(-.5*(atts[key]-clssdf.loc[index,key])**2)
        p*=k
        condp*=p
        p=0
        
    return condp
    

def mostprobableclass(df,v):
    possibleclasses = df['clss'].unique().tolist()
    probs={}
    for i in possibleclasses:
        probs[i]=getprob(df,i,v)
    mostprobable = max(probs,key = probs.get)
    return("most probable class is "+ mostprobable)


df = pd.read_csv('example1.csv')
df = df.rename(columns ={'class':'clss'})
v = {'at1': 9, 'at2': 2.6, 'at3': 3.3}
mostprobableclass(df,v)    
