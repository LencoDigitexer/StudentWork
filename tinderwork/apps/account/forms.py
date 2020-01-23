from django import forms

class UserLogin(forms.Form):
    login = forms.CharField(min_length=3, max_length=20, label="Логин")
    passwd = forms.CharField(min_length=3, max_length=25, label="Пароль", widget=forms.PasswordInput())
    #status = forms.ChoiceField(label="Что ты будешь делать на сайте?", choices=(("worker", "Я ищу работу"), ("employer", "Я выдаю вакансии")))

class UserRegister(forms.Form):
    login = forms.CharField(min_length=3, max_length=20, label="Логин", help_text="Придумайте логин для сайта")
    passwd = forms.CharField(min_length=3, max_length=25, label="Пароль", help_text="Придумайте пароль для сайта", widget=forms.PasswordInput())
    status = forms.ChoiceField(label="Что ты будешь делать на сайте?", choices=(("worker", "Я ищу работу"), ("employer", "Я выдаю вакансии")))
