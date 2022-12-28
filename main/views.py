from django.shortcuts import render, redirect, HttpResponse
from .models import Patient_Case_Sheet
from django.contrib.auth.models import User
import json
import os

# getting the question data in variable "data"


with open('questions_data.json', 'r') as f:
    data = json.load(f)


# creating and redo-ing already existing casesheet
def createcasesheet(request):

    if request.method == "POST":
        if 'newCase' in request.POST:
            casesheetname = request.POST['casesheetname']

            if Patient_Case_Sheet.objects.filter(user=request.user, case_sheet_name=casesheetname).exists():
                return render(request, "newcasesheet.html", {"casesheetname": casesheetname, "error_message": "Casesheet already exists! Would you like to redo this casesheet again?"})

            newcasesheet = Patient_Case_Sheet.objects.create(
                user=request.user, case_sheet_name=casesheetname)
            newcasesheet.save()
            request.session['casesheetname'] = casesheetname
            return redirect('question1')

        if 'updateCase' in request.POST:
            request.session['casesheetname'] = request.POST['casesheetnameconfirm']
            return redirect('question1')

    return render(request, "newcasesheet.html")


# for major-location
def question1(request):
    if request.method == "GET":
        returndict = {
            "question":  "Q1. What is the location of your complaint?",
            "options": ["Head", "Upper Extremities", "Lower Extremities"],
            "casesheetname": request.session.get("casesheetname"),
            "question_name": "question1"
        }
        return render(request, "question_type1.html", {"returndict": returndict})

    else:
        optionselected = request.POST['selectedoption']
        casesheetname = request.POST['currentscasesheetname']
        currentuser = request.user
        mappedcasesheets = Patient_Case_Sheet.objects.filter(
            user=currentuser, case_sheet_name=casesheetname)

        if mappedcasesheets and len(mappedcasesheets) == 1:
            mappedcasesheets.update(majorlocation=optionselected)
        else:
            return HttpResponse("Something went wrong!!!")

        return redirect("question2")


# for minor-location
def question2(request):
    if request.method == 'GET':

        currentcasesheet = Patient_Case_Sheet.objects.filter(
            user=request.user, case_sheet_name=request.session.get("casesheetname"))

        returndict = {
            "question":  "Q2. What is the sub-location of your complaint?",
            "options": data["Q2"][currentcasesheet[0].majorlocation],
            "casesheetname": request.session.get("casesheetname"),
            "question_name": "question2"
        }
        return render(request, "question_type1.html", {"returndict": returndict})

    else:
        optionselected = request.POST['selectedoption']
        casesheetname = request.POST['currentscasesheetname']
        currentuser = request.user
        mappedcasesheets = Patient_Case_Sheet.objects.filter(
            user=currentuser, case_sheet_name=casesheetname)

        if mappedcasesheets and len(mappedcasesheets) == 1:
            mappedcasesheets.update(minorlocation=optionselected)
        else:
            return HttpResponse("Something went wrong!!!")

        return redirect("question3")


# for problem
def question3(request):
    if request.method == 'GET':

        currentcasesheet = Patient_Case_Sheet.objects.filter(
            user=request.user, case_sheet_name=request.session.get("casesheetname"))

        returndict = {
            "question":  "Q3. What is your complaint?",
            "options": data["Q3"][currentcasesheet[0].minorlocation],
            "casesheetname": request.session.get("casesheetname"),
            "question_name": "question3"
        }
        return render(request, "question_type1.html", {"returndict": returndict})

    else:
        optionselected = request.POST['selectedoption']
        casesheetname = request.POST['currentscasesheetname']
        currentuser = request.user
        mappedcasesheets = Patient_Case_Sheet.objects.filter(
            user=currentuser, case_sheet_name=casesheetname)

        if mappedcasesheets and len(mappedcasesheets) == 1:
            mappedcasesheets.update(problem=optionselected)
        else:
            return HttpResponse("Something went wrong!!!")

        return redirect("question4")


def question4(request):
    if request.method == 'GET':

        currentcasesheet = Patient_Case_Sheet.objects.filter(
            user=request.user, case_sheet_name=request.session.get("casesheetname"))

        returndict = {
            "question": data["Q4"][currentcasesheet[0].minorlocation][currentcasesheet[0].problem]["question"],
            "options": data["Q4"][currentcasesheet[0].minorlocation][currentcasesheet[0].problem]["options"],
            "casesheetname": request.session.get("casesheetname"),
            "question_name": "question4"
        }
        return render(request, "question_type1.html", {"returndict": returndict})
    else:
        optionselected = request.POST['selectedoption']
        casesheetname = request.POST['currentscasesheetname']
        currentuser = request.user
        mappedcasesheets = Patient_Case_Sheet.objects.filter(
            user=currentuser, case_sheet_name=casesheetname)

        if mappedcasesheets and len(mappedcasesheets) == 1:
            mappedcasesheets.update(q4=optionselected)
        else:
            return HttpResponse("Something went wrong!!!")

        return redirect("question5")


def question5(request):
    if request.method == 'GET':

        currentcasesheet = Patient_Case_Sheet.objects.filter(
            user=request.user, case_sheet_name=request.session.get("casesheetname"))

        returndict = {
            "question": data["Q5"][currentcasesheet[0].minorlocation][currentcasesheet[0].problem]["question"],
            "options": data["Q5"][currentcasesheet[0].minorlocation][currentcasesheet[0].problem]["options"],
            "casesheetname": request.session.get("casesheetname"),
            "question_name": "question5"
        }
        return render(request, "question_type1.html", {"returndict": returndict})
    else:
        optionselected = request.POST['selectedoption']
        casesheetname = request.POST['currentscasesheetname']
        currentuser = request.user
        mappedcasesheets = Patient_Case_Sheet.objects.filter(
            user=currentuser, case_sheet_name=casesheetname)

        if mappedcasesheets and len(mappedcasesheets) == 1:
            mappedcasesheets.update(q5=optionselected)
        else:
            return HttpResponse("Something went wrong!!!")

        return redirect("question6")


def question6(request):
    if request.method == 'GET':

        currentcasesheet = Patient_Case_Sheet.objects.filter(
            user=request.user, case_sheet_name=request.session.get("casesheetname"))

        returndict = {
            "question": data["Q6"][currentcasesheet[0].minorlocation][currentcasesheet[0].problem]["question"],
            "options": data["Q6"][currentcasesheet[0].minorlocation][currentcasesheet[0].problem]["options"],
            "casesheetname": request.session.get("casesheetname"),
            "question_name": "question6"
        }
        return render(request, "question_type1.html", {"returndict": returndict})
    else:
        optionselected = request.POST['selectedoption']
        casesheetname = request.POST['currentscasesheetname']
        currentuser = request.user
        mappedcasesheets = Patient_Case_Sheet.objects.filter(
            user=currentuser, case_sheet_name=casesheetname)

        if mappedcasesheets and len(mappedcasesheets) == 1:
            mappedcasesheets.update(q6=optionselected)
        else:
            return HttpResponse("Something went wrong!!!")

        return redirect("question6")
