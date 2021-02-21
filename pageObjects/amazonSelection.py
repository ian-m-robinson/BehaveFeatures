import time

class AmazonHelper():
    def __init__(self, driver):
        self.driver = driver

        self.basketCount_link_id = "nav-cart-count"
        self.searchBox = "twotabsearchtextbox"
        self.searchButton = "nav-search-submit-button"
        self.selectFirst = "//div[@data-index='1']//div"
        self.addToCart = "add-to-cart-button"
        self.acceptCookies = "a-autoid-0"


    def getBasketCount(self):
        basketCount = self.driver.find_element_by_id(self.basketCount_link_id).text
        print("Basket Contains {0} items".format(basketCount))
        return(basketCount)

    def addItem2Basket(self, search):
        self.driver.find_element_by_id(self.searchBox).send_keys(search)
        self.driver.find_element_by_id(self.searchButton).click()
        try:
            self.driver.find_element_by_id(self.acceptCookies).click()
        except:
            pass
        self.driver.find_element_by_xpath(self.selectFirst).click()

        time.sleep(2)

        self.driver.find_element_by_id(self.addToCart).click()
        return ()

    def addMultipleItems2Basket(self, search, quantity):
        self.driver.find_element_by_id(self.searchBox).send_keys(search)
        self.driver.find_element_by_id(self.searchButton).click()
        try:
            self.driver.find_element_by_id(self.acceptCookies).click()
        except:
            pass
        self.driver.find_element_by_xpath(self.selectFirst).click()
        self.driver.find_element_by_xpath("//select/option[@value={}]".format(quantity)).click()

        time.sleep(2)

        self.driver.find_element_by_id(self.addToCart).click()
        return ()