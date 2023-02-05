from selenium import webdriver
from selenium.webdriver.common.by import By
class UrlManager():
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
        self.types = ['crunchyroll', 'tubi']
        
    def add_new_url(self, url):
        if url is None or len(url) == 0:
            return
        if url in self.new_urls or url in self.old_urls:
            return
        self.new_urls.add(url)
    
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)
            
    def get_url(self):
        if self.has_new_url():
            url = self.new_urls.pop()
            self.old_urls.add(url)
            return url
        else:
            return None
    
    def has_new_url(self):
        return len(self.new_urls) > 0

    def search(self, url):
        browser = webdriver.Chrome()
        browser.get(url)
        resualts = []
        
        if self.types[0] in url:
            element = browser.find_element(By.CLASS_NAME, "erc-current-media-info")
            h4_nodes = element.find_elements(By.TAG_NAME, 'h4')
            for h4_node in h4_nodes:
                resualts.append("Title: "+h4_node.text)
            h1_nodes = element.find_elements(By.TAG_NAME, 'h1')
            for h1_node in h1_nodes:
                resualts.append("Episode: "+h1_node.text)

        elif self.types[1] in url:
            h1_nodes = browser.find_elements(By.TAG_NAME, 'h1')
            for h1_node in h1_nodes:
                resualts.append("Title: "+h1_node.text)
            h2_nodes = browser.find_elements(By.TAG_NAME, 'h2')
            for h2_node in h2_nodes:
                resualts.append("Episode: "+h2_node.text)
                            
        return resualts