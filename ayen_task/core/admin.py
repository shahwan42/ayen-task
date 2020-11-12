from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib import admin
from .models import Document

User = get_user_model()


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("name", "file")


admin.site.unregister(Group)
admin.site.unregister(User)
