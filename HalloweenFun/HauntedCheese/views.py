from django.http import request
from django.shortcuts import render
from django.views import View

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.urls import reverse 

from HauntedCheese.models import Todo, TodoIterator
from HauntedCheese.forms import UserForm 


# Create your views here.

class Index(View):

    context_dict = {}

    # handle get requests
    def get(self, request):
        return render(request, 'HauntedCheese/index.html', self.context_dict)

    # handle post requests
    def post(self, request):
        pass
    

class ViewList(View):

    context_dict = {}

    def get(self, request):
        pass
    def post(self, request):
        pass

class Login(View):

    context_dict = {}
    def get(self, request, **kwargs):
        pass

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        # If they clicked the register button they are redirected to register page.
        if 'register' in request.POST:
            return redirect(reverse('spatulaApp:register'))

        user = authenticate(username=str(username.lower()), password=str(password))
        
        if user: 
            if user.is_active:
                login(request, user)
                return redirect(reverse('spatulaApp:index'))
            else: 
                return self.get(request, **{"login_error_msg":"Your Spatula account has been disabled."})
                
        else:
            return self.get(request, **{"login_error_msg":"Invalid login details supplied."})

class Register(View):
    context_dict = {}

    def get(self,request, **kwargs):
        pass

    def post(self,request):
         # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            user.username = user.username.lower()
            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()
           
            # Update our variable to indicate that the template
            # registration was successful.
            registered = True
            
            user = authenticate(username=user.username.lower(), password=user_form['password'].data)
            if user:
                login(request, user)
                
            return redirect(reverse('spatulaApp:index'))
        else:
            # Invalid form or forms - mistakes or something else?
            # Print problems to the terminal.
            return self.get(request,**{"errors":user_form.errors})