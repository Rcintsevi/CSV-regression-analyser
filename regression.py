import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def compute_fwb(X,w,b):
    m=X.shape[0]
    fwb=np.zeros(m)
    fwb=w*X+b
    return fwb

def compute_cost(fwb,y):
    m=fwb.shape[0]
    cost=0
    for i in range(m):
        cost+=(fwb[i]-y[i])**2
    return cost/(2*m)

def run_regression(file_path,weight,bias):

    df=pd.read_csv(file_path)

    X = df.iloc[:,0].values.reshape(-1,1)
    y = df.iloc[:,1].values

    w=weight
    b=bias

    fwb=compute_fwb(X,w,b)
    cost=compute_cost(fwb,y)

    

    


    plt.scatter(X,y)
    plt.plot(X,fwb,color='red')
    plt.title(f"Cost = {cost[0]:.2f}")
    plot_path = "plots/output.png"
    plt.savefig(plot_path)
    plt.close()
    return plot_path


