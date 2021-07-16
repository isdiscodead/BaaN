# from django.shortcuts import render
#
# # Create your views here.
# from bookmarkapp.models import Bookmark
#
# def home(request):
#     urlList = Bookmark.objects.order_by("title")
#     urlCount = Bookmark.objects.all().count()
#
#     return render("list.html", {"urlList":urlList, "urlCount":urlCount})