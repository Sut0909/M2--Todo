from django.shortcuts import render
from .models import Todo

# Create your views here.
def indexview(request):
    tasks = Todo.objects.all()
    context = {
        'tasks': tasks
    }

    return render(request, 'index.html',context)
    