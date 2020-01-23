from django import forms

class NewArticle(forms.Form):
    work_name = forms.CharField(label="Имя должности/работы")
    description_work = forms.CharField(label="Описание", widget=forms.Textarea)