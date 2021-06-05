from django.contrib.admin import widgets
from django.db.models import fields
from django.shortcuts import render

# Create your views here.
from django import  forms
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from .models import DTModel
class DTForm(forms.Form):
    your_name = forms.CharField(max_length=64)
    date_input = forms.DateField(widget=AdminDateWidget())
    time_input = forms.DateField(widget=AdminTimeWidget())
    date_time_input = forms.DateField(widget=AdminSplitDateTime())

class DTModelForm(forms.ModelForm):
    date_time = forms.SplitDateTimeField(widget=AdminSplitDateTime())

    class Meta:
        model = DTModel
        fields = "__all__"
        widgets = {
            "date": AdminDateWidget(),
            "time": AdminTimeWidget(),
        }


def index(request):
    form = DTForm()
    return render(request, 'index.html', {'form':form})


def index_v2(request):
    if request.method == "POST":
        form = DTModelForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Error ", form.errors)
    form = DTModelForm()
    return render(request, 'index_v2.html', {'form':form})