from scrape import UrlManager

url = "https://www.crunchyroll.com/watch/GRMGQX55R/izuku-midoriya-origin"
url1 ="https://www.crunchyroll.com/watch/G4VUQZ7MX/the-new-threat"
url2 = "https://tubitv.com/tv-shows/395405/s01-e01-end-and-beginning?start=true"

url_manager = UrlManager()
url_manager.add_new_url(url1)
resualt = url_manager.search(url_manager.get_url())

print(resualt)