from framework.drivercore import by
from framework.drivercore import waitconditions as conditions
from lol_esports.pages.pagebase import PageBase
from lol_esports.data import esports_api as api
from lol_esports.pages.universe import Universe

class Champions:
    def __init__(self, driver):
        self._driver = driver
    
    @property
    def goto_champions_tab (self):
        Universe
        