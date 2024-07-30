from initializer import DriverConstructor
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.action_builder import ActionBuilder
import time


class BookingOperator:
    def __init__(self):
        self.driver = DriverConstructor().get_driver()

    def select_page(
        self, *, location, checkin, checkout, adults=1, rooms=1, children=0
    ):
        url = f"https://www.booking.com/searchresults.en-gb.html?ss={location}&checkin={checkin}&checkout={checkout}&group_adults={adults}&no_rooms={rooms}&group_children={children}&order=price&nflt=ht_id%3D204"
        self.driver.get(url)
        time.sleep(5)
        self.close_google_sign_up_pop_up()
        self.decline_all_cookies()
        self.close_dialog()
        location = self.validate_location()
        prices = self.get_prices()
        # print(
        #     f"Location: {location}, Average: {sum(prices)/len(prices)}, Num Results: {len(prices)}"
        # )
        return location, prices

    def select_location(self, location):
        self.driver.implicitly_wait(10)
        elem = self.driver.find_element(
            By.XPATH, "//input[@placeholder='Where are you going?']"
        )
        self.driver.implicitly_wait(10)
        elem.click()
        self.driver.implicitly_wait(10)
        elem.send_keys(location)
        elem.send_keys(Keys.ENTER)

    def close_dialog(self):
        try:
            self.driver.implicitly_wait(10)
            elem = self.driver.find_element(
                By.XPATH, "//button[@aria-label='Dismiss sign in information.']"
            )
            self.driver.implicitly_wait(10)
            elem.click()
        except Exception:
            pass

    def get_prices(self) -> list[int]:
        self.driver.implicitly_wait(10)
        elems = self.driver.find_elements(
            By.XPATH, "//span[@data-testid='price-and-discounted-price']"
        )
        self.driver.implicitly_wait(10)
        s = 0
        len = elems.__len__()
        results_list = [(int(item.text[1:])) for item in elems]
        return results_list

    def validate_location(self) -> str:
        self.driver.implicitly_wait(1)
        elem = self.driver.find_element(
            By.XPATH, "//input[@placeholder='Where are you going?']"
        )
        self.driver.implicitly_wait(10)
        return elem.get_attribute("value")

    def close_google_sign_up_pop_up(self):
        try:
            self.driver.implicitly_wait(1)
            iframe = self.driver.find_element(
                By.XPATH, "//iframe[@title='Sign in with Google Dialogue']"
            )
            self.driver.implicitly_wait(1)
            self.driver.switch_to.frame(iframe)
            self.driver.implicitly_wait(1)
            elem = self.driver.find_element(By.ID, "close")
            self.driver.implicitly_wait(1)
            elem.click()
            self.driver.implicitly_wait(1)
            self.driver.switch_to.default_content()
        except Exception:
            pass

    def decline_all_cookies(self):
        try:
            self.driver.implicitly_wait(1)
            elem = self.driver.find_element(By.ID, "onetrust-reject-all-handler")
            self.driver.implicitly_wait(1)
            elem.click()
        except Exception:
            pass
