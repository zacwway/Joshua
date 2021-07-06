from selenium import webdriver

class WebSearch():
  def __init__(self):
      self.driver = webdriver.Edge(r'C:\Users\zacwa\edgedriver_win32\msedgedriver.exe')

  def openPage(self, url):
    self.driver.get(url=url)

  def wikipedia(self, query):
      self.openPage("https://www.wikipedia.org")

      search_bar = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
      search_bar.click()
      search_bar.send_keys(query)

      search_button = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
      search_button.click()

  def youtube(self, query):
    self.openPage("https://www.youtube.com")

    search_bar = self.driver.find_element_by_xpath('//*[@id="search"]')
    search_bar.click()
    search_bar.send_keys(query)

    search_button = self.driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
    search_button.click()

  def duckduckgo(self, query):
    self.query = query.replace(" ", "+")
    self.openPage("https://duckduckgo.com/?q=" + self.query)

  def openSite(self, query):
    self.query = query.replace(" ", "+")
    self.openPage("https://duckduckgo.com/?q=" + self.query + "+!")

  def openInYoutube(self, query):
    self.openPage("https://www.youtube.com/results?search_query=" + query)

    video = self.driver.find_element_by_xpath('//*[@id="dismissible"]')
    video.click()
