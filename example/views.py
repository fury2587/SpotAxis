# -*- coding: utf-8 -*-

import random
from django.contrib import messages

from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from django.template import RequestContext


def test(request):
    # if request.method == 'POST':
    #     form = BasicSearchVacancyForm(data=request.POST, files=request.FILES, industry_selected=industry_selected)
    #     if form.is_valid():
    #         return redirect('vacancies_first_search_vacancies')
    # else:
    #     form = BasicSearchVacancyForm()

    return render_to_response('test.html',
                              {'isIndex': True,
                               },
                              context_instance=RequestContext(request))