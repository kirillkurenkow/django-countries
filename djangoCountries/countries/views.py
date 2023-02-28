from django.shortcuts import render
from django.http import HttpRequest
from django.core.paginator import Paginator
from .models import *


def index(request: HttpRequest):
    return render(request, 'countries/index.html', {'title': 'Главная'})


def countries_list(request: HttpRequest):
    countries = Country.objects.all()
    paginator = Paginator(countries, 10)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    return render(request, 'countries/countries_list.html', {
        'countries': countries,
        'title': 'Список стран',
        'alphabet': 'ABCDEFGHUJKLMNOPQRSTUVWXYZ',
        'page_object': page_object,
    })


def countries_list_alphabet(request: HttpRequest, char: str,):
    countries = [x for x in Country.objects.all() if x.name.startswith(char)]
    return render(request, 'countries/countries_list_alphabet.html', {
        'countries': countries,
        'title': f'Список стран на букву {char}'
    })


def country_info(request: HttpRequest, country: str):
    languages_ = Country.objects.get(name=country).languages.all()
    return render(request, 'countries/country_info.html', {
        'country': country,
        'languages': languages_,
        'title': country,
    })


def languages(request: HttpRequest):
    languages_ = Language.objects.all()
    return render(request, 'countries/languages.html', {
        'title': 'Языки',
        'languages': languages_
    })


def language_info(request: HttpRequest, language: str):
    countries = Country.objects.filter(languages__language=language)
    return render(request, 'countries/language_info.html', {
        'title': language,
        'countries': countries,
        'language': language,
    })
