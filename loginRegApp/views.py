from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from . models import *


def index(request):
    return render(request, "mark.html")

def Reggae(request):
    errorFromTheValidator = RegistrationForm.objects.i_am_the_validator(request.POST)

    print("Errors from the Validator is HERE!!!", errorFromTheValidator)

    if len(errorFromTheValidator)>0:
        for key, value in errorFromTheValidator.items():
            messages.error(request, value)
        return redirect("/")
            

    newuser = RegistrationForm.objects.create(first_name = request.POST["fname"], last_name = request.POST["lname"], email = request.POST["eml"], password = request.POST["PW"])

    request.session["UserID"] = newuser.id
    
    return redirect("/success")

def weMadeIt(request):
    print("********************")
    print(request.POST)
    print("********************")
    if "UserID" not in request.session:
        return redirect("/")


    

    context = {
        'Pickachu': RegistrationForm.objects.get(id=request.session["UserID"])
    }



    return render(request, "loginpg.html", context)

def ImIn(request):
    

    errorFromTheValidator = RegistrationForm.objects.loginVal(request.POST)
    if len(errorFromTheValidator)>0:
        for key, value in errorFromTheValidator.items():
            messages.error(request, value)
        return redirect("/")

    else: 
        user = RegistrationForm.objects.get(email = request.POST['eml']) 

        request.session["UserID"] = user.id

        return redirect("/success")

def logout(request):
    request.session.clear()
    return redirect("/")