from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import todo

# Create your views here.
def homepage(request):
    #return HttpResponse("<h1> MY home page</h1>")
    my_task= todo.objects.all() #this is used to get all the content(model) of the admin page
    print(my_task)
    my_dict= {"all_content" : my_task}
    return render(request, "home.html", my_dict)


def addtask(request):
    post_var = request.POST["text_var"]
    new_task_var = todo(text_var= post_var)
    new_task_var.save()
    return HttpResponseRedirect("/")  #To redirect back to my home page

    #return HttpResponse("<h1> MY add page</h1>")
   
def deletetask(request, todo_id):
    del_var = todo.objects.get(id = todo_id)
    del_var.delete()
    return HttpResponseRedirect("/")  #To redirect back to my home page
