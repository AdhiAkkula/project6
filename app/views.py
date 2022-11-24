from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':120,'b':2609,'c':19970}
    return render(request,'condition.html',d)