from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, DeleteView, ListView, UpdateView

from memoapp.forms import MemoForm
from memoapp.models import Memo

def memo_create(request):
    form = MemoForm(request.POST)
    if form.is_valid():
        title = request.POST.get('title')
        content = request.POST.get('content')
        user = request.user
        return redirect("home")
    return render(request, "snippets/memo_create.html", {"form": form})


# class MemoCreateView(CreateView):
#     model = Memo
#     form_class = MemoForm
#     # template_name = 'snippets/memo_create.html'
#
#     def get_success_url(self):
#         return reverse('memoapp:list')


class MemoUpdateView(UpdateView):
    model = Memo
    context_object_name = 'target_memo'
    form_class = MemoForm
    template_name = 'memoapp/update.html'

    def get_success_url(self):
        return reverse('memoapp:detail', kwargs={'pk': self.object.pk})

class MemoDetailView(DetailView):
    model = Memo
    form_class = MemoForm
    context_object_name = 'target_memo'
    template_name = 'memoapp/detail.html'

class MemoDeleteView(DeleteView):
    model = Memo
    context_object_name = 'target_memo'
    success_url = reverse_lazy('memoapp:list')
    template_name = 'memoapp/delete.html'

class MemoListView(ListView):
    model = Memo
    context_object_name = 'memo_list'
    template_name = 'memoapp/list2.html'
    paginate_by = 5

def memo_delete(request, pk):
    memo = Memo.objects.get(id=pk)
    memo.delete()
    return HttpResponseRedirect(reverse('memoapp:list'))