# from django.shortcuts import render
#
# # Create your views here.
from django.views.generic import ListView

from bookmarkapp.models import Bookmark
#
# def home(request):
#     urlList = Bookmark.objects.order_by("title")
#     urlCount = Bookmark.objects.all().count()
#
#     return render("list.html", {"urlList":urlList, "urlCount":urlCount})

class bookmarkListView(ListView):
    model = Bookmark
    context_object_name = 'bookmark_list'
    template_name = 'bookmarkapp/list.html'