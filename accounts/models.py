from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class Patient_Medical_History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    marital_status = models.BooleanField()
    date_of_birth = models.DateField()
    age = models.IntegerField()
    sex = models.CharField(max_length=1)
    occupation = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=10)
    height = models.CharField(max_length=5)
    weight = models.CharField(max_length=3)

    def __str__(self):
        return str(self.user)

class Medical_Narcotics_Sports_History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    medical_history_asthama = models.BooleanField(default=False)
    medical_history_infection = models.BooleanField(default=False)
    medical_history_tuberculosis = models.BooleanField(default=False)
    medical_history_thyroid = models.BooleanField(default=False)
    medical_history_hypertension = models.BooleanField(default=False)
    medical_history_diabetes = models.BooleanField(default=False)
    narcotics_history_smoking = models.BooleanField(default=False)
    narcotics_history_drugs = models.BooleanField(default=False)
    narcotics_history_alcohol = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)