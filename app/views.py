from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def Student(request):
    SFO=Student_Form()
    d={'SFO':SFO}

    if request.method=='POST':
        SFD=Student_Form(request.POST)

        if SFD.is_valid():
            return HttpResponse(str(SFD.cleaned_data))
        
        else:
            return HttpResponse('Data is not valid')

    return render(request, 'S_Form.html', d)
