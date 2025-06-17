class Config:
    URL = "http://37.203.243.26:5000/"
    search_url = f"{URL}search"
    search_url_api = "http://37.203.243.26:5000/api/search"

    @staticmethod
    def get_clients(query):
        return f"{Config.search_url_api}?q={query}"


