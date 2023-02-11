from mal import AnimeSearch
from scrape import UrlManager

class getMALid():
    def __init__(self) -> None:
        self.ID = []
    
    def get_ID(self, urls=list):
        url_manager = UrlManager()
        for url in urls:
            url_manager.add_new_url(url)
        resualt = []
        while url_manager.has_new_url() == True:
            resualt.append(url_manager.search(url_manager.get_url()))
        
        for title in resualt:
            self.ID.append(AnimeSearch(title[0][7:]).results[1].mal_id)
            
        return self.ID