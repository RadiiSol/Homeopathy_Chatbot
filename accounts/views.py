from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from . import models
from datetime import datetime
from django.contrib.auth.hashers import make_password, check_password


# HELPER FUNCTIONS


def getage(dob):
    todays_date = datetime.today()
    #dob = datetime.strptime(dob, "%Y-%m-%d")

    if dob.month > todays_date.month:
        return str(todays_date.year - dob.year - 1)
    elif dob.day > todays_date.day:
        return str(todays_date.year - dob.year - 1)
    else:
        return str(todays_date.year - dob.year)


def medical_historytoDB(medical_history_list):
    medical_history_dict = {
        "medical_history_asthma": False,
        "medical_history_infection": False,
        "medical_history_tuberculosis": False,
        "medical_history_thyroid": False,
        "medical_history_hypertension": False,
        "medical_history_diabetes": False
    }
    for item in medical_history_list:
        medical_history_dict[item] = True

    return medical_history_dict


def narcotics_historytoDB(narcotics_history_list):
    narcotics_history_dict = {
        "narcotics_history_smoking": False,
        "narcotics_history_alcohol": False,
        "narcotics_history_drugs": False
    }

    for item in narcotics_history_list:
        narcotics_history_dict[item] = True

    return narcotics_history_dict


# VIEWS


def go_home(request):
    return render(request, "home_links.html")

def login(request):
    if request.method == "POST":
        info = request.POST['info']
        password = request.POST['password']

        if '@' in info:
            email = info
            if User.objects.filter(email=email).exists():
                username = User.objects.filter(email=email)[0].username
            else:
                username = "not found"
        else:
            username = info

        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("")
            print("")
            print("Username: " + user.username)
            print("Password: " + user.password)
            print("")
            print("")
            auth.login(request, user)
            return redirect('go_home')
        else:
            return HttpResponse("Something went wrong!!!")

    return render(request, "index.html")


def signup(request):
    if request.method == "POST":

        first_name = request.POST['firstname']
        last_name = request.POST['lastname']

        if not User.objects.filter(username=request.POST['username']).exists():
            username = request.POST['username']
        else:
            return HttpResponse("Username already taken!!!")

        if not User.objects.filter(email=request.POST['email']):
            email = request.POST['email']
        else:
            return HttpResponse("Email already registered!!!")

        if request.POST['password'] == request.POST['confirm_password']:
            password = make_password(request.POST['password'], "pbkdf2_sha256")
        else:
            return HttpResponse("Passwords do not match!!!")

        date_of_birth = request.POST['date_of_birth']
        sex = request.POST.getlist('sex')[0]
        height = request.POST['height']
        weight = request.POST['weight']
        marital_status = request.POST.getlist('marital_status')[0]
        if marital_status == "married":
            marital_status = True
        else:
            marital_status = False
        occupation = request.POST['occupation']
        contact_number = request.POST['contact_number']
        address = request.POST['address']

        # for Medical_Narcotics_Sports_History
        medical_history_list = request.POST.getlist("medical_history")
        medical_history_DBready = medical_historytoDB(medical_history_list)

        narcotics_history_list = request.POST.getlist("narcotics_history")
        narcotics_history_DBready = narcotics_historytoDB(
            narcotics_history_list)

        sports_bool = request.POST.getlist("sports_bool")[0]
        if sports_bool == "yes":
            sports_bool = True
            sports_name = request.POST['sports_name']
        else:
            sports_bool = False
            sports_name = "NA"

        new_user = User.objects.create(
            username=username, first_name=first_name, last_name=last_name, email=email, password=password)

        new_user.save()

        patient_detail = models.Patient_Medical_History.objects.create(
            user=new_user, height=height, weight=weight, date_of_birth=date_of_birth, marital_status=marital_status, sex=sex, occupation=occupation, address=address, contact_number=contact_number)
        patient_detail.save()

        patient_history_detail = models.Medical_Narcotics_Sports_History.objects.create(user=new_user, medical_history_asthma=medical_history_DBready["medical_history_asthma"],  medical_history_infection=medical_history_DBready["medical_history_infection"], medical_history_tuberculosis=medical_history_DBready[
                                                                                        "medical_history_tuberculosis"], medical_history_thyroid=medical_history_DBready["medical_history_thyroid"], medical_history_hypertension=medical_history_DBready["medical_history_hypertension"], medical_history_diabetes=medical_history_DBready["medical_history_diabetes"], narcotics_history_smoking=narcotics_history_DBready["narcotics_history_smoking"],  narcotics_history_drugs=narcotics_history_DBready["narcotics_history_drugs"],  narcotics_history_alcohol=narcotics_history_DBready["narcotics_history_alcohol"], sports_bool=sports_bool, sports_name=sports_name)
        patient_history_detail.save()

        return redirect('go_home')
    else:
        return render(request, "signup.html")

