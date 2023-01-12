import logging
import time
import webbrowser

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from MethodPage import loginpage
from MethodPage import managepage
from MethodPage import companypage
from MethodPage import hubpage
from MethodPage import retailerpage
from MethodPage import carrierpage
import configparser

config = configparser.ConfigParser()
config.read("Utilities/input.properties")
from behave import *


@given('I launch Chrome browser')
def step_impl(context):
    context.browser = webdriver.Chrome(ChromeDriverManager().install())


@when('I open orange SEKO Homepage')
def step_impl(context):
    context.browser.get((config.get("Url", "base_url")))
    context.browser.maximize_window()


@when('enter username and password')
def step(context):
    login_page = loginpage.LoginPage(context)
    login_page.enter_username_in_input_field(config.get("credential", "correct_username"), context)
    login_page.enter_password_in_input_field(config.get("credential", "correct_password"), context)
    time.sleep(3)


@when('click on login button')
def step(context):
    login_page = loginpage.LoginPage(context)
    login_page.click_login_button(context)
    time.sleep(5)


@Then('click on manage button')
def step(context):
    manage_page = managepage.DashboardPage(context)
    manage_page.click_manage_button(context)
    time.sleep(3)


#
# @Then('click on Company')
# def step(context):
#     company_page = companypage.CompanyPage(context)
#     company_page.click_company(context)
#     time.sleep(3)
#
#
# @Then('Click on Add company')
# def step(context):
#     company_page = companypage.CompanyPage(context)
#     company_page.click_Add_company(context)
#     time.sleep(3)
#
#
# @Then('enter the Company Name "{field}"')
# def step(context, field):
#     company_page = companypage.CompanyPage(context)
#     company_page.Company_name_field(field, context)
#
#
# @Then('enter the Country "{field}"')
# def step(context, field):
#     company_page = companypage.CompanyPage(context)
#     company_page.Country_field(field, context)
#
#
# @Then('enter the Building Name "{field}"')
# def step(context, field):
#     company_page = companypage.CompanyPage(context)
#     company_page.Building_name_field(field, context)
#
#
# @Then('enter the Street Address "{field}"')
# def step(context, field):
#     company_page = companypage.CompanyPage(context)
#     company_page.Street_Address_field(field, context)
#
#
# @Then('enter the Suburb "{field}"')
# def step(context, field):
#     company_page = companypage.CompanyPage(context)
#     company_page.Suburb_field(field, context)
#
#
# @Then('enter the State_City "{field}"')
# def step(context, field):
#     company_page = companypage.CompanyPage(context)
#     company_page.State_field(field, context)
#
#
# @Then('enter the Postcode "{field}"')
# def step(context, field):
#     company_page = companypage.CompanyPage(context)
#     company_page.Postal_code(field, context)
#
#
# @Then('enter the Contact Number "{field}"')
# def step(context, field):
#     company_page = companypage.CompanyPage(context)
#     company_page.Contact_number(field, context)
#
#
# @Then('enter the Email "{field}"')
# def step(context, field):
#     company_page = companypage.CompanyPage(context)
#     company_page.Email_field(field, context)
#
#
# @Then('enter the Return Postal Domain "{field}"')
# def step(context, field):
#     company_page = companypage.CompanyPage(context)
#     company_page.Return_portal_Domain(field, context)
#     time.sleep(3)
#
#
# @Then('enter the Site URL "{field}"')
# def step(context, field):
#     company_page = companypage.CompanyPage(context)
#     company_page.Site_url(field, context)
#
#
# @Then('Click on Submit button')
# def step(context):
#     company_page = companypage.CompanyPage(context)
#     company_page.click_Submit_button(context)
#
#
# @Then('click on Company change logo')
# def step(context):
#     company_page = companypage.CompanyPage(context)
#     company_page.click_change_logo(context)
#     time.sleep(3)
#
#
# @Then('click on search field')
# def step(context):
#     company_page = companypage.CompanyPage(context)
#     company_page.click_Company_search_field(context)
#     time.sleep(3)
#
#
# @Then('click on Test Return')
# def step(context):
#     company_page = companypage.CompanyPage(context)
#     company_page.field_Test_Return(context)
#     time.sleep(1)
#
#
# @Then('Click on Change type field')
# def step(context):
#     company_page = companypage.CompanyPage(context)
#     company_page.click_Change_type_field(context)
#     time.sleep(1)
#
#
# @Then('click on Add type')
# def step(context, ):
#     company_page = companypage.CompanyPage(context)
#     company_page.click_dropdown_add_type(context)
#     time.sleep(1)
#
#
# @Then('Click on search button')
# def step(context):
#     company_page = companypage.CompanyPage(context)
#     company_page.click_Search_button(context)
#     time.sleep(3)
#
#
# @Then('click on popup button')
# def step(context):
#     company_page = companypage.CompanyPage(context)
#     company_page.click_popup_button(context)
#     time.sleep(3)
#
#
# @Then('click on cross button')
# def step(context):
#     company_page = companypage.CompanyPage(context)
#     company_page.click_cross_button(context)
#     time.sleep(3)
#
#
# @Then('click on View Companies')
# def step(context):
#     company_page = companypage.CompanyPage(context)
#     company_page.click_View_companies(context)
#     time.sleep(3)
#
#
# @Then('enter the Search input field "{field}"')
# def step(context, field):
#     company_page = companypage.CompanyPage(context)
#     company_page.click_Search_field(field, context)
#     time.sleep(2)
#
#
# @Then('Click on Search tab')
# def step(context):
#     company_page = companypage.CompanyPage(context)
#     company_page.click_search_button(context)
#     time.sleep(2)
#
#
# @Then('click on Export button')
# def step(context):
#     company_page = companypage.CompanyPage(context)
#     company_page.click_Export_button(context)
#     time.sleep(10)
#
#
# @Then('Click on edit button')
# def step(context):
#     company_page = companypage.CompanyPage(context)
#     company_page.click_edit(context)
#     time.sleep(2)
#
#
# @Then('enter the Description "{field}"')
# def step(context, field):
#     company_page = companypage.CompanyPage(context)
#     company_page.Description_field(field, context)
#
#
# @Then('Click on update button')
# def step(context):
#     company_page = companypage.CompanyPage(context)
#     company_page.click_update_button(context)
#     time.sleep(2)
#
#
# @Then('click on company logo')
# def step(context):
#     company_page = companypage.CompanyPage(context)
#     company_page.click_Change_logo(context)
#     time.sleep(3)
#
#
# @Then('click on company search')
# def step(context):
#     company_page = companypage.CompanyPage(context)
#     company_page.click_company_search_input_field(context)
#     time.sleep(3)
#
#
# @Then('click on test field')
# def step(context):
#     company_page = companypage.CompanyPage(context)
#     company_page.test_return(context)
#     time.sleep(1)
#
#
# @Then('Click on change type')
# def step(context):
#     company_page = companypage.CompanyPage(context)
#     company_page.click_change_type_field(context)
#     time.sleep(1)
#
#
# @Then('click on update')
# def step(context, ):
#     company_page = companypage.CompanyPage(context)
#     company_page.click_Dropdown_update_type(context)
#     time.sleep(1)
#
#
# @Then('Click on search')
# def step(context):
#     company_page = companypage.CompanyPage(context)
#     company_page.Click_search_button(context)
#     time.sleep(3)
#
#
# @Then('click on Popup field button')
# def step(context):
#     company_page = companypage.CompanyPage(context)
#     company_page.Click_popup_button(context)
#     time.sleep(3)
#
#
# @Then('click on cancel button')
# def step(context):
#     company_page = companypage.CompanyPage(context)
#     company_page.click_Cross_button(context)
#     time.sleep(3)

