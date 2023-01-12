from LocatorsPage.Retailerlocator import Retailer_locators
from Utilities.Utiles import Utiles
from LocatorsPage import Retailerlocator


class RetailerPage(object):

    def __init__(self, context):
        context = context

    def click_Retailer(self, context):
        retailerlocators = Retailer_locators()
        utiles = Utiles()
        utiles.performclick(context, retailerlocators.retailer_xpath)
        return self
    
    def click_Add_retiler(self, context):
        retailerlocators = Retailer_locators()
        utiles = Utiles()
        utiles.performclick(context, retailerlocators.Add_retailer_xpath)
        return self

    def click_company(self, context):
        retailerlocators = Retailer_locators()
        utiles = Utiles()
        utiles.performclick(context, retailerlocators.companys_xpath)
        return self

    def click_choose_file(self, context):
        retailerlocators = Retailer_locators()
        utiles = Utiles()
        utiles.performclick(context, retailerlocators.Choose_file_xpath)
        return self

    def click_field(self, enterdata, context):
        retailerlocators = Retailer_locators()
        utiles = Utiles()
        utiles.performsendkeys(context, retailerlocators.number_return_product_xpath, enterdata)
        return self

    def input_name_field(self, enterdata, context):
        retailerlocators = Retailer_locators()
        utiles = Utiles()
        utiles.performsendkeys(context, retailerlocators.first_name_xpath, enterdata)
        return self
