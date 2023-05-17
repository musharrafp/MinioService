from django.shortcuts import render
from django.views.generic import CreateView
from apps.models import Document
from apps.forms import DocForm


class Doc(CreateView):
    model = Document
    form_class = DocForm
    template_name = 'html.html'
