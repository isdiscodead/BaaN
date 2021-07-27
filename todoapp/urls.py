from django.urls import path

from todoapp.views import TodoListView, TodoCreateView

app_name = 'todoapp'

urlpatterns = [
    path('list/', TodoListView.as_view(), name='list'),
    path('create/', TodoCreateView.as_view(), name='create'),
    # path('update/<int:pk>', TodoUpdateView.as_view(), name='update'),
    # path('delete/<int:pk>', TodoDeleteView.as_view(), name='delete'),
]