from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from .models import List
from .forms import ListForm
# dusty pigeons man

def home(request):
    context = {
        'items': List.objects.all().order_by("deadline")
    }
    return render(request, 'list/home.html', context)

def add(request):
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-home')
    form = ListForm(request.POST)
    return render(request, 'list/add.html', {'form': form})

def remove(request, pk):
    item = get_object_or_404(List, pk=pk)
    item.delete()
    return redirect('list-home')
    