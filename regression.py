
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def run_regression(file_path):

    df=pd.read_csv(file_path)

    X = df.iloc[:,0].values.reshape(-1,1)
    y = df.iloc[:,1].values

    model = LinearRegression()
    model.fit(X,y)

    y_pred = model.predict(X)


    plt.scatter(X,y)
    plt.plot(X,y_pred,color='red')
    plot_path = "plots/output.png"
    plt.savefig(plot_path)
    plt.close()
    return plot_path


