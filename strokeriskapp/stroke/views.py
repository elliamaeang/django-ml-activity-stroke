from django.template import loader
from django.http import HttpResponse
from stroke.forms import StrokeForm
from stroke.models import Stroke
from stroke.apps import StrokeConfig

import numpy as np 

# Create your views here.
def home(request):
    '''
        This is the landing page of the website.
    '''

    template = loader.get_template("stroke/home.html")
    form = StrokeForm()
    context = {'form': form}

    return HttpResponse(template.render(context, request))

def predict(request):
    '''
        Retrieves input from form fields and passes inputs
        to the model for prediction.
    '''

    # targets = results / predictions
    targets = ['No Risk', 'At Risk']

    if request.method == 'POST':
        # pass form results
        form = StrokeForm(request.POST)

        # if form contains valid inputs
        if form.is_valid(): 

            # get the input values
            gender = int(form.cleaned_data.get('gender'))
            age = float(form.cleaned_data.get('age'))
            hypertension = int(form.cleaned_data.get('hypertension'))
            heart_disease = int(form.cleaned_data.get('heart_disease'))
            avg_glucose_level = float(form.cleaned_data.get('avg_glucose_level'))
            bmi = float(form.cleaned_data.get('bmi'))
            smoking_status = int(form.cleaned_data.get('smoking_status'))

            # send input values into a single array
            features = np.array([gender, age, hypertension, heart_disease, avg_glucose_level, bmi, smoking_status])
            print("Before scaling: ", features)

            # scale
            features = StrokeConfig.scaler.transform(features.reshape(1, -1))[0]
            print("After scaling: ", features)

            # get classification
            # StrokeConfig used to call the model function, since it was loaded in apps.py
            prediction = StrokeConfig.model.predict(features.reshape(1, -1))[0]
            print("Prediction: ", prediction, targets[prediction])
            prediction = targets[prediction]

            # get prediction probabilities
            prediction_probas = StrokeConfig.calibrated_clf.predict_proba(features.reshape(1, -1))[0]
            print("Probabilities: ", prediction_probas)
            prediction_probas = [f"{prob*100:.2f}%" for prob in prediction_probas] # convert to string with percentage sign and 2 decimal values

            # get classes
            prediction_proba_classes = zip(targets, prediction_probas) # zip() used to combine the two parameters into one list of tuples (target to prediction probabilities)
            prediction_proba_classes = sorted(prediction_proba_classes, key=lambda x: x[1], reverse=True) # sort from highest to lowest
                    
    template = loader.get_template('stroke/home.html')
    context = {
        'form': form,
        'predictions': prediction_proba_classes
    }

    return HttpResponse(template.render(context, request))