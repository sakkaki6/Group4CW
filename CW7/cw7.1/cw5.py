class Cache:
    def __init__(self):
        self.cache = {}
        print("\nCache initialized.")

    def __del__(self):
        self.cache.clear()
        print("\nCache cleared.")

def test_cache():
    
    cache = Cache()
    
    cache.cache['1'] = 'red'
    cache.cache['2'] = 'blue'
    print("\nItems added to cache:", cache.cache)
    
    del cache
    print("\nCache object deleted.")

test_cache()
