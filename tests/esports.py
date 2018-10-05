"""LOL Esports Tests.

pytest.fixture docs:
    "https://docs.pytest.org/en/latest/fixture.html#fixture"

Run tests:
    $ pytest tests/esports.py

Run tests in parallel:
    $ pytest tests/esports.py --workers 2
"""


import pytest
from framework.drivercore.driver import Driver
from lol_esports.data import esports_api as api
from lol_esports.pages.controller import Pages



@pytest.fixture
def setup():
    driver = Driver("chrome")
    pages = Pages(driver)
    yield driver, pages
    driver.quit()


# def test_esports_pages(setup):
#     driver, pages = setup
#     driver.goto("https://www.lolesports.com")
#     pages.league.goto("EU LCS")
#     assert driver.title == "Schedule | LoL Esports"


# def test_each_teams_standings_displayed(setup):
#     driver, pages = setup
#     driver.goto("https://www.lolesports.com")
#     pages.league.goto("NA LCS")
#     pages.teamstandings.goto()
#     pages.teamstandings.select_stage_by_name("Regular Season")
    
#     for api_team in pages.teamstandings.get_teams_from_api():
#         team = pages.teamstandings.find_regseason_team(api_team["name"])
#         assert team.is_displayed

def test_each_champion(setup):
    driver, pages = setup
    driver.goto("https://www.lolesports.com")
    pages.universe