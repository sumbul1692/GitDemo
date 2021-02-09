from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homepage= HomePage(self.driver)
        checkoutpage = homepage.ShopItems()
        log.info("getting all card titles")
        #checkoutpage = CheckoutPage(self.driver)

        cards = checkoutpage.getCardTitles()
        i: int = -1

        for card in cards:
            i = i+1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutpage.getCardFooter()[i].click()

        checkoutpage.checkOutButton().click()
        phone_name = checkoutpage.getPhoneName().text
        assert "Blackberry" in phone_name

        confirmpage = checkoutpage.CheckOutSuccess()
        log.info("Entering country name as Ind")
        confirmpage.enterCountry().send_keys("Ind")
        self.verifyLinkPresence("India")
        confirmpage.selectCountry().click()

        checkbox = confirmpage.selectTermsAndConditions()

        if not checkbox.is_selected():
            checkbox.click()

        confirmpage.hitPurchase().click()

        success_message = confirmpage.getSuccessMessage().text
        log.info("Text received from application is" +success_message)
        assert "Success! Thank you!" in success_message
        print(success_message)







