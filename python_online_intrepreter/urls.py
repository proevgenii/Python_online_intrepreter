from django.contrib import admin
from django.urls import path

from python_online_intrepreter.views import Main

urlpatterns = [
    path("", Main.as_view()),
]
