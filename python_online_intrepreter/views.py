import subprocess
import sys

from django.shortcuts import render
from django.views import View

from python_online_intrepreter.forms import (PythonOnlineInterpreterFormAdmin,
                                             PythonOnlineInterpreterFormUsual)

# Create your views here.

template = "poi/index.html"


def get_form_admin(request, form):
    if form.is_valid():
        user_input = form.cleaned_data["user_input"]
        timeout = form.cleaned_data["timeout"]

        try:
            result = subprocess.run(
                [sys.executable, "-c", user_input],
                text=True,
                capture_output=True,
                input=user_input,
                timeout=timeout,
            )
            out = result.stderr if result.stderr else result.stdout
        except subprocess.TimeoutExpired as err:
            out = f"RuntimeError('Your time {err.timeout} is expired')"

        form = PythonOnlineInterpreterFormAdmin(
            {"python_output": out, "user_input": user_input, "timeout": timeout}
        )

        return render(
            request,
            template,
            {
                "form": form,
            },
        )
    else:
        return render(
            request,
            template,
            {
                "form": form,
            },
        )


def get_form_usual(request, form):
    if form.is_valid():
        user_input = form.cleaned_data["user_input"]
        timeout = form.cleaned_data["timeout"]

        try:
            result = subprocess.run(
                [sys.executable, "-c", user_input],
                text=True,
                capture_output=True,
                input=user_input,
                timeout=timeout,
            )
            out = result.stderr if result.stderr else result.stdout
        except subprocess.TimeoutExpired as err:
            out = f"RuntimeError('Your time {err.timeout} is expired')"

        form = PythonOnlineInterpreterFormUsual(
            {"python_output": out, "user_input": user_input, "timeout": timeout}
        )

        return render(
            request,
            template,
            {
                "form": form,
            },
        )
    else:
        return render(
            request,
            template,
            {
                "form": form,
            },
        )


class Main(View):

    @staticmethod  # !!!!!!!
    def get(request, *args, **kwargs):
        if request.user.is_authenticated:
            form = PythonOnlineInterpreterFormAdmin()
        else:
            form = PythonOnlineInterpreterFormUsual()

        return render(
            request,
            template,
            {
                "form": form,
            },
        )

    @staticmethod
    def post(request, *args, **kwargs):
        if request.user.is_authenticated:
            form = PythonOnlineInterpreterFormAdmin(request.POST)
            return get_form_admin(request, form)

        else:
            form = PythonOnlineInterpreterFormUsual(request.POST)
            return get_form_usual(request, form)
