from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NewArticle
from .models import Work
# Create your views here.
def dash_index(request):
    cookie_user = request.COOKIES.get('authorization') #куки об успешной авторизации

    if cookie_user is None: # если пользваткль не авторизовался
        context = {"error":'Вы не авторизованы'}
        response = render(request, 'dashboard/index.html', context) 
        return response

    form = NewArticle(request.POST or None)
    if form.is_valid():
        work_name = form.cleaned_data.get("work_name")
        description_work = form.cleaned_data.get("description_work")
        new_work = Work(work_name=work_name, description_work=description_work)
        new_work.save()
        return HttpResponseRedirect("list/")
    else:
        context= {'form': form}
        return render(request, 'dashboard/index.html', context)

def list_work(request):
    vacansy = Work.objects.all()
    return render(request, "dashboard/list_work.html", {"work": vacansy})