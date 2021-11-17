from django import forms
from shift.models import Shift


class ResponseForm(forms.Form):
    selected_response = forms.ModelMultipleChoiceField(queryset=None)
    response_email = forms.EmailField

    def __init__(self, report_name, *args, **kwargs):
        self.report_name = kwargs.pop('report_name')
        super().__init__(*args, **kwargs)
        self.fields['report_name'] = report_name
        self.fields['selected_response'].queryset = ""
