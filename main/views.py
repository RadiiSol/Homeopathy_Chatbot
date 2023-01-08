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

        return redirect("question7")


def question7(request):
    if request.method == 'GET':

        currentcasesheet = Patient_Case_Sheet.objects.filter(
            user=request.user, case_sheet_name=request.session.get("casesheetname"))

        returndict = {
            "question": data["Q7"][currentcasesheet[0].minorlocation][currentcasesheet[0].problem]["question"],
            "options": data["Q7"][currentcasesheet[0].minorlocation][currentcasesheet[0].problem]["options"],
            "casesheetname": request.session.get("casesheetname"),
            "question_name": "question7"
        }
        return render(request, "question_type1.html", {"returndict": returndict})
    else:
        optionselected = request.POST['selectedoption']
        casesheetname = request.POST['currentscasesheetname']
        currentuser = request.user
        mappedcasesheets = Patient_Case_Sheet.objects.filter(
            user=currentuser, case_sheet_name=casesheetname)

        if mappedcasesheets and len(mappedcasesheets) == 1:
            mappedcasesheets.update(q7=optionselected)
        else:
            return HttpResponse("Something went wrong!!!")

        return redirect("question8")


def question8(request):
    if request.method == 'GET':

        currentcasesheet = Patient_Case_Sheet.objects.filter(
            user=request.user, case_sheet_name=request.session.get("casesheetname"))

        returndict = {
            "question": data["Q8"][currentcasesheet[0].minorlocation][currentcasesheet[0].problem]["question"],
            "options": data["Q8"][currentcasesheet[0].minorlocation][currentcasesheet[0].problem]["options"],
            "casesheetname": request.session.get("casesheetname"),
            "question_name": "question8"
        }
        return render(request, "question_type1.html", {"returndict": returndict})
    else:
        optionselected = request.POST['selectedoption']
        casesheetname = request.POST['currentscasesheetname']
        currentuser = request.user
        mappedcasesheets = Patient_Case_Sheet.objects.filter(
            user=currentuser, case_sheet_name=casesheetname)

        if mappedcasesheets and len(mappedcasesheets) == 1:
            mappedcasesheets.update(q8=optionselected)
        else:
            return HttpResponse("Something went wrong!!!")

        return redirect("question9")


def question9(request):
    if request.method == 'GET':

        currentcasesheet = Patient_Case_Sheet.objects.filter(
            user=request.user, case_sheet_name=request.session.get("casesheetname"))

        returndict = {
            "question": data["Q9"][currentcasesheet[0].minorlocation][currentcasesheet[0].problem]["question"],
            "options": data["Q9"][currentcasesheet[0].minorlocation][currentcasesheet[0].problem]["options"],
            "casesheetname": request.session.get("casesheetname"),
            "question_name": "question9"
        }
        return render(request, "question_type1.html", {"returndict": returndict})
    else:
        optionselected = request.POST['selectedoption']
        casesheetname = request.POST['currentscasesheetname']
        currentuser = request.user
        mappedcasesheets = Patient_Case_Sheet.objects.filter(
            user=currentuser, case_sheet_name=casesheetname)

        if mappedcasesheets and len(mappedcasesheets) == 1:
            mappedcasesheets.update(q9=optionselected)
        else:
            return HttpResponse("Something went wrong!!!")

        return redirect("question10")


def question10(request):
    if request.method == 'GET':

        currentcasesheet = Patient_Case_Sheet.objects.filter(
            user=request.user, case_sheet_name=request.session.get("casesheetname"))

        returndict = {
            "question": data["Q10"][currentcasesheet[0].minorlocation][currentcasesheet[0].problem]["question"],
            "options": data["Q10"][currentcasesheet[0].minorlocation][currentcasesheet[0].problem]["options"],
            "casesheetname": request.session.get("casesheetname"),
            "question_name": "question10"
        }
        return render(request, "question_type1.html", {"returndict": returndict})
    else:
        optionselected = request.POST['selectedoption']
        casesheetname = request.POST['currentscasesheetname']
        currentuser = request.user
        mappedcasesheets = Patient_Case_Sheet.objects.filter(
            user=currentuser, case_sheet_name=casesheetname)

        if mappedcasesheets and len(mappedcasesheets) == 1:
            mappedcasesheets.update(q10=optionselected)
        else:
            return HttpResponse("Something went wrong!!!")

        return redirect("question11")


