# What is this?

A Django app that adds a table for the [Canadian version of the North American Industry Classification System](https://www.statcan.gc.ca/eng/subjects/standard/naics/2017/index). Handy when you want a standardized list of


# Installation

```
$ pip install git+https://github.com/msukmanowsky/django-naics-scian@master
```

# Usage

Add to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    # ...
    "naics_scian",
]
```

Migrate:

```
$ python manage.py migrate
```

Note that this initial migration will also seed your database with the
[Statistics Canada NAICS 2017 list](https://www.statcan.gc.ca/eng/subjects/standard/naics/2017/index).

## As a field

```python
from naics_scian.fields import NAICSCodeField

class MyModel(models.Model):

    industry = NAICSCodeField()
```


## As a table

Add an additional app to your `INSTALLED_APPS`:

```python
# settings.py

INSTALLED_APPS = [
    # ...
    "naics_scian",
    "naics_scian.table",
]
```

Add as a `ForeignKey` to your models:

```python
from django.db import models

class MyModel(models.Model):

    industry = ForeignKey(
        "naics_scian.NAICSClassification",
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

```

# Developing

Clone the repo:

```
git clone https://github.com/msukmanowsky/django-naics-scian
```

## Testing

To run tests after cloning the repo, run:

```
python3 -m venv env
source env/bin/activate
pip install django
pip install -r requirements.txt
pytest
```
