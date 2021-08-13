from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from django.views.generic.edit import FormMixin

from memoapp.forms import MemoForm
from memoapp.models import Memo

# def memo_create(request):
#     form = MemoForm(request.POST)
#     if form.is_valid():
#         title = request.POST.get('title')
#         content = request.POST.get('content')
#         user = request.user
#         return redirect("home")
#     return render(request, "memoapp/create.html", {"form": form})


@method_decorator(login_required(login_url='/accounts/login/'), 'get')
@method_decorator(login_required(login_url='/accounts/login/'), 'post')
class MemoCreateView(CreateView):
    model = Memo
    form_class = MemoForm
    template_name = 'memoapp/create.html'

    def form_valid(self, form):
        temp_memo = form.save(commit=False)
        temp_memo.user = self.request.user
        temp_memo.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('memoapp:list', kwargs={'pk':self.object.pk})
        # return HttpResponseRedirect(reverse('memoapp:list'))


@method_decorator(login_required(login_url='/accounts/login/'), 'get')
class MemoListView(ListView, FormMixin):
    model = Memo
    form_class = MemoForm
    context_object_name = 'memo_list'
    template_name = 'memoapp/list.html'
    paginate_by = 5


@method_decorator(login_required(login_url='/accounts/login/'), 'get')
class MemoDetailView(DetailView, FormMixin):
    model = Memo
    form_class = MemoForm
    context_object_name = 'target_memo'

    def get_success_url(self):
        return reverse('memoapp:list')


@method_decorator(login_required(login_url='/accounts/login/'), 'get')
class MemoUpdateView(UpdateView, FormMixin):
    model = Memo
    context_object_name = 'target_memo'
    form_class = MemoForm

    def get_success_url(self):
        return reverse('memoapp:list')

@login_required(login_url='/accounts/login/')
def memo_delete(request, pk):
    memo = Memo.objects.get(pk=pk)
    memo.delete()
    return HttpResponseRedirect(reverse('memoapp:list'))