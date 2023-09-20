from django.apps import AppConfig
from django.conf import settings
import joblib
import os

class StrokeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stroke'

    # Load model
    model = joblib.load(os.path.join(settings.BASE_DIR, "models/stroke_clf.joblib"))
    calibrated_clf = joblib.load(os.path.join(settings.BASE_DIR, "models/stroke_calibrated_clf.joblib"))

    # Load scaler
    scaler = joblib.load(os.path.join(settings.BASE_DIR, "models/scaler.save"))