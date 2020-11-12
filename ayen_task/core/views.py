from django.http import request
from ayen_task.core.forms import DocumentForm
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import FormView


class Home(TemplateView):
    template_name = "home.html"
