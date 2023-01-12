from LocatorsPage.Carrierlocator import Carrier_locators
from Utilities.Utiles import Utiles
from LocatorsPage import Carrierlocator


class CarrierPage(object):

    def __init__(self, context):
        context = context

    def click_carrier(self, context):
        carrierLocators = Carrier_locators()
        utiles = Utiles()
        utiles.performclick(context, carrierLocators.carrier_xpath)
        return self

    def click_add_carrier(self, context):
        carrierLocators = Carrier_locators()
        utiles = Utiles()
        utiles.performclick(context, carrierLocators.Add_carrier_xpath)
        return self
