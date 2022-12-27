from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import os


DRIVER_LOCATION = os.environ['DRIVER_LOCATION']
URL = "https://www.youtube.com/"


class WebDriver:

    def __init__(self, search_for, exclude_this):
        self.search_this = search_for
        self.exclude = exclude_this
        self.service = Service(executable_path=DRIVER_LOCATION)
        self.driver = webdriver.Chrome(service=self.service)

    def open_youtube(self):

        self.driver.get(URL)

    def search_youtube(self):

        search_list = self.driver.find_elements(by=By.ID, value="search")
        time.sleep(5)

        search_list[1].send_keys(self.search_this)
        search_list[1].send_keys(Keys.ENTER)

        time.sleep(10)

        titles = self.driver.find_elements(By.CSS_SELECTOR, ".title-and-badge a")

        title_list = []
        link_list = []

        for title in titles:
            try:
                title_text = title.get_attribute("title")
                link = title.get_attribute("href")
                title_list.append(title_text)
                link_list.append(link)
            except NoSuchElementException:
                print("No title")

        keys_to_delete = []
        final_dict = {title_list[n]: link_list[n] for n in range(10)}
        for key in final_dict.keys():
            split_key = key.split(" ")
            for word in split_key:
                for exclude in self.exclude:
                    if word.lower() == exclude.lower():
                        keys_to_delete.append(key)
        for del_key in keys_to_delete:
            try:
                del final_dict[del_key]
            except KeyError:
                pass
        for key in final_dict.keys():
            print(key, final_dict[key])

        # final_list = [[title_list[n], link_list[n]] for n in range(10)]
        # print(final_list)

        # for listed in final_list:
        #     print(listed)

        self.driver.quit()
