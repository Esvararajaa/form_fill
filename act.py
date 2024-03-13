from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


class Elements:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def get(self, url):
        return self.driver.get(url)

    def max_screen(self):
        return self.driver.maximize_window()

    def quit(self):
        return self.driver.quit()

    def element(self, locator, value, key=None):
        if key is None:
            if locator.lower() == "id":
                return self.driver.find_element(By.ID, value)
            elif locator.lower() == "css":
                return self.driver.find_element(By.CSS_SELECTOR, value)
            elif locator.lower() == "xpath":
                return self.driver.find_element(By.XPATH, value)
            elif locator.lower() == "name":
                return self.driver.find_element(By.NAME, value)
            elif locator.lower() == "class":
                return self.driver.find_element(By.CLASS_NAME, value)
            elif locator.lower() == "link text":
                return self.driver.find_element(By.LINK_TEXT, value)
            elif locator.lower() == "partial link text":
                return self.driver.find_element(By.PARTIAL_LINK_TEXT, value)
        else:
            if locator.lower() == "id":
                return self.driver.find_element(By.ID, value).send_keys(key)
            elif locator.lower() == "css":
                return self.driver.find_element(By.CSS_SELECTOR, value).send_keys(key)
            elif locator.lower() == "xpath":
                return self.driver.find_element(By.XPATH, value).send_keys(key)
            elif locator.lower() == "name":
                return self.driver.find_element(By.NAME, value).send_keys(key)
            elif locator.lower() == "class":
                return self.driver.find_element(By.CLASS_NAME, value).send_keys(key)
            elif locator.lower() == "link text":
                return self.driver.find_element(By.LINK_TEXT, value).send_keys(key)
            elif locator.lower() == "partial link text":
                return self.driver.find_element(By.PARTIAL_LINK_TEXT, value).send_keys(key)

    def key_act(self, button):
        if button.lower() == "down":
            return ActionChains(self.driver).send_keys(Keys.DOWN).perform()
        if button.lower() == "up":
            return ActionChains(self.driver).send_keys(Keys.UP).perform()
        if button.lower() == "left":
            return ActionChains(self.driver).send_keys(Keys.LEFT).perform()
        if button.lower() == "right":
            return ActionChains(self.driver).send_keys(Keys.RIGHT).perform()

    def implicit_wait(self, time):
        return self.driver.implicitly_wait(time)

    def explicit_wait(self, time, locator, value):
        if locator.lower() == "xpath":
            return WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.XPATH, value)))
        if locator.lower() == "id":
            return WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.ID, value)))
        if locator.lower() == "name":
            return WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.NAME, value)))
        if locator.lower() == "css":
            return WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
        if locator.lower() == "class":
            return WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
        if locator.lower() == "link text":
            return WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.LINK_TEXT, value)))
        if locator.lower() == "partial link text":
            return WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, value)))
        # self.wait.until((EC.presence_of_element_located((locator, value)))
        # self.wait.until((EC.element_located_to_be_selected((locator, value)))
        # self.wait.until((EC.element_to_be_clickable((locator, value)))
        # self.wait.until((EC.element_located_selection_state_to_be((locator, value))))
        # self.wait.until((EC.element_selection_state_to_be((locator, value))))

    def js_scroll(self, element):
        return self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)