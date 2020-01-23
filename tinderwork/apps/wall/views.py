from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from dashboard.models import Work

def get_work_name(id):
    #work_name = "Prgger"
    work_name = Work.objects.get(id=id)
    return work_name.id


def wall_index(request):
    value = request.COOKIES.get('authorization') #куки об успешной авторизации
    
    try:
        session_key = request.COOKIES[settings.SESSION_COOKIE_NAME]
    except:
        pass
    #context = {"user_name" : "",
    #            "error" : "",
    #            "work_name" : ""}

    if value is None: # если пользваткль не авторизовался
        context = {"error":'Вы не авторизованы'}
        response = render(request, 'wall/index.html', context) 
        response.set_cookie("list", 2)
        return response

    if value is not None: # если пользователь авторизовался
        list_id = request.COOKIES.get('list') #куки об успешной авторизации
        context = {"position" : ""} # инициализация отношения к вакансии
        context["user_name"] = value # инициализация имени пользователя из кук
        context["work_name"] = get_work_name(list_id) #init вакансии по ее id
        context["session_id"] = session_key #test function

        if request.POST or None: #обработка нажатий разных кнопок
            if '_like' in request.POST:
                context["position"] = "нравится"
                list_id = request.COOKIES.get('list') #куки об успешной авторизации
                list_id =+ 1
            if '_dislike' in request.POST:
                context["position"] = "не нравится"
                list_id = request.COOKIES.get('list') #куки об успешной авторизации
                list_id =+ 1
        
        response = render(request, 'wall/index.html', context) #рендерин странички 

        if list_id is not None: # если id вакансии существует
            response.set_cookie("list", list_id)
            return response


        if list_id is None: # если куки с list не существует, то отправить ошибку
            pass