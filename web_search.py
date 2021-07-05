from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Web_Search():
  def __init__(self):
      self.driver = webdriver.Edge(r'C:\Users\zacwa\edgedriver_win32\msedgedriver.exe')

  def open_page(self, url):
    self.driver.get(url=url)

  def wikipedia(self, query):
      self.query = query
      self.open_page("https://www.wikipedia.org")

      search_bar = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
      search_bar.click()
      search_bar.send_keys(query)

      search_button = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
      search_button.click()

  def youtube(self, query):
    self.query = query
    self.open_page("https://www.youtube.com")

    search_bar = self.driver.find_element_by_xpath('//*[@id="search"]')
    search_bar.click()
    search_bar.send_keys(query)

    search_button = self.driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
    search_button.click()

  def duckduckgo(self, query):
    self.query = query
    self.query = self.query.replace(" ", "+")
    self.open_page("https://duckduckgo.com/?q=" + self.query)