def question11(request):
    if request.method == 'GET':

        currentcasesheet = Patient_Case_Sheet.objects.filter(
            user=request.user, case_sheet_name=request.session.get("casesheetname"))

        returndict = {
            "question": data["Q11"][currentcasesheet[0].minorlocation][currentcasesheet[0].problem]["question"],
            "options": data["Q11"][currentcasesheet[0].minorlocation][currentcasesheet[0].problem]["options"],
            "casesheetname": request.session.get("casesheetname"),
            "question_name": "question11"
        }
        return render(request, "question_type1.html", {"returndict": returndict})
    else:
        optionselected = request.POST['selectedoption']
        casesheetname = request.POST['currentscasesheetname']
        currentuser = request.user
        mappedcasesheets = Patient_Case_Sheet.objects.filter(
            user=currentuser, case_sheet_name=casesheetname)

        if mappedcasesheets and len(mappedcasesheets) == 1:
            mappedcasesheets.update(q11=optionselected)
        else:
            return HttpResponse("Something went wrong!!!")

        return redirect("question12")


def question12(request):
    if request.method == 'GET':

        currentcasesheet = Patient_Case_Sheet.objects.filter(
            user=request.user, case_sheet_name=request.session.get("casesheetname"))

        returndict = {
            "question": data["Q12"][currentcasesheet[0].minorlocation][currentcasesheet[0].problem]["question"],
            "options": data["Q12"][currentcasesheet[0].minorlocation][currentcasesheet[0].problem]["options"],
            "casesheetname": request.session.get("casesheetname"),
            "question_name": "question12"
        }
        return render(request, "question_type1.html", {"returndict": returndict})
    else:
        optionselected = request.POST['selectedoption']
        casesheetname = request.POST['currentscasesheetname']
        currentuser = request.user
        mappedcasesheets = Patient_Case_Sheet.objects.filter(
            user=currentuser, case_sheet_name=casesheetname)

        # checks if we got multiple casesheets of same name
        if mappedcasesheets and len(mappedcasesheets) == 1:
            mappedcasesheets.update(q12=optionselected)
        else:
            return HttpResponse("Something went wrong!!!")

        return redirect("question13")


def question13(request):
    if request.method == 'GET':

        currentcasesheet = Patient_Case_Sheet.objects.filter(
            user=request.user, case_sheet_name=request.session.get("casesheetname"))

        optionheadings = []
        options = []

        # for filling option-headings
        for item in data["Q13"][currentcasesheet[0].minorlocation][currentcasesheet[0].problem]["options"]:
            optionheadings.append(item)

        # for the filling the options under each option heading
        for item in optionheadings:
            options.append(data["Q13"][currentcasesheet[0].minorlocation]
                           [currentcasesheet[0].problem]["options"][item])

        returndict = {
            "question": data["Q13"][currentcasesheet[0].minorlocation][currentcasesheet[0].problem]["question"],
            "headingsWithOptions": zip(optionheadings, options),
            "numberOfHeadings": len(options),
            "casesheetname": request.session.get("casesheetname"),
            "question_name": "question13"
        }

        return render(request, "question_type2.html", {"returndict": returndict})
    else:
        optionselected = request.POST.getlist('selectedoption')
        casesheetname = request.POST['currentscasesheetname']
        currentuser = request.user
        mappedcasesheets = Patient_Case_Sheet.objects.filter(
            user=currentuser, case_sheet_name=casesheetname)

        finalString = optionselected[0]  # stores what to put in DB

        # putting all array values into one string
        for item in range(1, len(optionselected)):
            finalString += "$"
            finalString += optionselected[item]

        # checks if we got multiple casesheets of same name
        if mappedcasesheets and len(mappedcasesheets) == 1:
            mappedcasesheets.update(q13=finalString)
        else:
            return HttpResponse("Something went wrong!!!")

        return redirect("question14")


def question14(request):
    if request.method == 'GET':

        currentcasesheet = Patient_Case_Sheet.objects.filter(
            user=request.user, case_sheet_name=request.session.get("casesheetname"))

        optionheadings = []
        options = []

        # for filling option-headings
        for item in data["Q14"][currentcasesheet[0].minorlocation][currentcasesheet[0].problem]["options"]:
            optionheadings.append(item)

        # for the filling the options under each option heading
        for item in optionheadings:
            options.append(data["Q14"][currentcasesheet[0].minorlocation]
                           [currentcasesheet[0].problem]["options"][item])

        returndict = {
            "question": data["Q14"][currentcasesheet[0].minorlocation][currentcasesheet[0].problem]["question"],
            "headingsWithOptions": zip(optionheadings, options),
            "numberOfHeadings": len(options),
            "casesheetname": request.session.get("casesheetname"),
            "question_name": "question14"
        }

        return render(request, "question_type2.html", {"returndict": returndict})
    else:
        optionselected = request.POST.getlist('selectedoption')
        casesheetname = request.POST['currentscasesheetname']
        currentuser = request.user
        mappedcasesheets = Patient_Case_Sheet.objects.filter(
            user=currentuser, case_sheet_name=casesheetname)

        finalString = optionselected[0]  # stores what to put in DB

        # putting all array values into one string
        for item in range(1, len(optionselected)):
            finalString += "$"
            finalString += optionselected[item]

        # checks if we got multiple casesheets of same name
        if mappedcasesheets and len(mappedcasesheets) == 1:
            mappedcasesheets.update(q14=finalString)
        else:
            return HttpResponse("Something went wrong!!!")

        return redirect("question15")


