import re
from django import forms
from django_ace import AceWidget
from django.core.validators import RegexValidator

validator_open = RegexValidator(inverse_match=True,
                                message='You are not allowed to use open()',
                                regex=re.compile('open', re.ASCII))

validator_exec = RegexValidator(inverse_match=True,
                                message='You are not allowed to use exec()',
                                regex=re.compile('exec', re.ASCII))

validator_eval = RegexValidator(inverse_match=True,
                                message='You are not allowed to use eval()',
                                regex=re.compile('eval', re.ASCII))
validator_subprocess = RegexValidator(inverse_match=True,
                                      message='You are not allowed to use subprocess()',
                                      regex=re.compile('subprocess', re.ASCII))

validator_os = RegexValidator(inverse_match=True,
                              message='You are not allowed to use os module',
                              regex=re.compile('os', re.ASCII))

validator_file = RegexValidator(inverse_match=True,
                                message='You are not allowed to use os module',
                                regex=re.compile('os', re.ASCII))


class PythonOnlineInterpreterFormAdmin(forms.Form):
    user_input = forms.CharField(widget=AceWidget(mode="python",
                                                  theme='xcode',
                                                  wordwrap=False,
                                                  width="500px",
                                                  height="90vh",
                                                  minlines=None,
                                                  maxlines=None,
                                                  showprintmargin=True,
                                                  showinvisibles=False,
                                                  usesofttabs=True,
                                                  tabsize=None,
                                                  fontsize='12pt',
                                                  toolbar=False,
                                                  readonly=False,
                                                  showgutter=True,  # To hide/show line numbers
                                                  behaviours=True,
                                                  # To disable auto-append of quote when quotes are entered
                                                  ),
                                 initial='Your code', label=False)

    python_output = forms.CharField(widget=AceWidget(mode="python",
                                                     readonly=True,
                                                     theme='xcode',
                                                     wordwrap=False,
                                                     width="500px",
                                                     height="90vh",
                                                     minlines=None,
                                                     maxlines=None,
                                                     showprintmargin=True,
                                                     showinvisibles=False,
                                                     usesofttabs=False,
                                                     tabsize=None,
                                                     fontsize='12pt',
                                                     toolbar=False,
                                                     showgutter=False,  # To hide/show line numbers
                                                     behaviours=True,
                                                     ),
                                    required=False, label=False)

    timeout = forms.IntegerField(label='Timeout, sec', initial=1, max_value=60, min_value=1)


class PythonOnlineInterpreterFormUsual(PythonOnlineInterpreterFormAdmin):
    user_input = forms.CharField(widget=AceWidget(mode="python",
                                                  theme='xcode',
                                                  wordwrap=False,
                                                  width="500px",
                                                  height="90vh",
                                                  minlines=None,
                                                  maxlines=None,
                                                  showprintmargin=True,
                                                  showinvisibles=False,
                                                  usesofttabs=True,
                                                  tabsize=None,
                                                  fontsize='12pt',
                                                  toolbar=False,
                                                  readonly=False,
                                                  showgutter=True,  # To hide/show line numbers
                                                  behaviours=True,
                                                  # To disable auto-append of quote when quotes are entered
                                                  ),
                                 initial='Your code', label=False,
                                 validators=[validator_open, validator_exec, validator_eval, validator_subprocess,
                                             validator_os])

    python_output = forms.CharField(widget=AceWidget(mode="python",
                                                     readonly=True,
                                                     theme='xcode',
                                                     wordwrap=False,
                                                     width="500px",
                                                     height="90vh",
                                                     minlines=None,
                                                     maxlines=None,
                                                     showprintmargin=True,
                                                     showinvisibles=False,
                                                     usesofttabs=False,
                                                     tabsize=None,
                                                     fontsize='12pt',
                                                     toolbar=False,
                                                     showgutter=False,
                                                     behaviours=True,
                                                     ),
                                    required=False, label=False)

    timeout = forms.IntegerField(label='Timeout, sec', initial=1, max_value=60, min_value=1)
