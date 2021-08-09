from django.conf.urls import url
from django.urls import path

from memoapp import views
from memoapp.views import MemoDetailView, MemoDeleteView, MemoListView, MemoUpdateView

# MemoListView, MemoCreateView, MemoDetailView, MemoUpdateView, MemoDeleteView

app_name = 'memoapp'


urlpatterns = [
    path('list/', MemoListView.as_view(), name='list'),
    path('create/', views.memo_create, name='create'),
    # path('create/', MemoCreateView.as_view(), name='create'),
    path('detail/<int:pk>', views.MemoDetailView, name='detail'),
    path('update/<int:pk>', MemoUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.memo_delete, name='delete'),
]