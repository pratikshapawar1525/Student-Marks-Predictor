from flask import Flask, render_template,request
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

from sklearn.impute   import SimpleImputer
from sklearn.model_selection  import train_test_split
from sklearn.linear_model    import LinearRegression


df = pd.read_csv("student_info.csv")

si = SimpleImputer(missing_values=np.nan,  strategy="median")
df['hours'] = si.fit_transform(  df[[  "hours"]])

x = df.iloc[ : ,  0:1]  # 2D
y = df.iloc[ : ,  -1]   # 1D


xtrain, xtest,    ytrain, ytest      =  train_test_split( x, y,     test_size=0.2,  random_state=42)

# step 2 : make an object of a model.
linreg =   LinearRegression()


# step 3 : train the model.
linreg.fit(xtrain, ytrain)


# step 4 : predict using model.
yp = linreg.predict(xtest)


app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html")


    return render_template("index.html",value = pr)
@app.route("/predict", methods=["POST","GET"])
def predictor():
    hr = float(request.form.get("hours"))

    pre = linreg.predict([[hr]])

    return render_template("index.html", value=pre[0])



if __name__  ==  "__main__":
    app.run(debug=True)