def doctor_signup(request):
    if request.method == "POST":
        
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']

        if not User.objects.filter(username=request.POST['username']).exists():
            username = request.POST['username']
        else:
            return HttpResponse("Username already taken!!!")

        if not User.objects.filter(email=request.POST['email']):
            email = request.POST['email']
        else:
            return HttpResponse("Email already registered!!!")

        if request.POST['password'] == request.POST['confirm_password']:
            password = make_password(request.POST['password'], "pbkdf2_sha256")
        else:
            return HttpResponse("Passwords do not match!!!")

        specialization = request.POST['specialization']
        qualification = request.POST['qualification']
        hospital_name = request.POST['hospital_name']

        new_user = models.User.objects.create(
            username=username, first_name=first_name, last_name=last_name, email=email, password=password)
        new_user.save()

        doctor_profile = models.Doctor_Profile.objects.create(user=new_user, specialization=specialization, Qualification=qualification, hospitalname=hospital_name)
        doctor_profile.save()

        
        return redirect("go_home")
    return render(request, "doctor_signup.html")

def showDoctorProfile(request):
    if request.method == "POST":
        username = request.POST["username"]
        if models.User.objects.filter(username=username):
            user_details = models.User.objects.get(username=username)
            alldetails = models.Doctor_Profile.objects.get(user=user_details)
        else:
            return HttpResponse("Username NOT FOUND")

        return render(request, "doctor_details.html", {"alldetails": alldetails})
    return render(request, "getDoctorProfile.html")
    


def showPatientProfile(request):
    if request.method == "POST":
        alldetails = {
            "username": "",
            "name": "",
            "age": "",
            "sex": "",
            "height": "",
            "weight": "",
            "occupation": "",
            "address": "",
            "marital_status": "",
            "medical_history": "",
            "habits": "",
            "sports_played": "",
            "email": "",
            "contact": ""
        }
        userobjects = User.objects.filter(username=request.POST['username'])

        if len(userobjects) != 0:
            patient = userobjects[0]
            alldetails["username"] = patient.username
            alldetails["name"] = str(
                patient.first_name + " " + patient.last_name)
            alldetails["email"] = patient.email

            # Getting the full Patient Profile
            patientdetails = models.Patient_Medical_History.objects.get(
                user=patient)
            alldetails["age"] = getage(patientdetails.date_of_birth)
            alldetails["sex"] = patientdetails.sex
            alldetails["height"] = patientdetails.height
            alldetails["weight"] = patientdetails.weight
            alldetails["occupation"] = patientdetails.occupation
            alldetails["address"] = patientdetails.address
            alldetails["contact"] = patientdetails.contact_number
            if patientdetails.marital_status:
                alldetails["marital_status"] = "Married"
            else:
                alldetails["marital_status"] = "Unmarried"

            booleandetails = models.Medical_Narcotics_Sports_History.objects.get(
                user=patient)

            # Medical History
            if booleandetails.medical_history_asthma:
                alldetails["medical_history"] += "Asthma "
            if booleandetails.medical_history_infection:
                alldetails["medical_history"] += "Infection "
            if booleandetails.medical_history_tuberculosis:
                alldetails["medical_history"] += "Tuberculosis "
            if booleandetails.medical_history_thyroid:
                alldetails["medical_history"] += "Thyroid "
            if booleandetails.medical_history_hypertension:
                alldetails["medical_history"] += "Hypertension "
            if booleandetails.medical_history_diabetes:
                alldetails["medical_history"] += "Diabetes "

            if alldetails["medical_history"] == "":
                alldetails["medical_history"] = "None"

            # Habits
            if booleandetails.narcotics_history_smoking:
                alldetails["habits"] += "Smoking "
            if booleandetails.narcotics_history_drugs:
                alldetails["habits"] += "Drugs "
            if booleandetails.narcotics_history_alcohol:
                alldetails["habits"] += "Alcohol "

            if alldetails["habits"] == "":
                alldetails["habits"] = "None"

            # Sports
            alldetails["sports_played"] = booleandetails.sports_name

        else:
            return HttpResponse("Username not registered.")
        return render(request, "details.html", {"alldetails": alldetails})
    else:
        return render(request, "getPatientProfile.html")


def signout(request):
    logout(request)
    return redirect('go_home')
