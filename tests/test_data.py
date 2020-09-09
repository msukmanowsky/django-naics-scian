import os
from pathlib import Path

from naics_scian.data import read_naics_csv

BASE_DIR = Path(__file__).resolve().parent


def test_read_naics_csv():
    classifications = list(read_naics_csv())
    assert len(classifications) == 2079

    classification = classifications[0]
    assert classification.level == 1
    assert classification.structure == "Sector"
    assert classification.parent_code is None
    assert classification.class_title == "Agriculture, forestry, fishing and hunting"
    assert classification.superscript == ""
