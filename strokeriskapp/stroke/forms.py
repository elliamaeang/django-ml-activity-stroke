from stroke.models import Stroke
from django import forms

class StrokeForm(forms.ModelForm):
    class Meta:
        model = Stroke
        fields = '__all__'

        labels = {
            "gender": "Gender",
            "age": "Age",
            "hypertension": "Hypertension",
            "heart_disease": "Heart Disease",
            "avg_glucose_level": "Average Glucose Level",
            "bmi": "Body Mass Index (BMI)",
            "smoking_status": "Smoking Status",
        }

        widgets = {
            "gender": forms.Select(attrs={'class': 'form-control', 'id': 'gender'}),
            "age": forms.NumberInput(attrs={'class': 'form-control', 'id': 'age'}),
            "hypertension": forms.RadioSelect(attrs={'class': 'form-control', 'id': 'hypertension'}),
            "heart_disease": forms.RadioSelect(attrs={'class': 'form-control', 'id': 'petal_width'}),
            "avg_glucose_level": forms.NumberInput(attrs={'class': 'form-control', 'id': 'avg_glucose_level'}),
            "bmi": forms.NumberInput(attrs={'class': 'form-control', 'id': 'bmi'}),
            "smoking_status": forms.Select(attrs={'class': 'form-control', 'id':'smoking_status'}),
        }