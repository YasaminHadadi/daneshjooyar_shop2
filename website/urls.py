from django.urls import path
#from shop import views
from .views import index

app_name= "website"


urlpatterns = [
    path('',index, name="index"),


]
