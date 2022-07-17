from unicodedata import name
from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns =[

    path('',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('index/',views.index,name="index"),
    path('addapp/',views.addapp,name="addapp"),
    #path('update/<str:pk>',views.update,name='update'),
    #path('delete/<str:pk>',views.delete,name='delete')
    

]

