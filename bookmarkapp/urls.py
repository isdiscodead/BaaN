from django.conf.urls import url
from django.contrib.auth import admin
from django.urls import path

from bookmarkapp import views
from bookmarkapp.views import BookmarkListView

app_name = 'bookmarkapp'

urlpatterns = [
    path('list/', BookmarkListView.as_view(template_name='bookmarkapp/list.html'), name='list'),
    path('create/', views.bookmark_create, name='create'),
]