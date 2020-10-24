from django.http import request
from django.shortcuts import render
from django.views import View
from django.utils import timezone

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.urls import reverse 

from HauntedCheese.models import Todo
from HauntedCheese.forms import UserForm

def getTodoLists(request):
    x = Todo.objects.filter(user=User.objects.get(id=request.user.id))
    print("found:",x)
    return x

def getStatusOccurences(usersTodoLists):
    # returns a tuple with the number of pending and complete to do list items in the form: (PENDING, DONE)
    return (usersTodoLists.objects.filter(usersTodoLists__status=0).count(), usersTodoLists.objects.filter(usersTodoLists__status=1).count())

# Create your views here.

class Index(View):

    context_dict = {}

    # handle get requests
    def get(self, request):

        self.context_dict['todo_list'] = getTodoLists(request)

        current_time = timezone.now()
        for item in self.context_dict['todo_list']:
            if item.due_time > current_time and item.status == 0:
                self.context_dict['failure'] = True
            else:
                self.context_dict['failure'] = False

        return render(request, 'HauntedCheese/index.html', self.context_dict)

    # handle post requests
    def post(self, request):
        todo = Todo.objects.get(id = request.POST.get("todoid"))
        todo.status = 1
        todo.save()
        return self.get(request)
    

class Spook(View):

    context_dict = {}

    # handle get requests
    def get(self, request):
        return render(request, 'HauntedCheese/spook.html', self.context_dict)

    # handle post requests
    def post(self, request):
        pass

class AddList(View):

    context_dict = {}

    def get(self, request):
        if(not request.user.is_authenticated):
            return redirect(reverse('HauntedCheese:login'))
        
       
        return render(request, 'HauntedCheese/addList.html', context= self.context_dict)
    def post(self, request):
        print("POST request")
        
        user = User.objects.get(id = request.user.id)

        new_todo = Todo.objects.get_or_create(
                user=user,
                title=request.POST.get("todo_label"),
                description = request.POST.get("todo_description"),
                created_time = request.POST.get("start"),
                due_time = request.POST.get("end"),
                status = 0
                 )[0]
        new_todo.save()

        print(request.POST)
        return self.get(request)

class Login(View):

    context_dict = {}
    def get(self, request, **kwargs):
        self.context_dict["user_form"] = UserForm()
        return render(request, "HauntedCheese/login.html", self.context_dict)

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        # If they clicked the register button they are redirected to register page.
        if 'register' in request.POST:
            return redirect(reverse('HauntedCheese:register'))

        user = authenticate(username=str(username.lower()), password=str(password))
        if user: 
            if user.is_active:
                login(request, user)
                return redirect(reverse('HauntedCheese:index'))
        else:
            return self.get(request, **{"login_error_msg":"Invalid login details supplied."})

class Register(View):
    context_dict = {}
    registered = False

    def get(self,request, **kwargs):

        self.context_dict["registered"] = self.registered
        self.context_dict["user_form"] = UserForm()
        return render(request, 'HauntedCheese/register.html', self.context_dict)

    def post(self,request):
        # called when user presses submit

        # Attempt to grab information from the raw form information.
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
            self.registered = True

            user = authenticate(username=user.username.lower(), password=user_form['password'].data)
            if user:
                login(request, user)

            return redirect(reverse('HauntedCheese:index'))
        else:
            # Invalid form or forms - mistakes or something else?
            # Print problems to the terminal.
            return self.get(request,**{"formErrors":user_form.errors})

class Logout(View): 

    def get(self,request):
        if(request.user.is_authenticated):
            logout(request)

        
        # Take the user back to login page.
        return redirect(reverse('HauntedCheese:login'))
    
    def post(self,request):
        return redirect(reverse('HauntedCheese:index'))
