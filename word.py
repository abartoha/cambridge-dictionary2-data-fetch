class Word(BeautifulSoup):
    def __init__(self, url):
        self.url = "https://dictionary.cambridge.org"+url
        self.soup = get(url, headers=headers)
        self.meanings = []
    def getMeanings(self):
        return self.meanings