from django.contrib import admin
from .models import Declaration,Company

# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    ordering = ["-created_at"]


@admin.register(Declaration)
class DeclarationAdmin(admin.ModelAdmin):
    ordering = ["-created_at"]