#
# @Then('click on Hub button')
# def step(context):
#     hub_page = hubpage.HubPage(context)
#     hub_page.Click_hub(context)
#
#
# @Then('click on Add hub button')
# def step(context):
#     hub_page = hubpage.HubPage(context)
#     hub_page.click_hub_add(context)
#
#
# @Then('click on name of company')
# def step(context):
#     hub_page = hubpage.HubPage(context)
#     hub_page.input_company_name(context)
#
#
# @Then('click on company name')
# def step(context):
#     hub_page = hubpage.HubPage(context)
#     hub_page.test_return(context)
#
#
# @Then('enter the name "{field}"')
# def step(context, field):
#     hub_page = hubpage.HubPage(context)
#     hub_page.input_name(field, context)
#
#
# @Then('enter the description field "{field}"')
# def step(context, field):
#     hub_page = hubpage.HubPage(context)
#     hub_page.input_description(field, context)
#
#
# @Then('enter the building "{field}"')
# def step(context, field):
#     hub_page = hubpage.HubPage(context)
#     hub_page.input_building(field, context)
#
#
# @Then('enter the address "{field}"')
# def step(context, field):
#     hub_page = hubpage.HubPage(context)
#     hub_page.input_address(field, context)
#
#
# @Then('enter the country name "{field}"')
# def step(context, field):
#     hub_page = hubpage.HubPage(context)
#     hub_page.input_country(field, context)
#
#
# @Then('enter the suburub "{field}"')
# def step(context, field):
#     hub_page = hubpage.HubPage(context)
#     hub_page.input_Suburub(field, context)
#
#
# @Then('enter the city field "{field}"')
# def step(context, field):
#     hub_page = hubpage.HubPage(context)
#     hub_page.input_city(field, context)
#
#
# @Then('enter the postcode "{field}"')
# def step(context, field):
#     hub_page = hubpage.HubPage(context)
#     hub_page.inputpostcode(field, context)
#
#
# @Then('enter the email "{field}"')
# def step(context, field):
#     hub_page = hubpage.HubPage(context)
#     hub_page.email(field, context)
#
#
# @Then('click on serviceable')
# def step(context):
#     hub_page = hubpage.HubPage(context)
#     hub_page.serviceable(context)
#
#
# @Then('click on submit')
# def step(context):
#     hub_page = hubpage.HubPage(context)
#     hub_page.submit(context)
#     time.sleep(3)


