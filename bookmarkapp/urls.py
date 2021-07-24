from django.conf.urls import url
from django.contrib.auth import admin
from django.urls import path

from bookmarkapp import views
from bookmarkapp.views import BookmarkListView, BookmarkCreateView

app_name = 'bookmarkapp'

urlpatterns = [
    path('list/', BookmarkListView.as_view(template_name='bookmarkapp/list.html'), name='list'),
    path('create/', BookmarkCreateView.as_view(template_name='snippets/bookmark_create.html'), name='create'),
]