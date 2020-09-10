from django.db import models

from naics_scian.data import read_naics_csv

classifications = list(read_naics_csv())


def make_choices(classifications):
    return [
        (
            row.code,
            f"{row.code}: {row.structure} / {row.class_title}"
            + (f" ({row.superscript})" if row.superscript else ""),
        )
        for row in classifications
    ]


ALL_CODE_CHOICES = make_choices(classifications)

SECTOR_CODE_CHOICES = make_choices(
    [c for c in classifications if c.structure == "Sector"]
)

INDUSTRY_CODE_CHOICES = make_choices(
    [
        c
        for c in classifications
        if c.structure == "Industry" or c.structure == "Canadian industry"
    ]
)


class NAICSCodeField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 10
        kwargs["choices"] = ALL_CODE_CHOICES
        if "help_text" not in kwargs:
            kwargs[
                "help_text"
            ] = "NAICS code for all structures (sectors, subsectors, industry groups and industries)"
        super().__init__(*args, **kwargs)


class NAICSSectorCodeField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 10
        kwargs["choices"] = SECTOR_CODE_CHOICES
        if "help_text" not in kwargs:
            kwargs["help_text"] = "NAICS code for sectors only"
        super().__init__(*args, **kwargs)


class NAICSIndustryCodeField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 10
        kwargs["choices"] = INDUSTRY_CODE_CHOICES
        if "help_text" not in kwargs:
            kwargs[
                "help_text"
            ] = "NAICS code for industries only (Industry or Canadian Industry)"
        super().__init__(*args, **kwargs)
