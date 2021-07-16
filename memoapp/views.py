from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.edit import FormMixin, UpdateView, DeleteView

from memoapp.decorators import memo_ownership_required
from memoapp.forms import MemoCreationForm
from memoapp.models import Memo


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class MemoCreateView(CreateView):
    model = Memo
    form_class = MemoCreationForm
    template_name = 'memoapp/create.html'

    def form_valid(self, form):
        temp_memo = form.save(commit=False)
        temp_memo.writer = self.request.user
        temp_memo.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('memoapp:detail', kwargs={'pk':self.object.pk})

class MemoDetailView(DetailView, FormMixin):
    model = Memo
    form_class = MemoCreationForm
    context_object_name = 'target_memo'
    template_name = 'memoapp/detail.html'


@method_decorator(memo_ownership_required, 'get')
@method_decorator(memo_ownership_required, 'post')
class MemoUpdateView(UpdateView):
    model = Memo
    context_object_name = 'target_memo'
    form_class = MemoCreationForm
    template_name = 'memoapp/update.html'

    def get_success_url(self):
        return reverse('memoapp:detail', kwargs={'pk': self.object.pk})

@method_decorator(memo_ownership_required, 'get')
@method_decorator(memo_ownership_required, 'post')
class MemoDeleteView(DeleteView):
    model = Memo
    context_object_name = 'target_memo'
    success_url = reverse_lazy('memoapp:list')
    template_name = 'memoapp/delete.html'

class MemoListView(ListView):
    model = Memo
    context_object_name = 'memo_list'
    template_name = 'memoapp/list.html'
    paginate_by = 5