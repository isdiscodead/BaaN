# from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, CreateView

from bookmarkapp.forms import BookmarkCreationForm
from bookmarkapp.models import Bookmark

# 북마크에서 사용할 favicon과 title을 가져오기 위한 크롤링 모듈
from urllib.request import urlopen
from bs4 import BeautifulSoup
from django.core.validators import URLValidator


class BookmarkListView(ListView):
    model = Bookmark
    context_object_name = 'bookmark_list'
    template_name = 'bookmarkapp/list.html'


def bookmark_create(request):
    url = request.POST.get('url')
    title = request.POST.get('title')
    new_bookmark = Bookmark()
    validator = URLValidator()

    try:
        validator(url)  # url 유효성 검사

        new_bookmark.url = url
        new_bookmark.title = title
        new_bookmark.save()

    except ValidationError as exception:
        # URL is NOT valid here.
        print(exception)

    return HttpResponseRedirect(reverse('bookmarkapp:list'))

    #
    # # 이미지와 타이틀 가져오기
    # html = urlopen("https://hellogk.tistory.com/37")
    # bsObject = BeautifulSoup(html, "html.parser")
    #
    # if not model.title:
    #     title = bsObject.find("title").text

