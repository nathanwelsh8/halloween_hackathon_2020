from django.http import request
from django.shortcuts import render

  
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

from HauntedCheese.models import Todo, TodoIterator
from django.urls import reverse 

from django.views import View

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
