import os
from pathlib import Path

from naics_scian.data import read_naics_csv

BASE_DIR = Path(__file__).resolve().parent


def test_read_naics_csv():
    path = os.path.abspath(
        os.path.join(
            BASE_DIR,
            "..",
            "naics_scian",
            "data",
            "NAICS-SCIAN-2017-Structure-V1-eng.csv",
        )
    )
    classifications = list(read_naics_csv(path))
    assert len(classifications) == 2079

    classification = classifications[0]
    assert classification.level == 1
    assert classification.structure == "Sector"
    assert classification.parent_code is None
    assert classification.class_title == "Agriculture, forestry, fishing and hunting"
    assert classification.superscript == ""
