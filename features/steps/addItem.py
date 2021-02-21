from behave import *
from selenium import webdriver
from pageObjects.amazonSelection import AmazonHelper

driver = webdriver.Chrome(executable_path="C:/WebDrivers/Chrome/88.0.4324.96/chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://www.amazon.co.uk/')


##### 1 #####
@given('the users basket has "{count}" items in it')
def getBasketCount(context, count):
    amazon = AmazonHelper(driver)
    curCount = amazon.getBasketCount()
    if curCount == count:
        assert True
    else:
        assert False

@when('the user adds the item to the basket')
def addItem2Basket(context):
    amazon = AmazonHelper(driver)
    amazon.addItem2Basket("gordons gin")

@then('the users basket has "{count}" items in it')
def verifyBasketCount(context, count):
    amazon = AmazonHelper(driver)
    curCount = amazon.getBasketCount()
    if curCount == count:
        assert True
    else:
        assert False


##### 2 #####
@given('the users basket has at least "{count}" item')
def checkBasketCount(context, count):
    amazon = AmazonHelper(driver)
    curCount = amazon.getBasketCount()
    if curCount == count:
        assert True
    else:
        assert False

@when('the user adds another item to the basket')
def addAnotherItem(context):
    amazon = AmazonHelper(driver)
    amazon.addItem2Basket("Yorkshire Tonic Water Mixed Variety Selection Pack")

@then('the users basket has "{count}" more item in it')
def verifyItemCount(context, count):
    amazon = AmazonHelper(driver)
    curCount = amazon.getBasketCount()
    if int(curCount) == (int(count) + 1):
        assert True
    else:
        assert False

##### 3 #####
@given('the users basket has at least "{count}" item in it')
def checkBasketCount(context,count):
    amazon = AmazonHelper(driver)
    curCount = amazon.getBasketCount()
    if curCount >= count:
        assert True
    else:
        assert False

@when('the user adds more than "{count}" item to the basket')
def openHomepage(context, count):
    amazon = AmazonHelper(driver)
    amazon.addMultipleItems2Basket("smirnoff vodka 1ltr", int(count)+2)

@then('the users basket has more than "{count}" item in it')
def verifyLogo(context, count):
    amazon = AmazonHelper(driver)
    curCount = amazon.getBasketCount()
    if curCount >= count:
        assert True
    else:
        assert False

@then('teardown browser')
def closeBrowser(context):
    driver.close()