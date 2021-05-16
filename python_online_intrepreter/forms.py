import re
from django import forms
from django_ace import AceWidget
from django.core.validators import RegexValidator

validator_open = RegexValidator(inverse_match=True,
                                message='You are not allowed to use open()',
                                regex=re.compile(r'open\(', re.ASCII))

validator_exec = RegexValidator(inverse_match=True,
                                message='You are not allowed to use exec()',
                                regex=re.compile(r'exec\(', re.ASCII))

validator_eval = RegexValidator(inverse_match=True,
                                message='You are not allowed to use eval()',
                                regex=re.compile(r'eval\(', re.ASCII))
validator_subprocess = RegexValidator(inverse_match=True,
                                      message='You are not allowed to use subprocess()',
                                      regex=re.compile(r'subprocess\(', re.ASCII))

validator_os = RegexValidator(inverse_match=True,
                              message='You are not allowed to use os module',
                              regex=re.compile('os', re.ASCII))

validator_path = RegexValidator(inverse_match=True,
                                message='You are not allowed to use path',
                                regex=re.compile('path', re.ASCII))


class PythonOnlineInterpreterFormAdmin(forms.Form):
    user_input = forms.CharField(widget=AceWidget(mode="python",
                                                  theme='xcode',
                                                  width="500px",
                                                  height="90vh",
                                                  fontsize='12pt',
                                                  toolbar=False,
                                                  showgutter=True,
                                                  ),
                                 initial='Your code here', label=False)

    python_output = forms.CharField(widget=AceWidget(mode="python",
                                                     readonly=True,
                                                     theme='xcode',
                                                     width="500px",
                                                     height="90vh",
                                                     fontsize='12pt',
                                                     toolbar=False,
                                                     showgutter=False,
                                                     ),
                                    required=False, label=False)

    timeout = forms.IntegerField(label='Timeout, sec', initial=1, max_value=60, min_value=1)


class PythonOnlineInterpreterFormUsual(PythonOnlineInterpreterFormAdmin):
    user_input = forms.CharField(widget=AceWidget(mode="python",
                                                  theme='xcode',
                                                  width="500px",
                                                  height="90vh",
                                                  fontsize='12pt',
                                                  toolbar=False,
                                                  showgutter=True,
                                                  ),
                                 initial='Your code here', label=False,
                                 validators=[validator_open, validator_exec, validator_eval, validator_subprocess,
                                             validator_os])