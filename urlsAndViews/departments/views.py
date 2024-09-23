import json
from django.urls import reverse, reverse_lazy

from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect

from urlsAndViews.departments.models import Department


def index(request):
    return HttpResponse(f'<h1>Hello World</h1>')


def view_with_name(request, variable): # named same way as in urls
    # return HttpResponse(f'<h1>Variable: {variable}</h1>')
    return render(request, 'departments/name_template.html', {'variable': variable})
def view_with_int_pk(request, pk):
    # return HttpResponse(json.dumps({"pk": pk}), content_type="application/json")
    return JsonResponse({"pk": pk})
def view_with_slug(request, pk, slug):
    # department = Department.objects.filter(pk=pk, slug=slug)
    #
    # if not department:
    #     raise Http404

    # OPTION 2
    department = get_object_or_404(Department, pk=pk, slug=slug)

    return HttpResponse(f'<h1>Department from slug: {department}</h1>')

def show_archive(request, archive_year):
    return HttpResponse(f'<h1>The year is: {archive_year}</h1>')

def redirect_to_softuni(request):
    return redirect('https://softuni.bg')

def redirect_to_view(request):
    return redirect('home')