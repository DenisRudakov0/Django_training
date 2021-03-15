from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Отвечает за методы которые будут вызваны при переходя польователя на какуе-то определенную страницу
def index(request):
    return render(request, 'main/index.html') # метод render позволяет отображать полноценные html странички

def about(request):
    return HttpResponse('<h4>Ссылка 2</h4>')
