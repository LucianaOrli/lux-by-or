class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.cart_link = ".shopping_cart_link"
        self.checkout_btn = "[data-test='checkout']"
        self.first_name = "[data-test='firstName']"
        self.last_name = "[data-test='lastName']"
        self.zip_code = "[data-test='postalCode']"
        self.continue_btn = "[data-test='continue']"
        self.finish_btn = "[data-test='finish']"
        self.success_header = ".complete-header"

    def finish_checkout(self, fname, lname, zip):
        self.page.locator(self.cart_link).click()
        self.page.locator(self.checkout_btn).click()
        self.page.locator(self.first_name).fill(fname)
        self.page.locator(self.last_name).fill(lname)
        self.page.locator(self.zip_code).fill(zip)
        self.page.locator(self.continue_btn).click()
        self.page.locator(self.finish_btn).click()

    def get_success_message(self):
        return self.page.locator(self.success_header).inner_text()
