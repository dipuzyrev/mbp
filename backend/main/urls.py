from django.urls import path
from .views import *


urlpatterns = [
    path('update_height_weight/', UpdateHeightAndWeightAPI.as_view(), name='height_weight'),
    path('update_tonometer/', UpdateTonometerAPI.as_view(), name='update_tonometer'),
    path('patient_profile/', PatientProfileAPI.as_view(), name='patient_profile'),
    path('add_treatment/', AddTreatmentAPI.as_view(), name='add_treatment'),
    path('add_note/', AddNoteAPI.as_view(), name='add_note'),
    path('add_measurement/', AddMeasurementsAPI.as_view(), name='add_measurement'),
    path('patient_by_snils/', PatientBySnilsAPI.as_view(), name='patient_by_snils'),
]
