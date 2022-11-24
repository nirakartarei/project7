from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':20000,'b':800000,'c':900000}
    return render(request,'condition.html',d)
