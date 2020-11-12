import os
from django.core.exceptions import ValidationError
from django.db import models


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = [".pdf", ".pptx"]
    if ext.lower() not in valid_extensions:
        raise ValidationError("Only `pdf` or `pptx` documents.")


class Document(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to="uploads", validators=[validate_file_extension])
