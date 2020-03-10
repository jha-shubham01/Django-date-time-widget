from django.shortcuts import render

# Create your views here.
from django import  forms
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime

class DTForm(forms.Form):
    your_name = forms.CharField(max_length=64)
    date_input = forms.DateField(widget=AdminDateWidget())
    time_input = forms.DateField(widget=AdminTimeWidget())
    date_time_input = forms.DateField(widget=AdminSplitDateTime())

def index(request):
    form = DTForm()
    return render(request, 'index.html', {'form':form})