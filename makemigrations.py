#!/usr/bin/env python3
import os
import sys

from django.core.management import execute_from_command_line

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    args = sys.argv + ["makemigrations", "naics_scian", "naics_tables"]
    execute_from_command_line(args)
