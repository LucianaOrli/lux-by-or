class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.add_backpack_btn = "[data-test='add-to-cart-sauce-labs-backpack']"
        self.remove_backpack_btn = "[data-test='remove-sauce-labs-backpack']"
        self.cart_badge = ".shopping_cart_badge"

    def add_item_to_cart(self):
        self.page.locator(self.add_backpack_btn).click()

    def remove_item_from_cart(self):
        self.page.locator(self.remove_backpack_btn).click()

    def get_cart_count(self):
        badge = self.page.locator(self.cart_badge)
        return badge.inner_text() if badge.is_visible() else "0"
