# from django.shortcuts import render
import ssl

from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, CreateView

from bookmarkapp.forms import BookmarkCreationForm
from bookmarkapp.models import Bookmark

# 북마크에서 사용할 title을 가져오기 위한 크롤링 모듈
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

        # 타이틀 가져오기
        context = ssl._create_unverified_context()
        html = urlopen(url, context=context)
        bs_object = BeautifulSoup(html, "html.parser")

        if not title:
            title = bs_object.find("title").text

        # DB 등록
        new_bookmark.url = url
        new_bookmark.title = title
        new_bookmark.favicon_url = "http://www.google.com/s2/favicons?domain_url=" + url
        new_bookmark.save()

    except ValidationError as exception:
        # URL is NOT valid here.
        print(exception)

    return HttpResponseRedirect(reverse('bookmarkapp:list'))


