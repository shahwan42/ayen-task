from django.views.generic.edit import CreateView
from django.views.generic import FormView
from django.views.generic.list import ListView

from ayen_task.core.forms import SearchForm
from ayen_task.core.models import Document


class Home(ListView):
    model = Document
    template_name = "home.html"


class Search(FormView):
    form_class = SearchForm
    template_name = "search.html"


class Upload(CreateView):
    model = Document
    fields = ["name", "file"]
    success_url = "/"
    template_name = "upload.html"