def question15(request):
    if request.method == 'GET':

        currentcasesheet = Patient_Case_Sheet.objects.filter(
            user=request.user, case_sheet_name=request.session.get("casesheetname"))

        optionheadings = []
        options = []

        # for filling option-headings
        for item in data["Q15"][currentcasesheet[0].minorlocation][currentcasesheet[0].problem]["options"]:
            optionheadings.append(item)

        # for the filling the options under each option heading
        for item in optionheadings:
            options.append(data["Q15"][currentcasesheet[0].minorlocation]
                           [currentcasesheet[0].problem]["options"][item])

        returndict = {
            "question": data["Q15"][currentcasesheet[0].minorlocation][currentcasesheet[0].problem]["question"],
            "headingsWithOptions": zip(optionheadings, options),
            "numberOfHeadings": len(options),
            "casesheetname": request.session.get("casesheetname"),
            "question_name": "question15"
        }

        return render(request, "question_type2.html", {"returndict": returndict})
    else:
        optionselected = request.POST.getlist('selectedoption')
        casesheetname = request.POST['currentscasesheetname']
        currentuser = request.user
        mappedcasesheets = Patient_Case_Sheet.objects.filter(
            user=currentuser, case_sheet_name=casesheetname)

        finalString = optionselected[0]  # stores what to put in DB

        # putting all array values into one string
        for item in range(1, len(optionselected)):
            finalString += "$"
            finalString += optionselected[item]

        # checks if we got multiple casesheets of same name
        if mappedcasesheets and len(mappedcasesheets) == 1:
            mappedcasesheets.update(q15=finalString)
        else:
            return HttpResponse("Something went wrong!!!")

        return redirect("question16")


def question16(request):
    if request.method == 'GET':

        currentcasesheet = Patient_Case_Sheet.objects.filter(
            user=request.user, case_sheet_name=request.session.get("casesheetname"))

        returndict = {
            "question": data["Q16"][currentcasesheet[0].minorlocation][currentcasesheet[0].problem]["question"],
            "options": data["Q16"][currentcasesheet[0].minorlocation][currentcasesheet[0].problem]["options"],
            "casesheetname": request.session.get("casesheetname"),
            "question_name": "question16"
        }
        return render(request, "question_type1.html", {"returndict": returndict})
    else:
        optionselected = request.POST['selectedoption']
        casesheetname = request.POST['currentscasesheetname']
        currentuser = request.user
        mappedcasesheets = Patient_Case_Sheet.objects.filter(
            user=currentuser, case_sheet_name=casesheetname)

        # checks if we got multiple casesheets of same name
        if mappedcasesheets and len(mappedcasesheets) == 1:
            mappedcasesheets.update(q16=optionselected)
        else:
            return HttpResponse("Something went wrong!!!")

        return redirect("question17")


def question17(request):
    if request.method == 'GET':

        currentcasesheet = Patient_Case_Sheet.objects.filter(
            user=request.user, case_sheet_name=request.session.get("casesheetname"))

        returndict = {
            "question": data["Q17"][currentcasesheet[0].minorlocation][currentcasesheet[0].problem]["question"],
            "options": data["Q17"][currentcasesheet[0].minorlocation][currentcasesheet[0].problem]["options"],
            "casesheetname": request.session.get("casesheetname"),
            "question_name": "question17"
        }
        return render(request, "question_type1.html", {"returndict": returndict})
    else:
        optionselected = request.POST['selectedoption']
        casesheetname = request.POST['currentscasesheetname']
        currentuser = request.user
        mappedcasesheets = Patient_Case_Sheet.objects.filter(
            user=currentuser, case_sheet_name=casesheetname)

        # checks if we got multiple casesheets of same name
        if mappedcasesheets and len(mappedcasesheets) == 1:
            mappedcasesheets.update(q17=optionselected)
        else:
            return HttpResponse("Something went wrong!!!")

        get_medicine_scores(request.user, casesheetname)
        return redirect("go_home")


# for medicine suggestions
def get_medicine_scores(currentuser, casesheetname):
    medicine_scores = {}
    mappedcasesheets = Patient_Case_Sheet.objects.filter(
        user=currentuser, case_sheet_name=casesheetname)

    if(len(mappedcasesheets) > 1):
        print("")
        print("")
        print("do something!!!")
        print("")
        print("")

    print("")
    print("")
    print("hellow" + mappedcasesheets[0].majorlocation)
    print("")
    print("")

    return
