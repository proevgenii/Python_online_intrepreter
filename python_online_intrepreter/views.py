from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from django.views import View


class Main(View):


    def get(self, request, *args, **kwargs):
        return render(request, 'poi\index.html')

    def post(self, request, *args, **kwargs):
        return render(request)
