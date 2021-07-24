from django.conf.urls import url
from django.contrib.auth import admin
from django.urls import path

from bookmarkapp import views
from bookmarkapp.views import bookmarkListView

app_name = 'bookmarkapp'

urlpatterns = [
    path('list/', bookmarkListView.as_view(template_name='bookmarkapp/list.html'), name='list'),

]