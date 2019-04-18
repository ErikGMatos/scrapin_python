"""Exemplo de Page Object no google.com"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
import time
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=1920x1080")
#driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.get("http://www.google.com.br")
# driver.get_screenshot_as_file("capture.png")


class Google:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://google.com.br'
        self.searchBar = 'q'  # name
        self.btn_search = '.FPdoLc.VlcLAe [name=btnK]'  # name
        self.btn_lucky = '.FPdoLc.VlcLAe [name=btnI]'  # name

    def navigate(self):
        self.driver.get(self.url)

    def search(self, browser, word='None'):
        self.driver.find_element_by_name(self.searchBar).send_keys(word)
        actions = ActionChains(browser)
        actions.send_keys(Keys.TAB)
        actions.perform()
        self.driver.find_element_by_css_selector(self.btn_search).click()

    def lucky(self, browser, word='None'):
        self.driver.find_element_by_name(
        self.searchBar).send_keys(word)
        #time.sleep(10) #aguarda o tempo descrito para prosseguir
        actions = ActionChains(browser)
        actions.send_keys(Keys.TAB)
        actions.perform()
        self.driver.find_element_by_css_selector(self.btn_lucky).click()


browserChrome = webdriver.Chrome()
g = Google(browserChrome)
g.navigate()
g.search(browserChrome, 'Live de Python')
browserChrome.quit()

