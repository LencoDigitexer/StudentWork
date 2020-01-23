from django.shortcuts import render
from django.shortcuts import redirect #для перенаправления
from django.http import HttpResponse
from django.contrib.auth.models import User #авторизация
from django.contrib.auth.models import Group #добавлять юзера в группу
from .forms import UserLogin
from .forms import UserRegister #форма регистрации
from django.contrib.auth import authenticate, login

import datetime
def set_cookie(response, key, value, days_expire = 7):
    if days_expire is None:
        max_age = 365 * 24 * 60 * 60  #one year
    else:
        max_age = days_expire * 24 * 60 * 60 
    expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
    response.set_cookie(key, value, max_age=max_age, expires=expires, domain=settings.SESSION_COOKIE_DOMAIN, secure=settings.SESSION_COOKIE_SECURE or None)

# Create your views here.
'''
def index(request):
    return render(request, 'accounts/login.html')
'''

def login_user(request):
    #создание глобальных переменных
    uservalue = ''
    passwordvalue = ''

    #создаём экземпляр form формы Loginform
    form = UserLogin(request.POST or None)
    if form.is_valid():#если форма верна, то берем из шаблона формы данные
        uservalue = form.cleaned_data.get("login")
        passwordvalue = form.cleaned_data.get("passwd")

        #встроенная уатентификация
        user = authenticate(username=uservalue, password=passwordvalue)

        # если пользователь существует
        if user is not None:
            # регистрируем пользователя, передаём запрос и пользователя.
            login(request, user)
            context= {'form': form,
                      'error': 'Вход в систему прошел успешно'}
            response = render(request, 'accounts/login.html', context)
            response = redirect('/account/')
            response.set_cookie('authorization', user)
            return response
        else:
            context= {'form': form,
                      'error': 'Неверная комбинация имени пользователя и пароля'}
            
            return render(request, 'accounts/login.html', context )

    else:
        context= {'form': form}
        return render(request, 'accounts/login.html', context)


def register_user(request):
    #создание глобальных переменных
    uservalue = ''
    passwordvalue = ''
    statusvalue = ''

    form = UserRegister(request.POST or None)
    if form.is_valid():#если данные верна, то берем из шаблона формы данные
        uservalue = form.cleaned_data.get("login")
        passwordvalue = form.cleaned_data.get("passwd")
        statusvalue = form.cleaned_data.get("status")

        #инициализация групп статуса
        worker_group = Group.objects.get(name='worker')
        employer_group = Group.objects.get(name='employer')

        # Создайте пользователя и сохраните его в базе данных
        user = User.objects.create_user(username=uservalue, email=None, password=passwordvalue)

        #добавляем юзера в группу   
        if statusvalue == 'worker':
            worker_group.user_set.add(user)
        if statusvalue == 'employer':
            employer_group.user_set.add(user)
        # сохраняем юзера
        user.save()
        if user is None: #если юзер не существует
            # регистрируем пользователя, передаём запрос и пользователя.
            login(request, user)
            context= {'form': form,
                      'error': 'Неверная комбинация имени пользователя и пароля'}
            
            return render(request, 'accounts/register.html', context)
        else:
            context= {'form': form,
                      'error': "Вы зарегестрировались как " + str(statusvalue)}
            
            return render(request, 'accounts/register.html', context )
    else:
        context= {'form': form}
        return render(request, 'accounts/register.html', context)

def account_index(request):
    value = request.COOKIES.get('authorization')
    return HttpResponse(value)

