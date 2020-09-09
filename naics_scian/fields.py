from django.db import models

from naics_scian.data import read_naics_csv

CHOICES = [(row.code, row.class_title) for row in read_naics_csv()]


class NAICSCodeField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 10
        kwargs["choices"] = CHOICES
        kwargs.setdefault("blank", True)
        kwargs.setdefault("null", True)
        super().__init__(*args, **kwargs)
