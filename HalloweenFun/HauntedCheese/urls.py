from django.urls import path
from HauntedCheese import views
from . import views

app_name = "HauntedCheese"

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('viewList/',views.ViewList.as_view(), name='viewList'),
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register')
]