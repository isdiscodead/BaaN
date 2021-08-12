from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView, UpdateView, CreateView

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

    def get_success_url(self):
        return reverse('memoapp:list')

class MemoListView(ListView):
    model = Memo
    context_object_name = 'memo_list'
    template_name = 'memoapp/list.html'
    paginate_by = 5

def memo_delete(request, pk):
    memo = Memo.objects.get(id=pk)
    memo.delete()
    return HttpResponseRedirect(reverse('memoapp:list'))

def memo_detail(request, pk):
    memo = Memo.objects.get(id=pk)

    return HttpResponseRedirect(reverse('memoapp:list'))

# class MemoDetailView(DetailView):
#     model = Memo
#     form_class = MemoForm
#     context_object_name = 'target_memo'

def memo_update(request):
    form = MemoForm(request.POST)
    if form.is_valid():
        title = request.POST.get('title')
        content = request.POST.get('content')
        user = request.user
        return redirect("home")
    return render(request, "memoapp/create.html", {"form": form})

# class MemoUpdateView(UpdateView):
#     model = Memo
#     context_object_name = 'target_memo'
#     form_class = MemoForm
#
#     def get_success_url(self):
#         return reverse('memoapp:detail', kwargs={'pk': self.object.pk})