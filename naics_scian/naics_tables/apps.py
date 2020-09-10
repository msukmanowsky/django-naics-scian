from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class NAICSTablesConfig(AppConfig):
    name = "naics_scian.naics_tables"
    verbose_name = _("North American Industry Classification System")
