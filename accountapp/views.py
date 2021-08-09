from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your models here.
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, RedirectView, ListView

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountCreationForm, AccountLoginForm

has_ownership = [account_ownership_required, login_required(login_url='/accounts/login/')]


# BaaN 메인 페이지
@method_decorator(login_required(login_url='/accounts/login/'), 'get')
class AccountMainView(ListView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/index.html'


########################################


class AccountCreateView(CreateView):
    model = User
    form_class = AccountCreationForm
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/create.html'


class AccountLoginView(LoginView):
    template_name = 'accountapp/login.html'
    form_class = AccountLoginForm


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'


def search(request):
    engine = request.GET.get('engine')
    query = request.GET.get('query')
    query = query.replace(' ', '+')

    if engine == 'google':
        url = "https://www.google.com/search?q="
    elif engine == 'naver':
        url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query="
    else:
        url = "https://www.youtube.com/results?search_query="

    url += query
    return HttpResponseRedirect(url)