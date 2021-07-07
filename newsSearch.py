import requests
import json

class NewsSearch():
  def __init__(self):
    self.api_key = "YOUR API KEY"
    self.newsAPIurl = "https://newsapi.org/v2/top-headlines?country=us&apiKey="

  def getNews(self):
    response = requests.get(self.newsAPIurl + self.api_key)
    self.news = json.loads(response.text)
    return self.news

  def getHeadlines(self):
    self.getNews()
    self.headlines = []

    for i in self.news['articles']:
      self.headlines.append(i['title'])

    return self.headlines

  def getDescriptions(self):
    self.getNews()
    self.descriptions = []

    for i in self.news['articles']:
      self.descriptions.append(i['description'])

    return self.descriptions

  def getContents(self):
    self.getNews()
    self.contents = []

    for i in self.news['articles']:
      self.contents.append(i['content'])

    return self.contents

  def getURLs(self):
    self.getNews()
    self.urls = []

    for i in self.news['articles']:
      self.urls.append(i['url'])

    return self.urls

new = NewsSearch()
new.getNews()
