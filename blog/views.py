from django.shortcuts import render
from django.http import HttpResponse

l=[]
for i in range(1,21):
    l.append(i)





def home(request):


    contex={
        "list":l,
    }
    return render(request, 'home.html', contex)

def about(request):
    return render(request, 'about.html')

def case(request):
    first = int(request.GET['fname'])
    last = int(request.GET['lname'])
    m=[]
    if first<last:
        for i in range(first,last):
            m.append(i)
        context = {
            'lust': m,
        }
        return render(request, 'case.html', context)
    else:
        return HttpResponse('<p>Starting point has to be less than ending point<p>')


