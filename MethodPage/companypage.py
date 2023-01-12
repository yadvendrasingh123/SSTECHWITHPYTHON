from LocatorsPage.Companylocator import Company_locators
from Utilities.Utiles import Utiles
from LocatorsPage import Companylocator


class CompanyPage(object):

    def __init__(self, context):
        context = context

    def click_company(self, context):
        companyLocators = Company_locators()
        utiles = Utiles()
        utiles.performclick(context, companyLocators.companies_xpath)
        return self

    def click_Add_company(self, context):
        companyLocators = Company_locators()
        utiles = Utiles()
        utiles.performclick(context, companyLocators.addcompany_xpath)
        return self

    def Company_name_field(self, enterdata, context):
        companyLocators = Company_locators()
        utiles = Utiles()
        utiles.performsendkeys(context, companyLocators.Company_name_xpath, enterdata)
        return self

    def Country_field(self, enterdata, context):
        companyLocators = Company_locators()
        utiles = Utiles()
        utiles.performsendkeys(context, companyLocators.Country_xpath, enterdata)
        return self

    def Building_name_field(self, enterdata, context):
        companyLocators = Company_locators()
        utiles = Utiles()
        utiles.performsendkeys(context, companyLocators.Building_name_xpath, enterdata)
        return self

    def Street_Address_field(self, enterdata, context):
        companyLocators = Company_locators()
        utiles = Utiles()
        utiles.performsendkeys(context, companyLocators.Street_name_xpath, enterdata)
        return self

    def Suburb_field(self, enterdata, context):
        companyLocators = Company_locators()
        utiles = Utiles()
        utiles.performsendkeys(context, companyLocators.Suburb_xpath, enterdata)
        return self

    def State_field(self, enterdata, context):
        companyLocators = Company_locators()
        utiles = Utiles()
        utiles.performsendkeys(context, companyLocators.State_xpath, enterdata)
        return self

    def Postal_code(self, enterdata, context):
        companyLocators = Company_locators()
        utiles = Utiles()
        utiles.performsendkeys(context, companyLocators.Postal_code_xpath, enterdata)
        return self

    def Contact_number(self, enterdata, context):
        companyLocators = Company_locators()
        utiles = Utiles()
        utiles.performsendkeys(context, companyLocators.Contact_number_xpath, enterdata)
        return self

    def Email_field(self, enterdata, context):
        companyLocators = Company_locators()
        utiles = Utiles()
        utiles.performsendkeys(context, companyLocators.Email_xpath, enterdata)
        return self

    def Return_portal_Domain(self, enterdata, context):
        companyLocators = Company_locators()
        utiles = Utiles()
        utiles.performsendkeys(context, companyLocators.Return_Portal_Domain_xpath, enterdata)
        return self

    def Site_url(self, enterdata, context):
        companyLocators = Company_locators()
        utiles = Utiles()
        utiles.performsendkeys(context, companyLocators.Site_Url_xpath, enterdata)
        return self

    def click_Submit_button(self, context):
        companyLocators = Company_locators()
        utiles = Utiles()
        utiles.performclick(context, companyLocators.Submit_button_xpath)
        return self

    def click_change_logo(self, context):
        companyLocators = Company_locators()
        utiles = Utiles()
        utiles.performclick(context, companyLocators.company_change_logo_xpath)
        return self

    def click_Company_search_field(self, context):
        companyLocators = Company_locators()
        utiles = Utiles()
        utiles.performclick(context, companyLocators.Company_search_button_xpath)
        return self

    def field_Test_Return(self, context):
        companyLocators = Company_locators()
        utiles = Utiles()
        utiles.performclick(context, companyLocators.Search_Test_Return_xpath)
        return self

    def click_Change_type_field(self, context):
        companyLocators = Company_locators()
        utiles = Utiles()
        utiles.performclick(context, companyLocators.Change_type_field_xpath)
        return self

    def click_dropdown_add_type(self, context):
        companyLocators = Company_locators()
        utiles = Utiles()
        utiles.performclick(context, companyLocators.Add_type_xpath)
        return self

    def click_Search_button(self, context):
        companyLocators = Company_locators()
        utiles = Utiles()
        utiles.performclick(context, companyLocators.search_button_xpath)
        return self

    def click_popup_button(self, context):
        companyLocators = Company_locators()
        utiles = Utiles()
        utiles.performclick(context, companyLocators.Click_popup_xpath)
        return self

    def click_cross_button(self, context):
        companyLocators = Company_locators()
        utiles = Utiles()
        utiles.performclick(context, companyLocators.click_cross_button)
        return self

    def click_View_companies(self, context):
        companyLocators = Company_locators()
        utiles = Utiles()
        utiles.performclick(context, companyLocators.View_companies_xpath)
        return self

    def click_Search_field(self, enterdata, context):
        companyLocators = Company_locators()
        utiles = Utiles()
        utiles.performsendkeys(context, companyLocators.Search_field_xpath, enterdata)
        return self

    def click_search_button(self, context):
        companyLocators = Company_locators()
        utiles = Utiles()
        utiles.performclick(context, companyLocators.Search_button_xpath)
        return self

    def click_Export_button(self, context):
        companyLocators = Company_locators()
        utiles = Utiles()
        utiles.performclick(context, companyLocators.export_button_xpath)
        return self

    def click_edit(self, context):
        companyLocators = Company_locators()
        utiles = Utiles()
        utiles.performclick(context, companyLocators.edit_xpath)
        return self

    def Description_field(self, enterdata, context):
        companyLocators = Company_locators()
        utiles = Utiles()
        utiles.performsendkeys(context, companyLocators.Description_xpath, enterdata)
        return self

    def click_update_button(self, context):
        companyLocators = Company_locators()
        utiles = Utiles()
        utiles.performclick(context, companyLocators.update_button_xpath)
        return self

    def click_Change_logo(self, context):
        companyLocators = Company_locators()
        utiles = Utiles()
        utiles.performclick(context, companyLocators.company_change_logo_xpath)
        return self

    def click_company_search_input_field(self, context):
        companyLocators = Company_locators()
        utiles = Utiles()
        utiles.performclick(context, companyLocators.Company_search_button_xpath)
        return self

    def test_return(self, context):
        companyLocators = Company_locators()
        utiles = Utiles()
        utiles.performclick(context, companyLocators.Test_return_xpath)
        return self

    def click_change_type_field(self, context):
        companyLocators = Company_locators()
        utiles = Utiles()
        utiles.performclick(context, companyLocators.Change_type_field_xpath)
        return self

    def click_Dropdown_update_type(self, context):
        companyLocators = Company_locators()
        utiles = Utiles()
        utiles.performclick(context, companyLocators.update_type_xpath)
        return self

    def Click_search_button(self, context):
        companyLocators = Company_locators()
        utiles = Utiles()
        utiles.performclick(context, companyLocators.search_button_xpath)
        return self

    def Click_popup_button(self, context):
        companyLocators = Company_locators()
        utiles = Utiles()
        utiles.performclick(context, companyLocators.Click_popup_xpath)
        return self

    def click_Cross_button(self, context):
        companyLocators = Company_locators()
        utiles = Utiles()
        utiles.performclick(context, companyLocators.click_cross_button)
        return self
