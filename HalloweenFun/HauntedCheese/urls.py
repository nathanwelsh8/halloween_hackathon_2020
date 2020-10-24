from django.urls import path
from HauntedCheese import views
from . import views

app_name = "HauntedCheese"

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('addList/<slug:account_name_slug>',views.AddList.as_view(), name='addList'),
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('spook/', views.Spook.as_view(), name='spook'),
    
]