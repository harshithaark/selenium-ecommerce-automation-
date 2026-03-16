from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

def test_add_to_cart(driver):

    login = LoginPage(driver)
    product = ProductPage(driver)
    cart = CartPage(driver)

    login.login("standard_user", "secret_sauce")

    product.add_product_to_cart()
    product.open_cart()

    assert cart.is_item_present()