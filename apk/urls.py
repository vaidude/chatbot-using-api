from django.urls import path
from .import views
urlpatterns = [
    path('',views.chatbot,name='chatbot'),
    path('chatbot/',views.chatbot,name='chatbot'),
    path('index/',views.index,name='index'),

]