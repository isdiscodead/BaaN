# from django.shortcuts import render

from django.views.generic import ListView, CreateView

from bookmarkapp.forms import BookmarkCreationForm
from bookmarkapp.models import Bookmark

# 북마크에서 사용할 favicon과 title을 가져오기 위한 크롤링 모듈
from urllib.request import urlopen
from bs4 import BeautifulSoup


class BookmarkListView(ListView):
    model = Bookmark
    context_object_name = 'bookmark_list'
    template_name = 'bookmarkapp/list.html'


class BookmarkCreateView(CreateView):
    model = Bookmark
    context_object_name = 'target_bookmark'
    form_class = BookmarkCreationForm
    template_name = 'snippets/bookmark_create.html'

    #
    # # 이미지와 타이틀 가져오기
    # html = urlopen("https://hellogk.tistory.com/37")
    # bsObject = BeautifulSoup(html, "html.parser")
    #
    # if not model.title:
    #     title = bsObject.find("title").text

