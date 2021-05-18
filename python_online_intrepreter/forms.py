import re

from django import forms
from django.core.validators import RegexValidator
from django_ace import AceWidget

validator_open = RegexValidator(
    inverse_match=True,
    message="You are not allowed to use open()",
    regex=re.compile(r"open\(", re.ASCII),
)

validator_exec = RegexValidator(
    inverse_match=True,
    message="You are not allowed to use exec()",
    regex=re.compile(r"exec\(", re.ASCII),
)

validator_eval = RegexValidator(
    inverse_match=True,
    message="You are not allowed to use eval()",
    regex=re.compile(r"eval\(", re.ASCII),
)
validator_subprocess = RegexValidator(
    inverse_match=True,
    message="You are not allowed to use subprocess()",
    regex=re.compile(r"subprocess\(", re.ASCII),
)

validator_os = RegexValidator(
    inverse_match=True,
    message="You are not allowed to use os module",
    regex=re.compile(r"(?<![\"\'\w\d])os(?![\w\d\"\'])", re.ASCII),
)

validator_builtins = RegexValidator(
    inverse_match=True,
    message="You are not allowed to use __builtins__",
    regex=re.compile(r"__builtins__", re.ASCII),
)


class PythonOnlineInterpreterFormAdmin(forms.Form):
    user_input = forms.CharField(
        widget=AceWidget(
            mode="python",
            theme="xcode",
            width="40vw",
            height="80vh",
            fontsize="12pt",
            toolbar=False,
            showgutter=True,
        ),
        initial="Your code here",
        label=False,
    )

    optional_input = forms.CharField(widget=AceWidget(mode="python",
                                                      theme="xcode",
                                                      width="40vw",
                                                      height="10vh",
                                                      fontsize="12pt",
                                                      toolbar=False,
                                                      showgutter=False,
                                                      ),
                                     initial="#OPTIONAL Your input here",
                                     label=False,
                                     required=False,
                                     )

    python_output = forms.CharField(
        widget=AceWidget(
            mode="python",
            readonly=True,
            theme="xcode",
            width="40vw",
            height="90vh",
            fontsize="12pt",
            toolbar=False,
            showgutter=False,

        ),
        required=False,
        label=False,

    )

    timeout = forms.IntegerField(
        label="Timeout, sec", initial=1, max_value=60, min_value=1
    )


class PythonOnlineInterpreterFormUsual(PythonOnlineInterpreterFormAdmin):
    user_input = forms.CharField(
        widget=AceWidget(
            mode="python",
            theme="xcode",
            width="40vw",
            height="80vh",
            fontsize="12pt",
            toolbar=False,
            showgutter=True,
        ),
        initial="Your code here",
        label=False,
        validators=[
            validator_open,
            validator_exec,
            validator_eval,
            validator_subprocess,
            validator_os,
            validator_builtins,
        ],
    )

    optional_input = forms.CharField(widget=AceWidget(mode="python",
                                                      theme="xcode",
                                                      width="40vw",
                                                      height="10vh",
                                                      fontsize="12pt",
                                                      toolbar=False,
                                                      showgutter=False,
                                                      ),
                                     initial="#OPTIONAL Your input here",
                                     label=False,
                                     required=False,
                                     validators=[
                                         validator_open,
                                         validator_exec,
                                         validator_eval,
                                         validator_subprocess,
                                         validator_os,
                                         validator_builtins,
                                     ],
                                     )
