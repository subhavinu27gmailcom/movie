
from django.urls import path, include

from movieapp import views
app_name = "movieapp"

urlpatterns = [


    path('',views.index,name="index"),
    path('movie/<int:movie_id>/',views.detail,name="detail"),
     path('add/',views.add,name="add"),
     path('update/<int:movie_id>',views.update,name="update"),

]