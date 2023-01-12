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

    def input_name_field(self, enterdata, context):
        carrierLocators = Carrier_locators()
        utiles = Utiles()
        utiles.performsendkeys(context, carrierLocators.Blank_field_name_xpath, enterdata)
        return self

    def input_parcel_field(self, enterdata, context):
        carrierLocators = Carrier_locators()
        utiles = Utiles()
        utiles.performsendkeys(context, carrierLocators.Omni_parcel_id_xpath, enterdata)
        return self

    def input_parcel_name(self, enterdata, context):
        carrierLocators = Carrier_locators()
        utiles = Utiles()
        utiles.performsendkeys(context, carrierLocators.Omni_parcel_name_xpath, enterdata)
        return self

    def click_hub_checkbox(self, context):
        carrierLocators = Carrier_locators()
        utiles = Utiles()
        utiles.performclick(context, carrierLocators.Hub_checkbox_xpath)
        return self
