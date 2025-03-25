from flask import Flask,request, jsonify, render_template
import pickle as pk
import numpy as np
import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder


application = Flask(__name__) # create an instance of the Flask class
app = application

## importing the model, encoder and column transformer
gaussian_model = pk.load(open(r'D:\gaurav\KRIS NAIK STATEMENTS\NAIVE BAYES ALGORITHM\models\gaussian_tips.pkl','rb'))
label_encoder_1 = pk.load(open(r'D:\gaurav\KRIS NAIK STATEMENTS\NAIVE BAYES ALGORITHM\models\le1.pkl','rb'))
label_encoder_2 = pk.load(open(r'D:\gaurav\KRIS NAIK STATEMENTS\NAIVE BAYES ALGORITHM\models\le2.pkl','rb'))
label_encoder_3 = pk.load(open(r'D:\gaurav\KRIS NAIK STATEMENTS\NAIVE BAYES ALGORITHM\models\le3.pkl','rb'))
column_transformer = pk.load(open(r'D:\gaurav\KRIS NAIK STATEMENTS\NAIVE BAYES ALGORITHM\models\Column_transformer.pkl','rb'))

## The templates folder should be in the same directory as the application.py file

@app.route('/')
def index():
    print("Current Working Directory:", os.getcwd())
    print("Templates Directory Contents:", os.listdir('templates'))
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'POST':
        bill_amount=float(request.form.get('bill_amount'))
        tip_amount = float(request.form.get('tip_amount'))
        gender = request.form.get('gender')
        smoking_habbit = request.form.get('smoking_habbit')
        day = request.form.get('day')
        size = float(request.form.get('size'))


        gender = label_encoder_1.transform([gender])
        smoking_habbit = label_encoder_2.transform([smoking_habbit])
        
        test = [[bill_amount,tip_amount,gender[0],smoking_habbit[0],day,size]]
        test_final = column_transformer.transform(test)

        prediction = gaussian_model.predict(test_final)
        decode = label_encoder_3.inverse_transform(prediction)

        

        return render_template('home.html',results=decode[0])
    else:
        return render_template('home.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0") # run the application