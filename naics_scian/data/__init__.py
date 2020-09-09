import csv
import logging
import os
from collections import namedtuple
from pathlib import Path
from typing import Dict, Iterator, List, Optional, Type

from django.db import models

log = logging.getLogger(__name__)


NAICSClassificationRow = namedtuple(
    "NAICSClassificationRow",
    [
        "level",
        "structure",
        "parent_code",
        "code",
        "class_title",
        "superscript",
        "class_definition",
    ],
)

BASE_DIR = Path(__file__).resolve().parent


def read_naics_csv(
    path: Optional[str] = None, encoding="ISO-8859-1"
) -> Iterator[NAICSClassificationRow]:
    """Load a NAICS CSV data file like those obtained from https://www.statcan.gc.ca/eng/subjects/standard/naics/2017/index"""
    if path is None:
        path = os.path.join(BASE_DIR, "NAICS-SCIAN-2017-Structure-V1-eng.csv")
    with open(path, encoding=encoding) as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            level = int(row["Level"])
            kwargs = dict(
                level=level,
                structure=row["Hierarchical structure"],
                class_title=row["Class title"],
                superscript=row["Superscript"],
                class_definition=row["Class definition"],
            )
            if "-" in row["Code"]:
                start, stop = row["Code"].split("-")
                for i in range(int(start), int(stop) + 1):
                    code = str(i)
                    if level == 1:
                        kwargs["parent_code"] = None
                    else:
                        kwargs["parent_code"] = code[:level]

                    yield NAICSClassificationRow(code=str(i), **kwargs)
            else:
                if level == 1:
                    kwargs["parent_code"] = None
                else:
                    kwargs["parent_code"] = row["Code"][:level]

                yield NAICSClassificationRow(code=row["Code"], **kwargs)


def seed_database(
    csv_path: Optional[str] = None,
    encoding: str = "ISO-8859-1",
    Model: Optional[Type[models.Model]] = None,
):
    if Model is None:
        from naics_scian.models import NAICSClassification as Model

    rows = list(read_naics_csv(csv_path, encoding=encoding))
    n_levels = max(row.level for row in rows)
    for level in range(1, n_levels + 1):
        # Create one level at a time so foreign key relationships work
        log.info(f"Loading level {level} classifications...")
        level_rows = [row for row in rows if row.level == level]
        kwargs = row._asdict()
        kwargs["parent_id"] = kwargs.pop("parent_code")
        classifications = [Model(**kwargs) for row in level_rows]
        Model.objects.bulk_create(classifications)
