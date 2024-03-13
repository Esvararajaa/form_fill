from act import Elements
from data import test_data
from locator import test_locator


class form:
    e = Elements()
    td = test_data()
    tl = test_locator()

    def data_fill(self):
        self.e.max_screen()
        self.e.get(self.td.url)
        self.e.implicit_wait(20)
        # first name
        self.e.element("name",self.tl.first_name_name).clear()
        self.e.element("name", self.tl.first_name_name, self.td.first_name)
        print("First name entered")
        # last name
        self.e.element("name", self.tl.last_name_name).clear()
        self.e.element("name", self.tl.last_name_name, self.td.last_name)
        print("Last name entered")
        # gender
        male = self.e.element("id", self.tl.gender_male_id)
        if male.is_selected():
            pass
        else:
            male.click()
        # Years of experience
        exp_ele = self.e.element("id",self.tl.experience_4_id)
        self.e.js_scroll(exp_ele)
        exp_ele.click()
        # date
        self.e.element("id", self.tl.date_id, self.td.date)
        print("Date entered")
        # profession
        self.e.element("id", self.tl.manual_tester_id).click()
        print("Profession Manual tester selected")
        self.e.element("id", self.tl.automation_tester_id).click()
        print("Profession Automation tester selected")
        # Automation tools
        self.e.element("id", self.tl.protractor_id).click()
        print("Protractor tool selected")
        # Continent
        self.e.element("id", self.tl.continents_id).click()
        self.e.element("xpath", self.tl.continent_option_xpath).click()
        print("Continent selected")
        # selenium command
        self.e.element("id", self.tl.selenium_command_id).click()
        print("Selenium command selected")
        # upload image
        self.e.element("id", self.tl.upload_image_id, self.tl.jpg_location)
        print("Image uploaded")
        # button
        self.e.element("id", self.tl.button_id).click()
        print("Button clicked")
        self.e.quit()


h = form()
h.data_fill()
