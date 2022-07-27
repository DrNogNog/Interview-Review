# All cached data is stored in a hash!

cache = {}
def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_fromserver(url)
        cache[url] = data
        return data