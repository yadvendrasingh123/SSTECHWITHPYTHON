class Utiles():
    def performclick(self, object, locator):
        object.browser.find_element_by_xpath(locator).click()

    def performsendkeys(self, object, locator, enterdata):
        object.browser.find_element_by_xpath(locator).send_keys(enterdata)


