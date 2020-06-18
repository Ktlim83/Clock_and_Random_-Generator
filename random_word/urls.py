from django.urls import path


from . import views

urlpatterns = [

    path('random_word', views.get_random_word),
    path('reset',views.reset),
    
    
  
]

