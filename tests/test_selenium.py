import time
import pytest
# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from faker import Faker
fake = Faker()


@pytest.fixture()
def chrome_driver_init(request):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_driver = webdriver.Chrome(executable_path=r"./chromedriver", options=chrome_options)
    request.cls.driver = chrome_driver
    chrome_driver.get('http://localhost:7000/')
    chrome_driver.set_window_size(1552, 832)
    time.sleep(5)
    yield
    chrome_driver.close()


@pytest.mark.usefixtures('chrome_driver_init')
class test_browser_with_selenium(LiveServerTestCase):
    def test_newUserRegistration(self):
        self.driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.ID, "name").click()
        name = fake.name()
        self.driver.find_element(By.ID, "name").send_keys(name)
        self.driver.find_element(By.ID, "email").click()
        email = fake.email()
        self.driver.find_element(By.ID, "email").send_keys(email)
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("h1234567")
        self.driver.find_element(By.ID, "passwordConfirm").click()
        self.driver.find_element(By.ID, "passwordConfirm").send_keys("h1234567")
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".mt-3").click()
        time.sleep(3)
        assert self.driver.find_element(By.ID, "username").text == name.upper()

    #
    def test_login(self):
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
        self.driver.find_element(By.ID, "email").send_keys("hamza1@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("h0528419254")
        self.driver.find_element(By.CSS_SELECTOR, ".mt-3").click()
        time.sleep(3)
        assert self.driver.find_element(By.ID, "username").text == "HAMZA"

    def test_verifyInvalidPasswordErrorMessage(self):
        self.driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys("hamza1@gmail.com")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("invalidPassword")
        self.driver.find_element(By.CSS_SELECTOR, ".mt-3").click()
        time.sleep(3)
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".fade").text == "No active account found with the given credentials"

    def test_verifyInvalidEmailAddressErrorMessage(self):
        self.driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys("ivalid@invalid.com")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("h0528419254")
        self.driver.find_element(By.CSS_SELECTOR, ".mt-3").click()
        time.sleep(3)
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".fade").text == "No active account found with the given credentials"

    def test_buyingProduct(self):
        self.driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
        self.driver.find_element(By.ID, "email").send_keys("test11@test.com")
        self.driver.find_element(By.ID, "password").send_keys("h12345678")
        self.driver.find_element(By.CSS_SELECTOR, ".mt-3").click()
        self.driver.execute_script("window.scrollTo(0,711.2000122070312)")
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".col-xl-3:nth-child(3) .card-img").click()
        self.driver.execute_script("window.scrollTo(0,711.2000122070312)")
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".w-100").click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".col-md-3 > .form-control").click()
        dropdown = self.driver.find_element(By.CSS_SELECTOR, ".col-md-3 > .form-control")
        dropdown.find_element(By.XPATH, "//option[. = '2']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".w-100").click()
        self.driver.find_element(By.CSS_SELECTOR, ".justify-content-md-center").click()
        self.driver.find_element(By.ID, "address").send_keys("herzel")
        self.driver.find_element(By.ID, "city").click()
        self.driver.find_element(By.ID, "city").send_keys("akko")
        self.driver.find_element(By.ID, "postalCode").click()
        self.driver.find_element(By.ID, "postalCode").send_keys("25678")
        self.driver.find_element(By.ID, "country").click()
        self.driver.find_element(By.ID, "country").send_keys("israel")
        self.driver.find_element(By.CSS_SELECTOR, ".my-3").click()
        self.driver.find_element(By.CSS_SELECTOR, ".my-3").click()
        time.sleep(2)
        assert self.driver.find_element(By.CSS_SELECTOR, ".card h2").text == "ORDER SUMMARY"

    def test_search_product(self):
        self.driver.find_element(By.NAME, "q").click()
        self.driver.find_element(By.NAME, "q").send_keys("iphone")
        self.driver.find_element(By.CSS_SELECTOR, ".p-2").click()
        time.sleep(3)
        assert self.driver.find_element(By.CSS_SELECTOR, ".col-xl-3:nth-child(2) strong").text in "iphone XS MAX"

# class TestTestlogin():
#     def setup_method(self, method):
#         self.driver = webdriver.Chrome()
#         self.vars = {}
#
#     def teardown_method(self, method):
#         self.driver.quit()


# tests without fixture
# class testBrowser1 (LiveServerTestCase):
#     def test_example(self):
#         chrome_options = Options()
#         chrome_options.add_argument("--headless")
#
#         driver= webdriver.Chrome("./chromedriver",options=chrome_options)
#         # driver.get(("%s%s" %(self.live_server_url,"")))
#         driver.get('http://localhost:7000/admin/')
#         # time.sleep(5)
#         assert "Log in | Django site admin" in driver.title
