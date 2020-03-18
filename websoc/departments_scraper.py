from typing import Dict

from bs4 import BeautifulSoup
import requests

import utils.db as db
import websoc.settings as websoc
from models.departments_model import DepartmentsModel


def _scrape() -> [Dict]:
    source = requests.get(websoc.URL, headers={"User-Agent": websoc.USER_AGENT}).content
    soup = BeautifulSoup(source, "lxml")
    depts = []

    dept_select = soup.find("select", {"name": "Dept"})
    for option in dept_select.find_all("option"):
        depts.append({"value": option["value"], "text": option.text})

    return depts


def _save_to_db(departments: [Dict]) -> None:
    db.clear_all(DepartmentsModel)
    models = [DepartmentsModel(**dept) for dept in departments]
    db.save_list(models)


def update_departments() -> None:
    _save_to_db(_scrape())
