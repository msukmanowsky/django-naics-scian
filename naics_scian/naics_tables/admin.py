from django.contrib import admin
from naics_scian.naics_tables.models import NAICSClassification


@admin.register(NAICSClassification)
class NAICSClassificationAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "structure",
        "class_title",
    )
    readonly_fields = (
        "level",
        "structure",
        "code",
        "class_title",
        "superscript",
        "class_definition",
        "parent",
    )
    list_filter = (
        "level",
        "structure",
    )
    search_fields = (
        "class_title",
        "class_definition",
    )

    def has_add_permission(self, request, obj=None):
        return False
