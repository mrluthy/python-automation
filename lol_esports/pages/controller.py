"""Controller that holds all the page objects.

Each website consists of pages and these pages are "controlled"
or centralized using a Page Controller. This not only increases readability,
but it also simplifies usage of the Page Objects.

Classes
--------
* Pages

Usage
------
Each completed Page Object Model (POM) should be
added as a property of the Pages class.

code-example::
  1 def test_using_page_controller(self):
  2     pages = Pages()
  3     pages.home.goto()
  4     pages.league.goto("NA LCS")  
  5     assert pages.league.map.schedule_tab.is_displayed

code-example::
  1 def test_without_page_controller(self):
  2     home = HomePage(driver)
  3     home.goto()
  4     league = LeaguePage(driver)
  5     league.goto("NA LCS")    
  6     assert league.map.schedule_tab.is_displayed
"""

__author__ = "Carlos Kidman"


from lol_esports.pages.home import HomePage
from lol_esports.pages.league import LeaguePage
from lol_esports.pages.teamstandings import TeamStandingsPage
from lol_esports.pages.universe import Universe


class Pages:
    """The Pages controller for LOL Esports.
    
    Arguments
    ----------
    * driver (Driver): Driver instance to be used by the controller's pages.
    """
    def __init__(self, driver):
        self._home = HomePage(driver)
        self._league = LeaguePage(driver)
        self._teamstandings = TeamStandingsPage(driver)
        self._universe = Universe(driver)

    @property
    def home(self):
        return self._home

    @property
    def league(self):
        return self._league

    @property
    def teamstandings(self):
        return self._teamstandings

    @property
    def universe(self):
        return self._universe
