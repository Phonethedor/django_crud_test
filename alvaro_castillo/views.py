from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Pizza


# Create your views here.
def index(request):
    return render(request, "alvaro_castillo/index.html")

def add(request):
    Pizza.objects.create(
    nombre = request.POST['nombre'],
    ingredientes = request.POST['ingredientes'],
    valor = request.POST['valor'],
    )
    return render(request,"alvaro_castillo/index.html")

class read(ListView):
    template_name: "read.html"
    model = Pizza
    context_object_name = 'lista'

def getId(request):
    pizza = Pizza.objects.get(id=request.POST['id'])
    context = {
        "pizza": pizza
    }
    return render(request,'alvaro_castillo/edit.html', context)

def update(request):
    pizza = Pizza.objects.get(id=request.POST['id'])

    errores= Pizza.objects.validador_pizza(request.POST)
    
    if len(errores) == 0:
        pizza.nombre = request.POST['nombre']
        pizza.ingredientes = request.POST['ingredientes']
        pizza.valor = request.POST['valor']
        pizza.save()
    
    return redirect('/read')

def delete(request):
    pizza = Pizza.objects.get(id=request.POST['id'])
    pizza.delete()
    return redirect("/read")