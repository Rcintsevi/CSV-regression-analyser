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

def compute_gradient(X,y,w,b):
    m=X.shape[0]
    dJ_dw=0
    dJ_db=0

    for i in range(m):
        dJ_dw+=(w*X[i]+b-y[i])*X[i]
        dJ_db+=(w*X[i]+b-y[i])

    dJ_dw=dJ_dw/m
    dJ_db=dJ_db/m

    
    return dJ_dw,dJ_db

def gradient_descent(X,y,w_in,b_in,alpha,iterations,compute_cost,compute_gradient):

    p_history=[]
    j_history=[]
    w=w_in
    b=b_in

    j_history.append(compute_cost(compute_fwb(X,w,b),y))
    p_history.append([w,b])



    for i in range(iterations):
        dj_dw,dj_db=compute_gradient(X,y,w,b)

        w-=(alpha*dj_dw)
        b-=(alpha*dj_db)

        j_history.append(compute_cost(compute_fwb(X,w,b),y))
        p_history.append([w,b])
    return w,b,j_history,p_history

def r2_score(y,y_pred):
    mean=np.mean(y)
    ss_res=np.sum((y-y_pred)**2)
    ss_tot=np.sum((y-mean)**2)
    return 1-(ss_res/ss_tot)



def run_regression(file_path,weight,bias,alpha,iterations):

    df=pd.read_csv(file_path)
    preview = df.head().to_dict(orient="records")
    columns = list(df.columns)

    X = df.iloc[:,0].values
    y = df.iloc[:,1].values

    w=weight
    b=bias

    w_final,b_final,j_history,p_history=gradient_descent(X,y,w,b,alpha,iterations,compute_cost,compute_gradient)

    fwb=compute_fwb(X,w_final,b_final)
    cost=compute_cost(fwb,y)
    r2=r2_score(y,fwb)

    

    # Regression plot
    plt.figure(figsize=(8,6))
    plt.scatter(X,y)
    idx = np.argsort(X)
    plt.plot(X[idx], compute_fwb(X[idx],w_final,b_final),color='red')
    plt.title(f"Final Cost = {j_history[-1]:.2f}")
    regression_path = "plots/regression.png"
    plt.savefig(regression_path)
    plt.close()


    # Cost vs iterations
    plt.figure(figsize=(8,6))
    plt.plot(j_history)
    plt.title("Cost vs Iterations")
    plt.xlabel("Iterations")
    plt.ylabel("Cost")
    cost_path = "plots/cost.png"
    plt.savefig(cost_path)
    plt.close()

    return {
        "regression_plot": regression_path,
        "cost_plot": cost_path,
        "w":w_final,
        "b":b_final,
        "cost":j_history[-1],
        "r2":r2,
        "preview": preview,
        "columns": columns
    }


