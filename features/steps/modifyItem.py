from behave import *
from selenium import webdriver
from pageObjects.amazonSelection import AmazonHelper
from pageObjects.amazonBasket import AmazonBasketHelper


#amazonBasket = AmazonBasketHelper()
#amazon = AmazonHelper()

@given('a user is viewing his basket')
def step_impl(context):
    amazon = AmazonHelper(context.driver)
    amazonBasket = AmazonBasketHelper(context.driver)
    curCount = amazon.getBasketCount()
    if curCount >= 1:
        amazonBasket.getBasket()
    else:
        assert False


@when('the user changes the quantity of one of the items')
def step_impl(context):
    amazonBasket = AmazonBasketHelper(context.driver)
    amazonBasket.setBasketQuantity()

@then('the item quantity changes accordingly')
def step_impl(context):
    amazonBasket = AmazonBasketHelper(context.driver)
    curCount = amazonBasket.getItemQuantity()
    if curCount >= 1:
        amazonBasket.getBasket()
    else:
        assert False

@then('the overall number of items in the basket changes accordingly')
def step_impl(context):
    amazon = AmazonHelper(context.driver)
    amazonBasket = AmazonBasketHelper(context.driver)
    curCount = amazon.getBasketCount()
    if curCount >= 1:
        amazonBasket.getBasket()
    else:
        assert False

    return ()
