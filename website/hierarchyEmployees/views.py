from django.shortcuts import render

# Create your views here.
def base():
    context = {}
    return context


def index(request):
    context = {}
    context.update(base())
    return render(request, 'hierarchyEmployees/index.html', context)