@Then('click on Retailer')
def step(context):
    retailer_page = retailerpage.RetailerPage(context)
    retailer_page.click_Retailer(context)
    time.sleep(3)


@Then('click on Add')
def step(context):
    retailer_page = retailerpage.RetailerPage(context)
    retailer_page.click_Add_retiler(context)
    time.sleep(3)


@Then('click on Test return')
def step(context):
    retailer_page = retailerpage.RetailerPage(context)
    retailer_page.click_company(context)
    time.sleep(3)


@Then('click on choose file')
def step(context):
    retailer_page = retailerpage.RetailerPage(context)
    retailer_page.click_choose_file(context)
    time.sleep(3)


@Then('enter the return "{field}"')
def step(context, field):
    retailer_page = retailerpage.RetailerPage(context)
    retailer_page.click_field(field, context)
    time.sleep(3)


@Then('enter the name "{field}"')
def step(context, field):
    retailer_page = retailerpage.RetailerPage(context)
    retailer_page.input_name_field(field, context)
    time.sleep(3)


@Then('click on carrier')
def step(context):
    carrier_page = carrierpage.CarrierPage(context)
    carrier_page.click_carrier(context)
    time.sleep(3)


@Then('click on add carrier')
def step(context):
    carrier_page = carrierpage.CarrierPage(context)
    carrier_page.click_add_carrier(context)
    time.sleep(3)

