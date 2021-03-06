from xueqiu.page.base_page import BasePage
from xueqiu.page.contact_page import ContactPage


class MainPage(BasePage):
    def goto_contact(self):
        self.find_and_click('id', 'menu_contacts')
        return ContactPage(self.driver)
