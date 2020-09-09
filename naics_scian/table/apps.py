from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TableConfig(AppConfig):
    name = "naics_scian.table"
    verbose_name = _("North American Industry Classification System")
