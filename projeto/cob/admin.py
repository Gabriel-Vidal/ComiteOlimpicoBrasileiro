from django.contrib import admin

from .models import Competicao


class CompeticaoAdmin(admin.ModelAdmin):
    ...


admin.site.register(Competicao, CompeticaoAdmin)
