from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView


from .models import Todo


# Create your views here.

class TodoAppCreateView(CreateView):
    model = Todo
    fields = ['title', 'description']
    template_name = 'home.html'
    success_url = 'list/'


class TodoAppListView(ListView):
    model = Todo
    template_name = 'list.html'


class TodoAppDetailView(DetailView):
    model = Todo
    template_name = "detail.html"


class TodoAppUpdateView(UpdateView):
    model = Todo
    fields = ['title', 'description']
    template_name = 'update.html'
    success_url = '/'


class TodoAppDeleteView(DeleteView):
    model = Todo
    template_name = 'delete.html'
    success_url = '/'
