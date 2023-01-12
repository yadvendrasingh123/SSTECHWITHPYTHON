from LocatorsPage.Hublocator import Hub_locators
from Utilities.Utiles import Utiles
from LocatorsPage import Hublocator


class HubPage(object):

    def __init__(self, context):
        context = context

    def Click_hub(self, context):
        hubLocators = Hub_locators()
        utiles = Utiles()
        utiles.performclick(context, hubLocators.hub_button_xpath)
        return self

    def click_hub_add(self, context):
        hubLocators = Hub_locators()
        utiles = Utiles()
        utiles.performclick(context, hubLocators.add_hub_button_xpath)
        return self

    def input_company_name(self, context):
        hubLocators = Hub_locators()
        utiles = Utiles()
        utiles.performclick(context, hubLocators.hub_company_name_xpath)
        return self

    def test_return(self, context):
        hubLocators = Hub_locators()
        utiles = Utiles()
        utiles.performclick(context, hubLocators.company_hub_test_return_xpath)
        return self

    def input_name(self, enterdata, context):
        hubLocators = Hub_locators()
        utiles = Utiles()
        utiles.performsendkeys(context, hubLocators.name_xpath,enterdata)
        return self

    def input_description(self,enterdata, context):
        hubLocators = Hub_locators()
        utiles = Utiles()
        utiles.performsendkeys(context, hubLocators.description_xpath,enterdata)
        return self

    def input_building(self,enterdata, context):
        hubLocators = Hub_locators()
        utiles = Utiles()
        utiles.performsendkeys(context, hubLocators.Building_xpath,enterdata)
        return self

    def input_address(self,enterdata, context):
        hubLocators = Hub_locators()
        utiles = Utiles()
        utiles.performsendkeys(context, hubLocators.Address_street_xpath,enterdata)
        return self

    def input_country(self,enterdata, context):
        hubLocators = Hub_locators()
        utiles = Utiles()
        utiles.performsendkeys(context, hubLocators.Country_xpath,enterdata)
        return self

    def input_Suburub(self,enterdata, context):
        hubLocators = Hub_locators()
        utiles = Utiles()
        utiles.performsendkeys(context, hubLocators.suburub_xpath,enterdata)
        return self

    def input_city(self,enterdata, context):
        hubLocators = Hub_locators()
        utiles = Utiles()
        utiles.performsendkeys(context, hubLocators.city_xpath,enterdata)
        return self

    def inputpostcode(self,enterdata, context):
        hubLocators = Hub_locators()
        utiles = Utiles()
        utiles.performsendkeys(context, hubLocators.postcode_xpath,enterdata)
        return self

    def email(self,enterdata, context):
        hubLocators = Hub_locators()
        utiles = Utiles()
        utiles.performsendkeys(context, hubLocators.email_xpath, enterdata)
        return self

    def serviceable(self, context):
        hubLocators = Hub_locators()
        utiles = Utiles()
        utiles.performclick(context, hubLocators.serviceable_countries_xpath)
        return self

    def submit(self, context):
        hubLocators = Hub_locators()
        utiles = Utiles()
        utiles.performclick(context, hubLocators.submit_xpath)
        return self












