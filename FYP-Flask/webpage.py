# Importing required functions 
from flask import Flask, render_template, request
from flask import url_for
import pandas as pd
import pickle


# Flask constructor 
app = Flask(__name__)
 
loaded_model = pickle.load(open("model.pkl", "rb")) 
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route('/')
def home():
    return render_template('prediction.html')

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        # All features 
        age = float(request.form['age'])
        sex = request.form['sex']
        ascites = request.form['ascites']
        hepatomegaly = request.form['hepatomegaly']
        spiders = request.form['spiders']
        edema = request.form['edema']
        bilirubin = float(request.form['bilirubin'])
        cholesterol = float(request.form['cholesterol'])
        albumin = float(request.form['albumin'])
        copper = float(request.form['copper'])
        alkphos = float(request.form['alk_phos'])
        sgot = float(request.form['sgot'])
        tryglicerides = float(request.form['tryglicerides'])
        platelets = float(request.form['platelets'])
        prothrombin = float(request.form['prothrombin'])
        
        # Encoding (Categorical)
        sex_encoded = 1 if sex == 'male' else 0
        hepatomegaly_encoded = 1 if hepatomegaly == 'yes' else 0
        ascites_encoded = 1 if ascites == 'yes' else 0  
        spiders_encoded = 1 if spiders == 'yes' else 0  
        if edema == 'y':
            edema_encoded = 2
        elif edema == "s":
            edema_encoded = 1
        else:
            edema_encoded = 0

        # Make prediction
        input_data = [[age, sex_encoded, ascites_encoded, hepatomegaly_encoded,spiders_encoded, 
                       edema_encoded, bilirubin, cholesterol, albumin, copper, alkphos, sgot, 
                       tryglicerides, platelets, prothrombin
                       ]]
        
        input_data_scaled = scaler.transform(input_data)

        # Take only the data required for the model
        prediction = loaded_model.predict(input_data_scaled[:, [10, 14, 2, 1, 0, 9, 3]] )
        prediction_proba = loaded_model.predict_proba(input_data_scaled[:, [10, 14, 2, 1, 0, 9, 3]])

        confidence_score = max(prediction_proba[0]) * 100  

        if prediction == 0:
            prediction = "Non-Cirrhotic Stage"
        elif prediction == 1:
            prediction = "Cirrhotic stage"

        return render_template('prediction_result.html', prediction = prediction, confidence_score = confidence_score)
    
    # Display prediction result in another page
    return render_template('prediction.html')
    
@app.route('/prediction_result')
def prediction_result():
    return render_template('prediction_result.html')

# Main Driver Function 
if __name__ == '__main__':
    app.run(debug=True)