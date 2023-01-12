from LocatorsPage.Dashboardlocator import Dashboard_locators
from Utilities.Utiles import Utiles
from LocatorsPage import Dashboardlocator


class DashboardPage(object):

    def __init__(self, context):
        context = context

    def click_manage_button(self, context):
        dashboardLocators = Dashboard_locators()
        utiles = Utiles()
        utiles.performclick(context, dashboardLocators.button_manage_xpath)
        return self


