from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib import auth,messages
from .models import Test
from joblib import load
# Create your views here.
def index(request):
    return render(request,'index.html')

model=load('D:/Django/CropPredict/CropPredict/savemodels/model.joblib')


# def register(request):
#     if request.method=="POST":
#         f=request.POST['first']
#         l=request.POST['last']
#         e=request.POST['email']
#         u=request.POST['uname']
#         p1=request.POST['psw']
#         p2=request.POST['psw-repeat']
#         dob=request.POST['date']
#         if(p1==p2):
#             if(Register.objects.filter(Email=e).exists()):
#                 messages.info(request,"Email exists")
#                 return render(request,"register.html")
#             elif(Register.objects.filter(username=e).exists()):
#                 messages.info(request,"Username exists")
#                 return render(request,"register.html")
#             else:
#                  r=Register.objects.create(FirstName=f,LastName=l,Email=e,username=u,dob=dob,password=p1)
#                  r.save()
#                  return redirect('login.html')
#         else:
#             messages.info(request,"Password Does Not Matches")
#             return render(request,"register.html")

#     else:
#         return render(request,"register.html")
    
#     return render(request,"register.html")


def register(request):
    if request.method=="POST":
        f=request.POST['first']
        l=request.POST['last']
        e=request.POST['email']
        u=request.POST['uname']
        p1=request.POST['psw']
        p2=request.POST['psw-repeat']
        if p1==p2:
            if User.objects.filter(email=e).exists():
                messages.info(request,"Email exists")
                return render(request,"register.html")
            elif User.objects.filter(username=u).exists():
                messages.info(request,"Username Exists")
                return render(request,"register.html")
            else:
                user=User.objects.create_user(first_name=f,last_name=l,email=e,username=u,password=p1)
                user.save()
                return redirect('login.html')
        else:
            messages.info(request,'Password Not Matching')
            return render(request,"register.html")

    else:
        return render(request,"register.html")
    return render(request,"register.html")

def login(request):
    if request.method=='POST':
        u=request.POST['uname']
        p1=request.POST['psw']
        user=auth.authenticate(username=u,password=p1)
        if user is not None:
            auth.login(request,user)
            return redirect('authenticate.html')
        else:
            messages.info(request,"Invalid Credentials")
            return render(request,"login.html")


    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('index.html')
def pricing(request):
    return render(request,"pricing.html")

def authenticate(request):
    return render(request,"authenticate.html")

def contacts(request):
    return render(request,"contacts.html")

def test1(request):
    if request.method=="POST":
        N=request.POST['N']
        P=request.POST['p']
        K=request.POST['k']
        t=request.POST['temperature']
        ph=request.POST['ph']
        h=request.POST['humidity']
        r=request.POST['rain']
        N=int(N)
        P=int(P)
        K=int(K)
        t=int(t)
        ph=int(ph)
        h=int(h)
        r=int(r)
        y_pred=model.predict([[N,P,K,t,ph,h,r]])
        if y_pred[0]==1:
            y_pred="Rice"
        elif y_pred[0]==2:
            y_pred="Maize"
        elif y_pred[0]==3:
            y_pred="soyabeans"
        elif y_pred[0]==4:
            y_pred="beans"
        elif y_pred[0]==5:
            y_pred="Peas"
        elif y_pred[0]==6:
            y_pred="GroundNuts"
        elif y_pred[0]==7:
            y_pred="Cowpeas"
        elif y_pred[0]==8:
            y_pred="Banana"
        elif y_pred[0]==9:
            y_pred="mango"
        elif y_pred[0]==10:
            y_pred="grapes"
        elif y_pred[0]==11:
            y_pred="watermelon"
        elif y_pred[0]==12:
            y_pred="apple"
        elif y_pred[0]==13:
            y_pred="orange"
        elif y_pred[0]==14:
            y_pred="cotton"
        else:
            y_pred="coffee"
        return render(request,"result.html",{'result': y_pred})
        
        
    else:
        return render(request,"result.html")

def predictor(request):
    return render(request,"test.html")


    




