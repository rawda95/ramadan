from django.urls import path

from .views import index, UserPage

app_name = 'rmadan'
urlpatterns = [
    path('main/', index, name='index'),
    path('<name>/', UserPage, name='UserPage')

]
