from django import forms

class SalaryReportform(forms.Form):
    start_date = forms.DateField()
    end_date = forms.DateField()    