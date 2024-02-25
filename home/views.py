from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    peoples =[
        {'name': 'Bhim', 'age':21,},
        {'name': "Lucky", 'age':22},
        {'name': 'lolo', 'age':27}
        

    ]
    return render(request , "home/index.html", context ={'peoples':peoples})
def about(request):
    return HttpResponse(request, "home/about.html")

def contact(request):
    return HttpResponse(request, "home/contact.html")
def sucess_page(request):
    return HttpResponse("<h1>Hey this is Sucess page </h1>")
