import argparse
import csv
import os
import pathlib

from django.core.management.base import BaseCommand, CommandError

from naics_scian.models import NAICSClassification
from naics_scian.data import seed_database

BASE_DIR = pathlib.Path(__file__).resolve().parent


class Command(BaseCommand):
    help = "Loads data from a NAICS csv file"

    def add_arguments(self, parser: argparse.ArgumentParser):
        parser.add_argument("csvinput")
        parser.add_argument(
            "--clear", help="Clear the table first before loading", action="store_true"
        )

    def handle(self, *args, **options):
        if options["clear"]:
            NAICSClassification.objects.all().delete()

        path = os.path.abspath(
            os.path.join(BASE_DIR, "..", "..", "NAICS-SCIAN-2017-Structure-V1-eng.csv")
        )
        seed_database(path)
