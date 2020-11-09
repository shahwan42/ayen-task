from django.shortcuts import render
from django.views.generic.base import View


class FileView(View):
    def get(self, request, **kwargs):
        return render(request, "core/file.html")

    def post(self, request, **kwargs):
        return render(request, "core/file.html")
