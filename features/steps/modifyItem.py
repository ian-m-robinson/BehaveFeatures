from behave import *
from pageObjects.amazonSelection import AmazonHelper
from pageObjects.amazonBasket import AmazonBasketHelper
from addItem import driver


@given('a user is viewing his basket')
def step_impl(context):
    amazon = AmazonHelper(driver)
    amazonBasket = AmazonBasketHelper(driver)
    curCount = amazon.getBasketCount()
    if curCount >= 1:
        amazonBasket.getBasket()
    else:
        assert False


@when('the user changes the quantity of one of the items')
def step_impl(context):
    amazonBasket = AmazonBasketHelper(driver)
    amazonBasket.setBasketQuantity()

@then('the item quantity changes accordingly')
def step_impl(context):
    amazonBasket = AmazonBasketHelper(driver)
    curCount = amazonBasket.getItemQuantity()
    if curCount >= 1:
        amazonBasket.getBasket()
    else:
        assert False

@then('the overall number of items in the basket changes accordingly')
def step_impl(context):
    amazon = AmazonHelper(context.driver)
    amazonBasket = AmazonBasketHelper(driver)
    curCount = amazon.getBasketCount()
    if curCount >= 1:
        amazonBasket.getBasket()
    else:
        assert False

    return ()
