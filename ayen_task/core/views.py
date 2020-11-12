from django.views.generic.edit import CreateView
from django.views.generic import FormView

from ayen_task.core.models import Document
from ayen_task.core.forms import DocumentForm


class Search(FormView):
    pass


class Upload(CreateView):
    model = Document
    fields = ["name", "file"]
    success_url = "/"
    template_name = "upload.html"
