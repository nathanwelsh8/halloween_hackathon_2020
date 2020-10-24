from django.http import request
from django.shortcuts import render

  
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

#from spatulaApp.models import Recipe, Category, RecipeImage, UserProfile, Rating, UserImage
from django.urls import reverse 

from django.views import View

# Create your views here.

class Index(View):

    def post(self, request):
        pass
    def get(self, request):
        return render(request, 'HauntedCheese/index.html')

class ViewList(View):
    def get(self, request):
        pass
    def post(self, request):
        pass
