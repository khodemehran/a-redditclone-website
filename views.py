from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def signup(request):

    if request.method == 'POST':
        if request.POST['username'] == '':
            return render(request,'acounts/signup.html',{'error':'please write a correct user name'})
        else:
            if request.POST['password1'] == request.POST['password2']:

                 try:
                     user = User.objects.get(username=request.POST['username'])
                     return render(request,'acounts/signup.html', {'error':'user has already been taken'})
                 except User.DoesNotExist:
                     user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                     login(request,user)
                     return render(request,'acounts/signup.html')
            else:
                return render(request,'acounts/signup.html', {'error':'Passwords did not match!'})

        
    else:

        return render(request, 'acounts/signup.html')
        
def loginview(request):

    if request.method == 'POST':
        user = authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            #redirect to a success page
            return render(request,'acounts/login.html', {'error':'login succesful!'})
        else:
            return render(request,'acounts/login.html', {'error':'username and Password did not match!'})


        
    else:

        return render(request, 'acounts/login.html')