from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.edit import FormMixin, CreateView

from todoapp.forms import TodoCreationForm
from todoapp.models import Todo


@method_decorator(login_required(login_url='/accounts/login/'), 'get')
class TodoListView(ListView, FormMixin):
    model = Todo
    form_class = TodoCreationForm
    context_object_name = 'todo_list'
    template_name = 'todoapp/list.html'

    def get_context_data(self, **kwargs):
        object_list = Todo.objects.filter(user=self.request.user)
        return super(TodoListView, self).get_context_data(object_list=object_list, **kwargs)


@method_decorator(login_required(login_url='/accounts/login/'), 'get')
@method_decorator(login_required(login_url='/accounts/login/'), 'post')
class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoCreationForm
    template_name = 'todoapp/create.html'

    def form_valid(self, form):
        temp_todo = form.save(commit=False)
        temp_todo.user = self.request.user
        temp_todo.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('todoapp:list')