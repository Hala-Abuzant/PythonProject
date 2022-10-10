from django.shortcuts import render,HttpResponse,redirect
import bcrypt
from .models import *
from django.contrib import messages

def form1(request):

        return render(request, 'registerdriver.html')


def driver(request):
    return render(request, 'driver.html')

def police(request):
    return render(request, 'police.html')

def login(request):
    return render(request, 'login.html')    

def reg(request):
    
        request.session['type'] = 'driver'
        errors = Driver.objects.basic_validator(request.POST)
        users=Driver.objects.all()
        # for user in users:
        #     if user.email==request.POST['email']:
        #         errors['email']="this email aleady exsist"

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        password= request.POST['password']
        pw_hash= bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() 
        Driver.objects.create (
            full_name=request.POST['fullname'],
            birthday=request.POST['birthday'],
            notional_id=request.POST['nid'],
            city=request.POST['city'],
            blood_type=request.POST['bloodtype'],
            email=request.POST['email'],
            password=pw_hash,
            phone_number=request.POST['phonenumber'],
        
        )
        name1=Driver.objects.last()
        request.session['full_name']=name1.full_name
        request.session['driver_id'] = name1.id

        return redirect('/driver')

def regpolice(request):
    
        errors = Police.objects.basic_validator(request.POST)
        polices=Police.objects.all()
        for police in polices:
            if police.email==request.POST['email']:
                errors['email']="this email aleady exsist"

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        password= request.POST['password']
        pw_hash= bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() 
        Police.objects.create (
            full_name=request.POST['fullname'],
            birthday=request.POST['birthday'],
            city=request.POST['city'],
            email=request.POST['email'],
            password=pw_hash,
            phone_number=request.POST['phonenumber'],
        
        )
        name1=Police.objects.last()
        request.session['full_name_p']=name1.full_name
        request.session['police_id'] = name1.id

        return redirect('/regp')

def signin(request):
    if request.POST['type']=='driver':
        driver = Driver.objects.filter(email=request.POST['email2']) 
        if driver:
            logged_driver=driver[0]


            if bcrypt.checkpw(request.POST['password2'].encode(),logged_driver.password.encode()):
                request.session['user_id'] = logged_driver.id
                request.session['user_name']= logged_driver.full_name
                return redirect('/driver')
            else:
                messages.error(request,"Your email or password is wrong try ag!")
                return redirect('/')
        else:
            messages.error(request,"Your email or password is wrong try ag!")

        return redirect('/')

    


