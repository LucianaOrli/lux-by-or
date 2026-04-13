from pytest_bdd import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

@given('the user is logged into the system')
def login_usuario(page):
    login = LoginPage(page)
    login.navigate()
    login.login("standard_user", "secret_sauce")

@when('I select the product "Sauce Labs Backpack"')
def adicionar_produto(page):
    inventory = InventoryPage(page)
    inventory.add_item_to_cart()

@when('I complete the checkout with shipping details')
def finalizar_checkout(page):
    checkout = CheckoutPage(page)
    checkout.finish_checkout("Luciana", "Fonseca", "12345")

@when('I remove the product from the cart')
def remover_produto(page):
    inventory = InventoryPage(page)
    inventory.remove_item_from_cart()

@then('the order should be processed successfully')
def validar_sucesso(page):
    assert page.locator(".complete-header").is_visible()

@then('the system should display the message "Thank you for your order"')
def validar_mensagem(page):
    assert "Thank you" in page.content()

@then('the cart badge should be empty')
def validar_carrinho_vazio(page):
    inventory = InventoryPage(page)
    assert inventory.get_cart_count() == "0"

