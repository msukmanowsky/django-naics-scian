from django.db import models
from django.utils.translation import gettext_lazy as _


class NAICSClassification(models.Model):
    class Structure(models.TextChoices):
        SECTOR = "Sector", _("Sector")
        SUBSECTOR = "Subsector", _("Subsector")
        INDUSTRY_GROUP = "Industry group", _("Industry Group")
        INDUSTRY = "Industry", _("Industry")
        CANADIAN_INDUSTRY = "Canadian industry", _("Canadian Industry")

    class Superscript(models.TextChoices):
        CAN = "CAN", _("CAN")  # Canadian class only
        US = "US", _("US")  # Canadian and United States classes are comparable
        MEX = "MEX", _("MEX")  # Canadian and Mexican classes are comparable

    code = models.CharField(
        max_length=10, help_text="Code for the classification", primary_key=True
    )
    parent = models.ForeignKey(
        "self",
        default=None,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        help_text="Parent classification (null if top-level)",
    )
    level = models.PositiveIntegerField(help_text="Nesting level in the hierarchy")
    structure = models.CharField(
        max_length=17, choices=Structure.choices, help_text="Corresponding structure"
    )
    class_title = models.CharField(max_length=200)
    superscript = models.CharField(
        max_length=3,
        choices=Superscript.choices,
        blank=True,
        help_text="Used to signify comparability",
    )
    class_definition = models.TextField()

    class Meta:
        verbose_name = "NAICS Classification"
        ordering = ("code",)

    def __str__(self):
        return f"{self.code}: {self.class_title}"
