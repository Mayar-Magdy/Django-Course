from django.urls import path

from . import views
urlpatterns = [
    path("",views.index,),
    path("<int:month_number>",views.month_by_number , ),
    path("<str:month_name>",views.month_by_name , name ='month_by_name' ),

]
