# import region
from selenium import webdriver
from SUP.Libraries.constants import CHROME_DRIVER_PATH as DRIVER_PATH,\
    HTML
from time import sleep


class Reader:
    def __init__(self):
        # Preconditions region
        print("Precondition 1 : Load Google Chrome properly.")
        self.driver = webdriver.Chrome(DRIVER_PATH)
        sleep(5)  # wait for chrome load properly

        print("Precondition 2 : www.ceneo.pl")
        self.driver.get(HTML)
        sleep(5)  # wait for website load properly
        self.driver.get(self.driver.find_element_by_css_selector("#body > div.no-banner > div > div > div.screening-wrapper.bordered-tabs-2020 > div.page-tab-content.click.cf > div.site-full-width.wrapper > div.page-navigation > div > dl > dd:nth-child(3) > div > div > div:nth-child(2) > a:nth-child(2)").get_attribute("href"))

        print(self.read(self.try_top_10()))
        sleep(2)

    def read(self, container) -> list:
        prices = list()
        for item in container:
            value = "#body > div.no-banner > div > div > div.screening-wrapper.bordered-tabs-2020 > div.page-tab-content.click.cf > div.site-full-width.wrapper > section.product-offers-group > table > tbody > tr:nth-child({}) > td.cell-price > a > span > span > span.value".format(item)
            penny = "#body > div.no-banner > div > div > div.screening-wrapper.bordered-tabs-2020 > div.page-tab-content.click.cf > div.site-full-width.wrapper > section.product-offers-group > table > tbody > tr:nth-child({}) > td.cell-price > a > span > span > span.penny".format(item)
            prices.append(self.driver.find_element_by_css_selector(value).text + self.driver.find_element_by_css_selector(penny).text)
        return prices

    def try_top_10(self) -> list:
        container = list()
        for item in range(100):
            string = "#body > div.no-banner > div > div > div.screening-wrapper.bordered-tabs-2020 > div.page-tab-content.click.cf > div.site-full-width.wrapper > section.product-offers-group > table > tbody > tr:nth-child({}) > td.cell-price > a > span > span > span.value".format(
                item)
            try:
                self.driver.find_element_by_css_selector(string).click()
                container.append(item)
            except:
                pass
            if len(container) >= 10:
                break
        return container
