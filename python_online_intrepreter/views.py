import subprocess
import sys

from django.shortcuts import render

import io
from contextlib import redirect_stdout
import traceback

##########

# Create your views here.
from django.views import View

from python_online_intrepreter.forms import PythonOnlineInterpreterFormAdmin, PythonOnlineInterpreterFormUsual


class Main(View):

    def get(self, request, *args, **kwargs):
        form = PythonOnlineInterpreterFormUsual()

        return render(request, 'poi\index.html', {'form': form, })

    def post(self, request, *args, **kwargs):
        print(request.user)
        if request.user.is_authenticated:
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
                out = result.stderr if result.stderr else result.stdout
            except subprocess.TimeoutExpired as err:
                out = "RuntimeError('Your time is expired')"  # POPRAVI!!!!!!

            form = PythonOnlineInterpreterFormUsual({'python_output': out,
                        'user_input': user_input,
                        'timeout': timeout})

            return render(request, 'poi\index.html', {'form': form, })
        else:
            return render(request, 'poi\index.html', {'form': form, })
