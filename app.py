import pickle
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

# loading model
model = pickle.load(open("RandomizedCV_log_reg_model.pkl", 'rb'))
b_model=model.best_estimator_

# '/' means home route
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/model')
def model():
    return render_template('model.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            age = float(request.form['age'])
            sex = float(request.form['sex'])
            cp = float(request.form['cp'])
            trestbps = float(request.form['trestbps'])
            chol = float(request.form['chol'])
            fbs = float(request.form['fbs'])
            restecg = float(request.form['restecg'])
            thalach = float(request.form['thalach'])
            exang = float(request.form['exang'])
            oldpeak = float(request.form['oldpeak'])
            slope = float(request.form['slope'])
            ca = float(request.form['ca'])
            thal = float(request.form['thal'])

            features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
            prediction = b_model.predict(features)
            prediction_text = "Heart Disease" if prediction[0] == 1 else "NO Heart Disease"
            return render_template('result.html', prediction=prediction_text)

        except ValueError:
            return render_template('model.html', error="invalid Input please enter correct number.")


if __name__ == '__main__':
    app.run()
