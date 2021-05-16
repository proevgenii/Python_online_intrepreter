import subprocess
import sys
from django.shortcuts import render
from django.views import View

from python_online_intrepreter.forms import PythonOnlineInterpreterFormAdmin, PythonOnlineInterpreterFormUsual


# Create your views here.


class Main(View):

    @staticmethod  # !!!!!!!
    def get(request, *args, **kwargs):
        if request.user.is_authenticated:  # Наверное при методе GET нет необходимости
            form = PythonOnlineInterpreterFormAdmin()
        else:
            form = PythonOnlineInterpreterFormUsual()

        return render(request, 'poi\index.html', {'form': form, })

    @staticmethod
    def post(request, *args, **kwargs):
        if request.user.is_authenticated:  # Различные возможности open(), exec() и т.д
            form = PythonOnlineInterpreterFormAdmin(request.POST)
        else:
            form = PythonOnlineInterpreterFormUsual(request.POST)

        if form.is_valid():
            user_input = form.cleaned_data['user_input']
            timeout = form.cleaned_data['timeout']

            try:
                result = subprocess.run(
                    [sys.executable, "-c", user_input],
                    text=True,
                    capture_output=True,
                    input=user_input,
                    timeout=timeout)
                out = result.stderr if result.stderr else result.stdout  # !!!!
            except subprocess.TimeoutExpired as err:
                out = f"RuntimeError('Your time {err.timeout} is expired')"  # POPRAVI!!!!!!

            form = PythonOnlineInterpreterFormUsual({'python_output': out,
                                                     'user_input': user_input,
                                                     'timeout': timeout})

            return render(request, 'poi\index.html', {'form': form, })
        else:
            return render(request, 'poi\index.html', {'form': form, })
