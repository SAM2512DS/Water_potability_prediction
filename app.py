from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import joblib as jb


app = Flask(__name__)


@app.route('/',methods=['GET'])
def home():  
    return render_template('water.html')

@app.route('/pred', methods=['POST'] )
def prediction():
    if request.method == 'POST':
        ph =(request.form["ph"])
        Hardness =(request.form["Hardness"])
        Solids =(request.form["Solids"])
        Chloramines =(request.form["Chloramines"])
        Sulfate =(request.form["Sulfate"])
        Conductivity =(request.form["Conductivity"])
        Organic_carbon =(request.form["Organic_carbon"])
        Trihalomethanes =(request.form["Trihalomethanes"])
        Turbidity =(request.form["Turbidity"])
        model=jb.load("wtr_predict.pkl")
        input_values=[ph, Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity]
        prediction=model.predict([input_values])
        
    return render_template('result.html',data=prediction)

if __name__=="__main__":
    app.run()