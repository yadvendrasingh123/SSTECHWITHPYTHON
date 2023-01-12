from LocatorsPage import Loginlocator
from LocatorsPage.Loginlocator import Login_locators
from Utilities.Utiles import Utiles


class LoginPage(object):

    def __init__(self, context):
        context = context

    def enter_username_in_input_field(self, username, context):
        loginLocators = Login_locators()
        utiles = Utiles()
        utiles.performsendkeys(context, loginLocators.textbox_username_xpath, username)
        return self

    def enter_password_in_input_field(self, password, context):
        loginLocators = Login_locators()
        utiles = Utiles()
        utiles.performsendkeys(context, loginLocators.textbox_password_xpath, password)

        return self

    def click_login_button(self, context):
        loginLocators = Login_locators()
        utiles = Utiles()
        utiles.performclick(context, loginLocators.button_login_xpath)
        return self























    #
    # def click_manage_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.button_manage_xpath)
    #     return self
    #
    # def click_company(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.companies_xpath)
    #     return self
    #
    # def click_Add_company(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.addcompany_xpath)
    #     return self
    #
    # def Company_name_field(self, enterdata, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performsendkeys(context, loginLocators.Company_name_xpath, enterdata)
    #     return self
    #
    # def Country_field(self, enterdata, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performsendkeys(context, loginLocators.Country_xpath, enterdata)
    #     return self
    #
    # def Building_name_field(self, enterdata, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performsendkeys(context, loginLocators.Building_name_xpath, enterdata)
    #     return self
    #
    # def Street_Address_field(self, enterdata, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performsendkeys(context, loginLocators.Street_name_xpath, enterdata)
    #     return self
    #
    # def Suburb_field(self, enterdata, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performsendkeys(context, loginLocators.Suburb_xpath, enterdata)
    #     return self
    #
    # def State_field(self, enterdata, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performsendkeys(context, loginLocators.State_xpath, enterdata)
    #     return self
    #
    # def Postal_code(self, enterdata, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performsendkeys(context, loginLocators.Postal_code_xpath, enterdata)
    #     return self
    #
    # def Contact_number(self, enterdata, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performsendkeys(context, loginLocators.Contact_number_xpath, enterdata)
    #     return self
    #
    # def Email_field(self, enterdata, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performsendkeys(context, loginLocators.Email_xpath, enterdata)
    #     return self
    #
    # def Return_portal_Domain(self, enterdata, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performsendkeys(context, loginLocators.Return_Portal_Domain_xpath, enterdata)
    #     return self
    #
    # def Site_url(self, enterdata, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performsendkeys(context, loginLocators.Site_Url_xpath, enterdata)
    #     return self
    #
    # def click_Submit_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.Submit_button_xpath)
    #     return self
    #
    #
    # def click_change_logo(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.companychangelogo_xpath)
    #     return self
    #
    # def click_Company_search_field(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.Company_search_button_xpath)
    #     return self
    #
    # def field_Test_Return(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.Search_Test_Return_xpath)
    #     return self
    #
    # def click_Change_type_field(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.Change_type_field_xpath)
    #     return self
    #
    # def click_dropdown_add_type(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.Add_type_xpath)
    #     return self
    #
    # def click_Search_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.search_button_xpath)
    #     return self
    #
    # def click_popup_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.Click_popup_xpath)
    #     return self
    #
    # def click_cross_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.click_cross_button)
    #     return self
    #
    # def click_View_companies(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.View_companies_xpath)
    #     return self
    #
    # def click_Search_field(self, enterdata, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performsendkeys(context, loginLocators.Search_field_xpath, enterdata)
    #     return self
    #
    # def click_search_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.Search_button_xpath)
    #     return self
    #
    # def click_Export_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.export_button_xpath)
    #     return self
    #
    # def click_edit(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.edit_xpath)
    #     return self
    #
    # def Description_field(self, enterdata, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performsendkeys(context, loginLocators.Description_xpath, enterdata)
    #     return self
    #
    # def click_update_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.update_button_xpath)
    #     return self
    #
    # def click_Change_logo(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.companychangelogo_xpath)
    #     return self
    #
    # def click_company_search_input_field(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.Company_search_button_xpath)
    #     return self
    #
    # def test_return(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.Test_return_xpath)
    #     return self
    #
    # def click_change_type_field(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.Change_type_field_xpath)
    #     return self
    #
    # def click_Dropdown_update_type(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.update_type_xpath)
    #     return self
    #
    # def Click_search_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.search_button_xpath)
    #     return self
    #
    # def Click_popup_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.Click_popup_xpath)
    #     return self
    #
    # def click_Cross_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.click_cross_button)
    #     return self
    #
    # def click_hub(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.hub_button_xpath)
    #     return self
    #
    # def click_Add_hub(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.add_hub_button_xpath)
    #     return self






















































    # def Click_Test_Return(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performEnter(context, loginLocators.search_button_xpath)
    #     return self
    #

    # def click_retailer_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.retailer_xpath)
    #     return self
    #
    # def input_field(self, enterdata, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performsendkeys(context, loginLocators.input_field1_xpath, enterdata)
    #     return self
    #
    # def click_search_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.button_Search11_xpath)
    #     return self
    #
    # def click_edit_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.edit_button_xpath)
    #     return self
    #
    # def click_assign_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.assign_xpath)
    #     return self
    #
    # def click_country_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.country_xpath)
    #     return self
    #
    # def click_payment_gateway_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.payment_gateway)
    #     return self
    #
    # def click_company(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.companies_xpath)
    #     return self
    #
    # def click_Add_company(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.saddcompany_xpath)
    #     return self
    #
    # def click_Company_changelogo(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.companychangelogo_xpath)
    #     return self
    #
    # def click_hub(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.hub_button_xpath)
    #     return self
    #
    # def click_Add_hub(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.add_hub_button_xpath)
    #     return self
    #
    # def click_Change_hub_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.change_hub_button_xpath)
    #     return self
    #
    # def click_Carrier(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.carrier_button_xpath)
    #     return self
    #
    # def click_ADD_Carrier(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.add_carrier_xpath)
    #     return self
    #
    # def click_Carrier_change(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.carrier_change_xpath)
    #     return self
    #
    # def click_User(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.user_button_xpath)
    #     return self
    #
    # def click_Reporting_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.reporting_xpath)
    #     return self
    #
    # def click_reporting_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.reporting2_xpath)
    #     return self
    #
    # def click_search1_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.search_button_xpath)
    #     return self
    #
    # def click_Report_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.reporting_xpath)
    #     return self
    #
    # def click_return_panding_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.return_panding_xpath)
    #     return self
    #
    # def click_search2_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.search_xpath)
    #     return self
    #
    # def click_voucher_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.voucher_button_xpath)
    #     return self
    #
    # def click_manualreturn_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.manual_return_xpath)
    #     return self
    #
    # def click_setting_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.hover_setting_xpath)
    #     return self
    #
    # def click_API_Trace_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.API_Trace_xpath)
    #     return self
    #
    # def click_setting1_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.hover_setting_xpath)
    #     return self
    #
    # def click_custom_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.custom_API_xpath)
    #     return self
    #
    # def click_setting2_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.hover_setting_xpath)
    #     return self
    #
    # def click_payment_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.payment_setting)
    #     return self
    #
    # def click_setting3_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.hover_setting_xpath)
    #     return self
    #
    # def click_email(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.email_Eqeue_xpath)
    #     return self
    #
    # def click_setting4_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.hover_setting_xpath)
    #     return self
    #
    # def click_custom_message_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.custom_message_xpath)
    #     return self
    #
    # def click_setting5_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.hover_setting_xpath)
    #     return self
    #
    # def click_API_search_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.AP21_Search_xpath)
    #     return self
    #
    # def click_name_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.hover_name_xpath)
    #     return self
    #
    # def click_profile(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.profile_xpath)
    #     return self
    #
    # def click_name1_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.hover_name_xpath)
    #     return self
    #
    # def click_Logout_button(self, context):
    #     loginLocators = Login_locators()
    #     utiles = Utiles()
    #     utiles.performclick(context, loginLocators.Logout_xpath)
    #     return self
