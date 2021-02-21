

class AmazonBasketHelper():
    def __init__(self, driver):
        self.driver = driver

        self.clickBasket = "hlb-view-cart-announce"
        self.deleteItem = "//input[@data-action='delete']"


    def getBasket(self):
        self.driver.find_element_by_id(self.clickBasket).click()

    def setBasketQuantity(self):
        quantity = 2
        self.driver.find_element_by_xpath("(//span/select/option[@value={}])[2]".format(quantity)).click()

    def getItemQuantity(self):
        itemQuantity = self.driver.find_element_by_xpath("(//span[@class='a-dropdown-prompt'])[2]").text
        return(itemQuantity)