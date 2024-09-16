from django.contrib import admin
from .models import Declaration,Company
from unfold.admin import ModelAdmin

# Register your models here.

@admin.register(Company)
class CompanyAdmin(ModelAdmin):
    ordering = ["-created_at"]


@admin.register(Declaration)
class DeclarationAdmin(ModelAdmin):
    ordering = ["-created_at"]
