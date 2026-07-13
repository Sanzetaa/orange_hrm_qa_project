from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BasePage:
    LOADER = (By.CSS_SELECTOR, ".oxd-form-loader")

    def wait_for_loader_to_disappear(self, timeout=15):
        try:
            WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(self.LOADER)
        )
        except Exception:
            pass

    def js_click(self, locator, timeout=10):
        element = self.find(locator, timeout)
        self.driver.execute_script("arguments[0].click();", element)

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        ).click() 

    def type(self, locator, text, timeout=10):
        element = self.find(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_url(self):
        return self.driver.current_url

    def wait_for_url_contains(self, partial_url, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(partial_url)
        )

    def find_all_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    def get_text(self, locator, timeout=10):
        return self.find(locator, timeout).text
    
    def press_enter(self, locator, timeout=10):
        self.find(locator).send_keys(Keys.ENTER)

    def get_value(self, locator, timeout=10):
        return self.find(locator, timeout).get_attribute("value")