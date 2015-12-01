from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.core.mail import send_mail,EmailMessage
import os
import re
import subprocess
def mylogin(req):
    error = None
    # if req.method == "GET":
        # nexturl = req.GET['next']
        # context={'next':nexturl,
                 # 'errors':errors}
        # return render(req,"login.html",context)
    if req.method == "POST":
        username = req.POST['inputusername']
        password = req.POST['inputpassword']
        # nexturl1 = req.POST['next']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(req,user)
            # return HttpResponseRedirect(nexturl1)
            return HttpResponseRedirect('/labsmith/')
        else:
            error = "Username or password is wrong"
    
    # nexturl = req.GET['next']
    # context={'next':nexturl,
    #          'error':error}
    context = {}
    return render(req,"login.html",context)



def mylogout(request):
    logout(request)
    return HttpResponseRedirect('/labsmith/')

def redirect2labsmith(req):
    return HttpResponseRedirect('/labsmith/')

def register(req):
    errors=[]
    if req.method == "POST":
        if not req.POST.get('username', ''):
            errors.append("Enter username.")
        if User.objects.filter(username__exact=req.POST['username']):
            errors.append("Username used.")
        if not req.POST.get('email', ''):
            errors.append("Enter e-mail.")
        if not req.POST.get('pwd1', ''):
            errors.append("Enter password.")
        if not req.POST.get('pwd2', ''):
            errors.append("Enter confirm password.")
        if not req.POST.get('first_name', ''):
            errors.append("Enter first name.")
        if not req.POST.get('last_name', ''):
            errors.append("Enter last name.")
        if not req.POST['pwd1'] == req.POST['pwd2']:
            errors.append("password not equal")
            
        if not errors:
            user = User.objects.create_user(
                username = req.POST['username'], 
                password = req.POST['pwd1'],
                email = req.POST['email'],
                first_name = req.POST['first_name'].title(),
                last_name = req.POST['last_name'].title(),
            )
            # user = User()
            # user.username = req.POST['username']
            # user.set_password(req.POST['pwd1'])
            # user.first_name = req.POST['first_name']
            # user.last_name = req.POST['last_name']
            # user.email = req.POST['email']
            # user.is_staff = False
            # user.is_superuser = False
            user.is_active = True
            user.save()
            return HttpResponseRedirect("/login/")
        
    context = {'errors':errors,}
    return  render(req, "register.html", context)
	
def reset(req):
    msg=""
    errors= []
    
    if req.method== "POST":
        if not req.POST.get('inputUserName', ''):
            errors.append("Enter username.")
        elif not req.POST.get('inputEmailAddress', ''):
            errors.append("Enter e-mail.")
        elif not User.objects.filter(username__exact=req.POST['inputUserName']):
            errors.append("Username not exist.")
        elif not User.objects.filter(email__exact=req.POST['inputEmailAddress']):
            errors.append("email not exist.")
        elif not User.objects.filter(username__exact=req.POST['inputUserName'],email__exact=req.POST['inputEmailAddress']):
            errors.append("Username or email does not match, please input again.")

        if not errors:
            user = User.objects.get(username = req.POST["inputUserName"])
            password = User.objects.make_random_password()
            print password
           
            user.set_password(password)
            user.save()
            
            usrName = req.POST["inputUserName"]
            mailto=req.POST["inputEmailAddress"]
            print mailto
            
            # subject = "[Labsmith] New password is sent to you " 
            # html_msg = r'<br>An email has been sent to the user %s, You can use the password<u><b> %s </b></u> to log in<br><br><a href="http://10.62.34.99:8010/labsmith/">http://10.62.34.99:8010/labsmith/</a>' % (user,password)
            # from_email = 'alarm@labsmith.com'
            # msg = EmailMessage(subject,html_msg,from_email,[mailto])
            # msg.content_subtype = "html"
            # msg.send(fail_silently=False)
            #send_mail(subject,html_msg,'alarm@labsmith.com',[mailto],fail_silently=False)
            subprocess.call(["/home/joe/labsmith_backup/forgetmail.sh",usrName,password,mailto])
           ###### msg = "Email has been sent"
          #####  print msg
			
            return HttpResponseRedirect('/resetresult/')

        

    context={'msg':msg,
                'errors':errors}
    return render(req,"ForgetEmail.html",context)

def resetresult(req):
    if req.method == "POST":
        return HttpResponseRedirect('/login/')
    context = []
    return render(req,"resetresult.html",context)