# @Then('click on retailer button')
# def step(context):
#     home_page = homepage.HomePage(context)
#     home_page.click_retailer_button(context)
#     time.sleep(2)
#
#
# @Then('enter the input field "{field}"')
# def step(context, field):
#     home_page = homepage.HomePage(context)
#     home_page.input_field(field, context)
#     time.sleep(2)
#
#
# @Then('click on search button')
# def step(context):
#     home_page = homepage.HomePage(context)
#     home_page.click_search_button(context)
#     time.sleep(2)
#
#
# @Then('click on edit button')
# def step(context):
#     home_page = homepage.HomePage(context)
#     home_page.click_edit_button(context)
#     time.sleep(2)
#
#
# @Then('click on assign button')
# def step(context):
#     home_page = homepage.HomePage(context)
#     home_page.click_assign_button(context)
#     time.sleep(2)
#
#
# @Then('click on country button')
# def step(context):
#     home_page = homepage.HomePage(context)
#     home_page.click_country_button(context)
#     time.sleep(2)
#
#
# @Then('click on payment gateway button')
# def step(context):
#     home_page = homepage.HomePage(context)
#     home_page.click_payment_gateway_button(context)
#     time.sleep(2)
#
#
# @Then('click on reporting button')
# def step(context):
#     home_page = homepage.HomePage(context)
#     home_page.click_Reporting_button(context)
#     time.sleep(2)
#
#
# @Then('click on reporting2 button')
# def step(context):
#     home_page = homepage.HomePage(context)
#     home_page.click_reporting_button(context)
#     time.sleep(2)
#
#
# @Then('click on search1 button')
# def step(context):
#     home_page = homepage.HomePage(context)
#     home_page.click_search1_button(context)
#     time.sleep(2)
#
#
# @Then('click on report button')
# def step(context):
#     home_page = homepage.HomePage(context)
#     home_page.click_Reporting_button(context)
#     time.sleep(2)
#
#
# @Then('click on report pending button')
# def step(context):
#     home_page = homepage.HomePage(context)
#     home_page.click_return_panding_button(context)
#     time.sleep(2)
#
#
# @Then('click on search3 button')
# def step(context):
#     home_page = homepage.HomePage(context)
#     home_page.click_search2_button(context)
#     time.sleep(2)
#
#
# @Then('click on voucher')
# def step(context):
#     home_page = homepage.HomePage(context)
#     home_page.click_voucher_button(context)
#     time.sleep(2)
#
#
# @Then('click on manual return')
# def step(context):
#     home_page = homepage.HomePage(context)
#     home_page.click_manualreturn_button(context)
#     time.sleep(2)
#
#
# @Then('click on setting')
# def step(context):
#     home_page = homepage.HomePage(context)
#     home_page.click_setting_button(context)
#     time.sleep(3)
#
#
# @Then('click on API Trace')
# def step(context):
#     home_page = homepage.HomePage(context)
#     home_page.click_API_Trace_button(context)
#     time.sleep(2)
#
#
# @Then('click on setting1')
# def step(context):
#     home_page = homepage.HomePage(context)
#     home_page.click_setting1_button(context)
#     time.sleep(3)
#
#
# @Then('click on custom API')
# def step(context):
#     home_page = homepage.HomePage(context)
#     home_page.click_custom_button(context)
#     time.sleep(2)
#
#
# @Then('click on setting2')
# def step(context):
#     home_page = homepage.HomePage(context)
#     home_page.click_setting2_button(context)
#     time.sleep(3)
#
#
# @Then('click on  payment')
# def step(context):
#     home_page = homepage.HomePage(context)
#     home_page.click_payment_button(context)
#     time.sleep(2)
#
#
# @Then('click on setting3')
# def step(context):
#     home_page = homepage.HomePage(context)
#     home_page.click_setting3_button(context)
#     time.sleep(3)
#
#
# @Then('click on email')
# def step(context):
#     home_page = homepage.HomePage(context)
#     home_page.click_email(context)
#     time.sleep(2)
#
#
# @Then('click on setting4')
# def step(context):
#     home_page = homepage.HomePage(context)
#     home_page.click_setting4_button(context)
#     time.sleep(3)
#
#
# @Then('click on custom message')
# def step(context):
#     home_page = homepage.HomePage(context)
#     home_page.click_custom_message_button(context)
#     time.sleep(2)
#
#
# @Then('click on setting5')
# def step(context):
#     home_page = homepage.HomePage(context)
#     home_page.click_setting5_button(context)
#     time.sleep(3)
#
#
# @Then('click on API21 Search')
# def step(context):
#     home_page = homepage.HomePage(context)
#     home_page.click_API_search_button(context)
#     time.sleep(2)
#
#
# @Then('click on akash')
# def step(context):
#     home_page = homepage.HomePage(context)
#     home_page.click_name_button(context)
#     time.sleep(2)
#
#
# @Then('click on profile')
# def step(context):
#     home_page = homepage.HomePage(context)
#     home_page.click_profile(context)
#     time.sleep(2)
#
#
# @Then('click on akash1')
# def step(context):
#     home_page = homepage.HomePage(context)
#     home_page.click_name1_button(context)
#     time.sleep(2)
#
#
# @Then('click on Logout')
# def step(context):
#     home_page = homepage.HomePage(context)
#     home_page.click_Logout_button(context)
#     time.sleep(2)
